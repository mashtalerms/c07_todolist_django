from django.contrib import admin

from core.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('last_login', 'date_joined',)
    list_display = ('username', 'email', 'first_name', 'last_name',)
    search_fields = ('email', 'last_name', 'username',)
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    exclude = ('password',)


admin.site.register(User, UserAdmin)
