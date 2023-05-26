from django.contrib import admin
from some_generic_sm.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('username', 'first_name', 'last_name',)
    ordering = ('-id',)


admin.site.register(User, UserAdmin)
