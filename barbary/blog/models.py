from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from ckeditor.fields import RichTextField


class Article(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('d', 'draft')
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, null=True, blank=True)
    description = RichTextField()
    thumbnail = models.ImageField(upload_to="images")
    alt_thumbnail = models.CharField(max_length=128, null=True, blank=True)
    title_thumbnail = models.CharField(max_length=128, null=True, blank=True)
    keywords = models.CharField(max_length=256, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']

