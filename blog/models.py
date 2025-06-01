from django.db import models
from django.utils.html import format_html



# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True,null=True)

    def img_tag(self):
        if self.image:
            return format_html('<img src="{}" style="width:40px;height:40px;" />', self.image.url)
        return "No Image"

    img_tag.short_description = "Image"

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title

MATERIAL_ADMIN_SITE = {
    'HEADER':  'IBlogs Admin Login',  # Admin site header
    'TITLE':  'IBlogs',  # Admin site title

}