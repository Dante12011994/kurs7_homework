from django.core.management import BaseCommand

from school.models import Payments, Kurs, Lesson


class Command(BaseCommand):
    def handle(self, *args, **kvargs):
        payment_list = [
            {'kurs': Kurs.objects.get(pk=2), 'user': 'Ivan', 'date': '2019-10-10', 'pay': '1000', 'payment_method': 'card'},
            {'lesson': Lesson.objects.get(pk=2), 'user': 'Petr', 'date': '2020-01-01', 'pay': '2000', 'payment_method': 'cash'},
            {'kurs': Kurs.objects.get(pk=2), 'user': 'Gogi', 'date': '2021-01-01', 'pay': '3000', 'payment_method': 'card'}
        ]

        for pay in payment_list:
            Payments.objects.create(**pay)
