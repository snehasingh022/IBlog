from django.contrib import admin
from .models import Category
from .models import Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('img_tag','title','description',)
    search_fields = ('title','description','image')

class PostAdmin(admin.ModelAdmin):
    list_display =('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5


    class Media:
        js = (
              'https://cdn.tiny.cloud/1/uxhwj0kc12wr0uzekjj9mztq021q63o1ts79jqi5z59e35h6/tinymce/7/tinymce.min.js',
              'js/script.js',
            )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)