from django.contrib import admin
from .models import Members


# Register your models here.
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    pass