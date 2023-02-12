from django.contrib import admin
from basicbankserver.models import accounts, User
from django.contrib.auth.admin import UserAdmin



admin.site.register(accounts)

admin.site.register(User, UserAdmin)
