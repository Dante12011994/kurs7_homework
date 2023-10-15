from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from school.models import Kurs, Lesson
from users.models import User


class SchoolTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.ru', password='12345', is_staff=True, is_superuser=True,
                                        is_active=True, is_moderator=False)
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(title='test', owner=self.user)

    def test_create_lesson(self):
        # тест создания урока
        data = {
            'title': 'test'
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        # проверка статуса исполнения
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # проверка итогового значения
        self.assertEquals(
            response.json(),
            {'id': 2, 'title': 'test', 'description': None, 'intro': None, 'video': None, 'kurs': None, 'owner': 1}
        )

    def test_list_lesson(self):
        # тест просмотра списка уроков
        response = self.client.get('/lesson/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(len(response.data), 4)

    def test_update_lesson(self):
        # тест изменения урока
        data = {
            'title': 'test update'
        }

        response = self.client.patch(
            f'/lesson/update/{self.lesson.id}/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()
        self.assertEquals(
            self.lesson.title,
            data['title']
        )

    def test_delete_lesson(self):
        # тест удаления урока
        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())
