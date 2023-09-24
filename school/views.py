from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from school.models import Kurs, Lesson, Payments
from school.serializers import KursSerializer, LessonSerializer, PaymentsSerializer


# ViewSet для Курсов
class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()


# Созданеи урока
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


# Просмотр всего списка уроков
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Просмотр информации об одном уроке
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Внесение изменений в урок
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Удаление урока
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


# Создание платежа за урок или курс
class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


# Просмотр всего списка платежей
class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('kurs', 'lesson', 'payment_method')  # Категории, по которым мможно фильтровать платежи
    ordering_fields = ('date',)  # Сортировка по дате
