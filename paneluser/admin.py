from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User,ticket,orders,payment,packs,ticketpm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets  = (
		('اطلاعات ورود', {
			'fields': ('username', 'password')
		}),

		('اطلاعات شخصی', {
			'fields': ('first_name', 'last_name', 'email','phonenumber')
		}),

		('دسترسی‌ها', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
	)
    add_fieldsets = (
		('اطلاعات ورود', {
			'fields': ('username', 'password1', 'password2','phonenumber')
		}),
	)

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(ticket)
admin.site.register(orders)
admin.site.register(payment)
admin.site.register(packs)
admin.site.register(ticketpm)