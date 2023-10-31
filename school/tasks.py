from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from school.models import Kurs, Subscription


@shared_task()
def send_update(course_id):
    kurs = Kurs.objects.get(pk=course_id)
    kurs_sub = Subscription.objects.filter(course=course_id)
    for sub in kurs_sub:
        send_mail(subject=f"{kurs.name}",
                  message=f"Курс {kurs.name} был обновлен",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[f'{sub.subscriber}'],
                  fail_silently=True
                  )
