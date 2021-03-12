from django.db import models
from accounts.models import User

class TopicManager(models.Manager):
    # Topic操作に関する処理を追加
    pass

class CommentManager(models.Manager):
    # Comment操作に関する処理を追加
    pass

class CategoryManager(models.Manager):
    # Category操作に関する処理を追加
    pass

class Category(models.Model):
    name = models.CharField(
        '学科名',
        max_length=50,
    )
    url_code = models.CharField(
        'URLコード',
        max_length=50,
        null=True,
        blank=False,
        unique=True,
    )
    sort=models.IntegerField(
        verbose_name='ソート',
        default=0,
    )
    objects = CategoryManager

    def __str__(self):
        return self.name

class Topic(models.Model):
    user_name = models.CharField(
        '学籍番号',
        max_length=30,
        null=True,
        blank=False,
    )
    title = models.CharField(
        '講義名',
        max_length=255,
        null = False,
        blank = False,
    )
    message = models.TextField(
        verbose_name='講義情報',
        null=True,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='学科名',
        on_delete=models.PROTECT,
        null=True,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        null=True,
        blank=True,
    )
    objects = TopicManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )
    no = models.IntegerField(
        default=0,
    )
    user_name = models.CharField(
        '学籍番号',
        max_length=30,
        null=True,
        blank=False,
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
    )
    message = models.TextField(
        verbose_name='投稿内容'
    )
    pub_flg = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        null=True,
        blank=True,
    )
    objects = CommentManager()

    def __str__(self):
        return '{}-{}'.format(self.topic.id, self.no)