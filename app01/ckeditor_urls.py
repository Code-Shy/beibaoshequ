from __future__ import absolute_import

from django.urls import re_path
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views

urlpatterns = [
    re_path(r'^upload/', views.upload, name='ckeditor_upload'),
    re_path(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
]
