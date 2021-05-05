from django.contrib import admin
from django.conf import settings
from userAuth.models import UserAccount


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email',
                    'created_at', "is_active", "is_superuser"]


admin.site.register(UserAccount, UserAdmin)
