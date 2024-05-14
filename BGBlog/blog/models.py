from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.utils import timezone

# My Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['parent__id', 'position']

    def __str__(self) -> str:
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('i', 'investigation'), #pending
        ('b', 'Back'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category,related_name='articles')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name="Premium Articles")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        return format_html("<img width=50 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = 'Image'

    def category_to_str(self):
         return ','.join([category.title for category in self.category.active()])
    category_to_str.short_description = 'Category'

    def get_absolute_url(self):
        return reverse("account:home")

    objects = ArticleManager()

