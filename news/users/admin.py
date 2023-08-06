from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChangeForm, CustomUserCreationForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)

