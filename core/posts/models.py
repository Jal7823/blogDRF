from django.db import models
from markdownx.models import MarkdownxField

class Category(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    image = models.ImageField('Image', upload_to='posts/image/',null=True,blank=True)
    post = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        managed = True
        verbose_name = 'post'
        verbose_name_plural = 'posts'