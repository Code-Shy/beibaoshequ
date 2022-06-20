from app01 import models
from django.contrib import admin

admin.site.register(models.User)
admin.site.register(models.Resource)
admin.site.register(models.Article)
admin.site.register(models.ArticleDetail)
admin.site.register(models.Comment)


admin.site.site_header = '背包知识社区管理后台'  # 设置header
admin.site.site_title = '背包知识社区管理后台'  # 设置title
admin.site.index_title = '背包知识社区管理后台'

