from django.db import models

# Create your models here.
from django.urls import reverse


class City(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=250,verbose_name="Заголовк")
    slug=models.SlugField(max_length=250,unique=True,db_index=True,verbose_name="Слог")
    #slug = models.SlugField(max_length=250, default=" ", db_index=True)
    content=models.TextField(blank = True,verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    #is_published=models.BooleanField(default=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True,verbose_name="Фото")  # Поле для изображения


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug.strip()})




