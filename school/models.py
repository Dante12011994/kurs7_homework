from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Kurs(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    intro = models.ImageField(upload_to='img/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    linc = models.URLField(verbose_name='Ссылка', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    kurs = models.ForeignKey('Kurs', on_delete=models.CASCADE, **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    intro = models.ImageField(upload_to='img/', verbose_name='Превью', **NULLABLE)
    video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    kurs = models.ForeignKey('Kurs', on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, blank=True)

    METHOD = [('card', 'картой'), ('cash', 'наличными')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    date = models.DateField(verbose_name='дата оплаты')
    pay = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=4, choices=METHOD, default='card')
    stripe_id = models.CharField(max_length=255, verbose_name='id платежа на stripe', **NULLABLE)


class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Подписчик',
                                   **NULLABLE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, **NULLABLE, related_name='subscription',
                               verbose_name='Подписка на курс')

    def __str__(self):
        return f'{self.subscriber}:{self.kurs}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
