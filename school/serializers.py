from rest_framework import serializers

from school.models import Kurs, Lesson, Payments


# Сериалайзер для модели уроков
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


# Сериалайзер для модели курсов
class KursSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()  # Вывод количства уроков в курсе
    lessons_list = LessonSerializer(source='lesson_set', many=True)  # Вывод списка уроков в курсе

    class Meta:
        model = Kurs
        fields = "__all__"

    # Метод для вывода списка уроков
    def get_lessons(self, instance):
        if instance.lesson_set.all():
            return len(instance.lesson_set.all())
        return 0


# Сериалайзер для модели платежей
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
