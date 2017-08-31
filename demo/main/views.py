#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response as render
from DjangoCaptcha import Captcha

def code(request):
    ca =  Captcha(request)
    ca.words = ['google','twitter','facebook', 'tomcat', 'nginx']
    ca_mode = request.GET.get('mode', 'word').lower()
    assert ca_mode in ['number', 'word', 'four_number']

    ca.mode = ca_mode
    return ca.display()

def index(request):
    ca_mode = request.GET.get('mode', 'word').lower()
    assert ca_mode in ['number', 'word', 'four_number']

    _code = request.GET.get('code') or ''
    if not _code:
        return render('index.html',locals())

    ca = Captcha(request)
    if ca.validate(_code):
        return HttpResponse("""<h1>^_^</h1><a href="/">back</a>""")
    return HttpResponse("""<h1>:-(</h1><a href="/">back</a>""")

