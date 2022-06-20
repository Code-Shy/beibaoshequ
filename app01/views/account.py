import hashlib

from django.shortcuts import render, redirect

from app01 import models
from app01.views.forms import RegForm, InformationForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        user_obj = models.User.objects.filter(username=username, password=md5.hexdigest(), is_active=True).first()

        if user_obj:
            # 登陆成功
            # 保存登陆状态
            request.session['is_login'] = True
            request.session['username'] = user_obj.username
            request.session['pk'] = user_obj.pk
            url = request.GET.get('url')
            if url:
                return redirect(url)
            return redirect('index')
        error = '用户名或密码错误'
    return render(request, 'login.html', locals())


def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('login')

    return render(request, 'register.html', {
        'form_obj': form_obj
    })


def logout(request):
    request.session.delete()
    return redirect('login')


def information(request):
    """ 编辑管理员 """
    row_object = models.User.objects.filter(id=request.session['pk']).first()
    print(row_object)
    form = InformationForm(instance=row_object)
    return render(request, "information.html", {
        'form': form,
        'obj': row_object
    })
