from school.apps import SchoolConfig
from django.urls import path
from rest_framework.routers import DefaultRouter

from school.views import KursViewSet, LessonListAPIView, LessonDestroyAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView, LessonCreateAPIView, PaymentsCreateAPIView, PaymentsListAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'kurs', KursViewSet, basename='kurs')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  path('payments/create/', PaymentsCreateAPIView.as_view(), name='payment-create'),
                  path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
              ] + router.urls
