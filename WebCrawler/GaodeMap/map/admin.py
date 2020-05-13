from django.contrib import admin

from .models import MapInfo


class MapInfoAdmin(admin.ModelAdmin):
    # 设置 列表页 显示字段名字的
    list_display = ['id', 'date', 'name', 'cdi', 'hlrr', 'mrcr', 'speed']


# 注册模型类 到 admin站点里面去
admin.site.register(MapInfo, MapInfoAdmin)

admin.site.site_header = '全国主要城市交通数据'
admin.site.site_title = '青岛市交通数据'
admin.site.index_title = '欢迎查看交通数据'
