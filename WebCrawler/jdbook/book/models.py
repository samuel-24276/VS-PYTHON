from django.db import models


# Create your models here.
# 1.创建模型类
class BookInfo(models.Model):
    # 2.定义字段  属性
    # 大分类
    category = models.CharField(max_length=50, verbose_name='大类', default='大类')
    small_category = models.CharField(max_length=50, verbose_name='小类', default='小类')
    name = models.CharField(max_length=200, default="无", verbose_name="书名")
    author = models.CharField(max_length=50, default="无", verbose_name="作者", null=True)
    store = models.CharField(max_length=100, default="无", verbose_name="出版社", null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="价格", null=True)
    default_image = models.ImageField(max_length=200, null=True, verbose_name="图片")

    class Meta:  # 别名
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    # 魔法函数
    def __str__(self):
        return self.name

# 3.终端操作 数据迁移
