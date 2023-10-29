from rest_framework import serializers

from school.models import Kurs, Lesson, Payments, Subscription
from school.servises import creates_payment_intent, retrieve_payment_intent
from school.validators import LinkValidator


# Сериалайзер для модели уроков
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LinkValidator(field='video')
        ]


# Сериалайзер для модели курсов
class KursSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()  # Вывод количства уроков в курсе
    lessons_list = LessonSerializer(source='lesson_set', many=True)  # Вывод списка уроков в курсе
    subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Kurs
        fields = "__all__"
        validators = [
            LinkValidator(field='video')
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    # Метод для вывода списка уроков
    def get_lessons(self, instance):
        if instance.lesson_set.all():
            return len(instance.lesson_set.all())
        return 0

    # Метод для отображения подписки на курс
    def get_subscription(self, instance):
        user = self.request.user
        sub_all = instance.subscription.all()
        for sub in sub_all:
            if sub.subscriber == user:
                return True
        return False


# Сериалайзер для модели платежей
class PaymentsSerializer(serializers.ModelSerializer):
    payment_stripe = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def get_payment_stripe(self, instance):
        if self.request.stream.method == 'POST':
            stripe_id = creates_payment_intent(int(instance.amount))
            obj_payments = Payments.objects.get(id=instance.id)
            obj_payments.stripe_id = stripe_id
            obj_payments.save()
            return retrieve_payment_intent(stripe_id)
        if self.request.stream.method == 'GET':
            if not instance.stripe_id:
                return None
            return retrieve_payment_intent(instance.stripe_id)

    class Meta:
        model = Payments
        fields = "__all__"


# Сериалайзер для модели подписок
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
