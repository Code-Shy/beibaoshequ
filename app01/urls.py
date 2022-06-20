from django.urls import path, re_path

from app01.views import account, index, article, backend, resource, paper, comment

urlpatterns = [
    path('login/', account.login, name='login'),
    path('register/', account.register, name='register'),
    path('logout/', account.logout, name='logout'),
    path('information/', account.information, name='information'),

    path('index/', index.index, name='index'),
    path('article/<int:pk>/',article.article, name='article'),
    # re_path(r'^article/(?P<pk>(\d+))/$', article.article, name='article'),

    path('backend/', backend.backend, name='backend'),
    path('article_list/', backend.article_list, name='article_list'),
    path('article_add/', backend.article_add, name='article_add'),
    path('article_edit/<int:pk>', backend.article_edit, name='article_edit'),
    path('article_delete/<int:pk>', backend.article_delete, name='article_delete'),

    path('resource_list/', resource.resource_list, name='resource_list'),
    path('resource_add/<int:type>', resource.resource_add, name='resource_add'),

    path('paper_list/', paper.paper_list, name='paper_list'),

    path('comment/', comment.comment, name='comment'),

]
