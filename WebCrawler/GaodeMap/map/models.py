from django.db import models


# Create your models here.
# 1.创建模型类
class MapInfo(models.Model):
    label = models.CharField(max_length=100, null=False, verbose_name="城市编号")
    name = models.CharField(max_length=200, default="无", verbose_name="城市")
    cdi = models.CharField(max_length=200, default="无", verbose_name="交通拥堵指数")
    hlrr = models.CharField(max_length=200, default="无", verbose_name="高延时运行时间占比")
    mrcr = models.CharField(max_length=200, default="无", verbose_name="拥堵路段里程比")
    speed = models.CharField(max_length=200, default="无", verbose_name="平均速度")
    rrsdr = models.CharField(max_length=200, default="无", verbose_name="道路运行速度偏差率")
    """
    cdi = models.DecimalField(decimal_places=2, max_digits=20, default="0.00", verbose_name="交通拥堵指数")
    hlrr = models.DecimalField(decimal_places=2, max_digits=20, default="0.00", verbose_name="高延时运行时间占比")
    mrcr = models.DecimalField(decimal_places=2, max_digits=20, default="0.00", verbose_name="拥堵路段里程比")
    speed = models.DecimalField(decimal_places=2, max_digits=20, default="0.00", verbose_name="平均速度")
    rrsdr = models.DecimalField(decimal_places=2, max_digits=20, default="0.00", verbose_name="道路运行速度偏差率")
    """

    class Meta:  # 别名
        verbose_name = "全国主要城市最近七天内平均交通数据"
        verbose_name_plural = verbose_name

    # 魔法函数
    def __str__(self):
        return self.name
