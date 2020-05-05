from django.contrib import admin

from .models import BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    # 设置 列表页 显示字段名字的
    list_display = ['id', 'category', 'small_category', 'name', 'author', 'store', 'price']


# 注册模型类 到 admin站点里面去
admin.site.register(BookInfo, BookInfoAdmin)

admin.site.site_header = '京东书城'
admin.site.site_title = '京东书城MIS'
admin.site.index_title = '欢迎使用京东书城MIS'
