from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='dante1201@mail.ru',
            first_name='Dante',
            last_name='Dante',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password('12345')
        user.save()
