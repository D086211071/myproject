from django.contrib import admin
from .models import registerforms,authentication,superusers
admin.site.register(registerforms)
admin.site.register(authentication)
admin.site.register(superusers)
