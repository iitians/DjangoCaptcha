DjangoCaptcha 
=======================
[![PyPI version](https://badge.fury.io/py/DjangoCaptcha.png)](http://badge.fury.io/py/DjangoCaptcha)


介绍
----
在django中生成英文单词验证码,提供验证码图片生成,检查验证码等功能



#### 新特性
+ 新增数字验证码模式
+ 字体尺寸根据图片长宽自适应

#### TODO
- [ ] 增加干扰强度的配置选项，用户可以根据需要选择不同的干扰强度输出
- [ ] 增加默认单词库的长度
- [ ] 增加批量生成验证码图片功能



Quick Start
---
Installing DjangoCaptcha module

```
pip install DjangoCaptcha
or
easy_install DjangoCaptcha
```

Implement views

```
from DjangoCaptcha import Captcha

def captcha(request):
    ca =  Captcha(request)
    ca.words s= ['hello','world','helloworld']
    ca.mode = 'word'
    ca.img_width    = 100
    ca.img_height   = 30
    return ca.display()

```

Validate

```
from DjangoCaptcha import Captcha
def index(request):
    value = request.GET.get('code') or ''
    if not value:
        return render('index.html',locals())

    ca = Captcha(request)
    if ca.validate(value):
        return HttpResponse('valid')
    else:
        return HttpResponse('invalid')
```

#### Configuration ####
-----
##### The width value of image
`ca.img_width` = 150
##### The height value of captch image
`ca.img_height` = 30

