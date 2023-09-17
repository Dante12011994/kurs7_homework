from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Kurs(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    intro = models.ImageField(upload_to='img/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    intro = models.ImageField(upload_to='img/', verbose_name='Превью', **NULLABLE)
    video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
