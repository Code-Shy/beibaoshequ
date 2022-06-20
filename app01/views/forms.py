import hashlib

from django.core.exceptions import ValidationError

from app01 import models
from django import forms
import re


class RegForm(forms.ModelForm):
    exclude = ['last_time', 'is_active', 'email']

    re_password = forms.CharField(widget=forms.PasswordInput, label="确认密码", min_length=6)
    password = forms.CharField(widget=forms.PasswordInput, label="密码", min_length=6)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 默认显示
        field = self.fields['type']
        choices = field.choices
        choices[0] = ('', '用户类别')
        field.choices = choices

        for name, field in self.fields.items():
            if name in self.exclude:
                continue
            if field.widget.attrs:
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "placeholder": field.label
                }

    class Meta:
        model = models.User
        fields = ['username', 'password', 're_password', 'phone', 'type', 'avatar']
        exclude = ['last_time', 'is_active', 'email']
        widgets = {
            "password": forms.PasswordInput()
        }

    def clean_phone(self):
        self._validate_unique = True  # 数据库校验唯一
        phone = self.cleaned_data.get('phone')
        if re.match(r'^1[3-9]\d{9}$', phone):
            return phone
        raise ValidationError('手机号格式错误')

    def clean(self):
        password = self.cleaned_data.get('password', '')
        re_pwd = self.cleaned_data.get('re_password')
        if password == re_pwd:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md5.hexdigest()

            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')


class InformationForm(forms.ModelForm):
    exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in self.exclude:
                continue
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

    class Meta:
        model = models.User
        fields = ['username', 'phone']


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['author'].choices = [(self.instance.author_id, self.instance.author.username)]

    class Meta:
        model = models.Article
        fields = '__all__'
        exclude = ['detail']


class ArticleDetailForm(forms.ModelForm):
    class Meta:
        model = models.ArticleDetail
        fields = '__all__'


class ResourceForm(forms.ModelForm):
    exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in self.exclude:
                continue
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

    class Meta:
        model = models.Resource
        fields = "__all__"
