from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Блокирует создание и удаление курсов и уроков.
    """
    def has_permission(self, request, view):
        if request.user.is_moderator:
            return False
        return True


class IsOwnerOrModerator(BasePermission):
    """
    Разрешает пользователю просмотр и редактирование только своих уроков и курсов,
    если он не модератор.
    """
    def has_permission(self, request, view):
        if request.user.is_moderator:
            return True
        return request.user == view.get_object().owner

