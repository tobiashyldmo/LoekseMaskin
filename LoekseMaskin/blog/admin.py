from django.contrib import admin
from .models import blog


class blogAdmin(admin.ModelAdmin):
    fields = ['headline', 'leadParagraph', 'article', 'publishedDate']

admin.site.register(blog, blogAdmin)
