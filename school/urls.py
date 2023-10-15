from school.apps import SchoolConfig
from django.urls import path
from rest_framework.routers import DefaultRouter

from school.views import LessonListAPIView, LessonDestroyAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView, LessonCreateAPIView, PaymentsCreateAPIView, PaymentsListAPIView, PaymentsDestroyAPIView, \
    KursCreateAPIView, KursListAPIView, KursRetrieveAPIView, KursUpdateAPIView, KursDestroyAPIView, \
    SubscriptionCreateApiView, SubscriptionDestroyAPIView

app_name = SchoolConfig.name

# router = DefaultRouter()
# router.register(r'kurs', KursViewSet, basename='kurs')

urlpatterns = [
    # Курсы
    path('kurs/create/', KursCreateAPIView.as_view(), name='kurs-create'),
    path('kurs/', KursListAPIView.as_view(), name='kurs-list'),
    path('kurs/<int:pk>/', KursRetrieveAPIView.as_view(), name='kurs-get'),
    path('kurs/update/<int:pk>/', KursUpdateAPIView.as_view(), name='kurs-update'),
    path('kurs/delete/<int:pk>/', KursDestroyAPIView.as_view(), name='kurs-delete'),

    # Уроки
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    # Платежи
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payment-create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('payments/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments-delete'),

    # Подписки
    path('subscription/create/', SubscriptionCreateApiView.as_view(), name='subscription-create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
]  # + router.urls
