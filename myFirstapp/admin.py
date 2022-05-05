
# Register your models here.
from django.contrib import admin

from .models import onlineFeature , offlineFeature

admin.site.register(onlineFeature)
admin.site.register(offlineFeature)
