from django.db import models
from mdeditor.fields import MDTextField

class Article(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name='Название статьи'
    )
    
    text = MDTextField(
        null=True, 
        blank=True,
        verbose_name='Markdown редактор'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
