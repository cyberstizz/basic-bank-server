from django.contrib import admin
from basicbankserver.models import customers, accounts, User
from django.contrib.auth.admin import UserAdmin


admin.site.register(customers)

admin.site.register(accounts)

admin.site.register(User, UserAdmin)
