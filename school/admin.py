from django.contrib import admin

from school.models import Payments


# Register your models here.
@admin.register(Payments)
class Paymentsadmin(admin.ModelAdmin):
    list_display = ("user", "date", "pay", "payment_method")
