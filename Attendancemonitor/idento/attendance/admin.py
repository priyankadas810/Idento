from django.contrib import admin
from .models import user_registration, admin_registration

# Register your models here.
admin.site.register(user_registration)

admin.site.register(admin_registration)