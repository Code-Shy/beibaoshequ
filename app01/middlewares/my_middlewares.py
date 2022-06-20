from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import re

from XSZS.settings import WHITE_LIST
from app01 import models


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):


        is_login = request.session.get('is_login')
        if is_login:
            obj = models.User.objects.filter(pk=request.session.get('pk')).first()
            request.my_user = obj
            return
        # 默认所有地址都要登录才能访问
        # 设置一个白名单，不登陆就可以访问
        url = request.path_info
        for i in WHITE_LIST:
            if re.match(i, url):
                return

        return redirect('{}?url={}'.format(reverse('login'), url))
