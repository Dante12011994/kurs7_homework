import re

from rest_framework.serializers import ValidationError


class LinkValidator:
    """
    Валидатор поверки прикрепленной ссылки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value:
            if not bool(re.search(r'youtube.com', field_value)):
                raise ValidationError('Указана некорректная ссылка, необходим youtube')
