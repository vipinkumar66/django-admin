from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural  = "Categories"
    def __str__(self):
        return self.name


class Post(models.Model):
    options = (
        ("draft","Draft"),
        ("published","Published")
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 default=1)
    title = models.CharField(max_length=250, help_text="Enter the name for you Post")
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    publish = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name="blog_posts", help_text="selcet from the drop down, if not than create it")
    content = models.TextField()

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Post")
        ordering = ("-publish",)