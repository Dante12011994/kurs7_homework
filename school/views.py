from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from school.models import Kurs, Lesson, Payments
from school.permissions import IsModerator, IsOwnerOrModerator
from school.serializers import KursSerializer, LessonSerializer, PaymentsSerializer


# ViewSet для Курсов
# class KursViewSet(viewsets.ModelViewSet):
#     serializer_class = KursSerializer
#     queryset = Kurs.objects.all()
#     permission_classes = [IsAuthenticated]


# Созданеи курса
class KursCreateAPIView(generics.CreateAPIView):
    serializer_class = KursSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        new_kurs = serializer.save()
        new_kurs.owner = self.request.user
        new_kurs.save()


# Просмотр всего списка курсов
class KursListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Kurs.objects.all()
    permission_classes = [IsAuthenticated]


# Просмотр информации об одном курсе
class KursRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Kurs.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


# Внесение изменений в курс
class KursUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Kurs.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


# Удаление курса
class KursDestroyAPIView(generics.DestroyAPIView):
    queryset = Kurs.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


# Созданеи урока
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


# Просмотр всего списка уроков
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


# Просмотр информации об одном уроке
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


# Внесение изменений в урок
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


# Удаление урока
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


# Создание платежа за урок или курс
class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated, IsModerator]


# Просмотр всего списка платежей
class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('kurs', 'lesson', 'payment_method')  # Категории, по которым мможно фильтровать платежи
    ordering_fields = ('date',)  # Сортировка по дате
    permission_classes = [IsAuthenticated, IsModerator]


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
