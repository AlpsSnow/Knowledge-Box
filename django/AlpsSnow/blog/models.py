from django.db import models

# Create your models here.

class Category(models.Model):
    """blog的分类"""
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """blog的标签"""
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """blog的文章"""
    title = models.CharField(max_length = 100)                  #字符字段
    body = models.TextField()
    created_time = models.DateTimeField()                       #日期时间字段
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank=True)    # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete = True)    # ForeignKey用于定义两个模型简单关联关系，表示多对1（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank =True)             # ManyToManyField用于定义两个模型简单关联关系，表示多对多（1个Tag对应多个post，1个post对应1个Tag,）
    views = models.PositiveIntegerField(default = 0)            # PositiveIntegerField表示正整数，阅读量
    class Meta:
        ordering = ('-created_time',)
    def __str__(self):
        return self.title