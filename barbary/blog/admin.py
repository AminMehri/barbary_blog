from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
