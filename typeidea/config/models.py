from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(verbose_name="标题", max_length=50)
    href = models.URLField(verbose_name="链接")
    status = models.PositiveIntegerField(verbose_name="状态", choices=STATUS_ITEMS, default=STATUS_NORMAL)
    weight = models.PositiveIntegerField(verbose_name="权重", default=1, choices=zip(range(1, 6),range(1, 6)), help_text="权重高展示顺序靠前")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "友链"
    
class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )

    title = models.CharField(verbose_name="标题", max_length=50)
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容", help_text="如果设置的不是HTML，可为空")
    status = models.PositiveIntegerField(verbose_name="状态", choices=STATUS_ITEMS, default=STATUS_SHOW)
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"