from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class User(models.Model):
    """ 用户表 """
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    type_choices = (
        (1, '超级管理员'),
        (2, '管理员'),
        (10, '普通用户'),
        (11, 'VIP用户')
    )
    type = models.SmallIntegerField(verbose_name='用户类别', choices=type_choices)
    email = models.EmailField(verbose_name='邮箱')

    phone = models.CharField(max_length=11, verbose_name='手机号')
    last_time = models.DateTimeField(null=True, blank=True, verbose_name='上次登陆时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='img/avatar', default='img/avatar/default_avatar.jpg')

    def __str__(self):
        return self.username


class Category(models.Model):
    """ 板块表 """
    title = models.CharField(max_length=64, verbose_name='板块名称')

    def __str__(self):
        return self.title


class Article(models.Model):
    def __str__(self):
        return self.title

    """ 文章表 """
    title = models.CharField(max_length=64, verbose_name='文章标题')
    abstract = models.CharField(max_length=256, verbose_name='文章摘要')
    author = models.ForeignKey(to='User', on_delete=models.DO_NOTHING, null=True, verbose_name='作者')
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='所属板块')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    publish_status = models.BooleanField(default=False, choices=((False, '未发布'), (True, '发布'),), verbose_name='发布状态')
    detail = models.OneToOneField('ArticleDetail', on_delete=models.CASCADE)
    delete_status = models.BooleanField(default=False, choices=((False, '未删除'), (True, '删除'),), verbose_name='文章状态')

    def show_publish_status(self):
        color_dict = {True: 'green', False: '#c35353'}

        return mark_safe(
            '<span style="background: {};color: white;padding: 3px" >{}</span>'.format(color_dict[self.publish_status],
                                                                                       self.get_publish_status_display()))


class ArticleDetail(models.Model):


    """ 文章详情表 """
    content = RichTextField(verbose_name='文章内容')


class Comment(models.Model):
    def __str__(self):
        return self.content

    """ 评论表 """
    content = models.TextField(verbose_name='评论内容')
    author = models.ForeignKey(to='User', on_delete=models.DO_NOTHING, null=True, verbose_name='评论者')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='评论文章')
    time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.BooleanField(default=True, verbose_name='审核状态')


class Resource(models.Model):
    def __str__(self):
        return self.name

    """ 资源 """
    name = models.CharField(verbose_name="资源名称", max_length=32)
    introduction = models.CharField(verbose_name="资源简介", max_length=128)
    resource = models.FileField(verbose_name="资源文件", max_length=1024, upload_to="resource")
    type_choices = (
        (0, '文献资料'),
        (1, '代码资料'),
        (2, '数据集')
    )
    type = models.SmallIntegerField(verbose_name='文献类别', choices=type_choices)

