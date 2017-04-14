#encoding:utf-8
from distutils.core import setup  
setup(name='DjangoCaptcha',  
      author='TY',  
      author_email='tianyu0915@gmail.com',  
      version='0.3.3', 
      description='A Captcha module for Django. Py3 supported',
      keywords ='django,captcha',
      url='http://github.com/tianyu0915/DjangoCaptcha',  
      packages=['DjangoCaptcha'],  
      install_requires=['six', 'pillow'],
      package_data={'DjangoCaptcha':['*.*','DjangoCaptcha/*.*']},

)  
