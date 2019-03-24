from django.db import models
from blog.models import Post

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, verbose_name="评论目标", on_delete=models.CASCADE)
    content = models.CharField(verbose_name="内容", max_length=2000)
    nickname = models.CharField(verbose_name="昵称", max_length=50)
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱", max_length=254)
    status = models.PositiveIntegerField(verbose_name="状态", choices=STATUS_ITEMS, default=STATUS_NORMAL)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = "评论"