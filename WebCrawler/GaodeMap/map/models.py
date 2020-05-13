from django.db import models


# Create your models here.
# 1.创建模型类
class MapInfo(models.Model):
    """
    date = models.CharField(max_length=20, null=False, verbose_name="日期")
    name = models.CharField(max_length=200, default="无", verbose_name="城市")
    """
    cdi = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="交通拥堵指数")
    hlrr = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="高延时运行时间占比")
    mrcr = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="拥堵路段里程比")
    speed = models.DecimalField(decimal_places=2, max_digits=10, default="0.00", verbose_name="平均速度")

    class Meta:  # 别名
        verbose_name = "青岛市交通数据"
        verbose_name_plural = verbose_name

