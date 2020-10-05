from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# class AccountAdmin(UserAdmin):
#     list_display = (
#         'email', 'username', 'date_joined', 'is_admin', 'is_active',
#         'is_staff', 'is_superuser')
#     search_fields = ('email', 'username')
#     readonly_fields = ('date_joined')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


admin.site.register(Jovens)
admin.site.register(Tribo)
admin.site.register(Grupo)
admin.site.register(Reuniao)
admin.site.register(Relatorio)
# admin.site.register(Account, AccountAdmin)
