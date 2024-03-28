from django.contrib import admin
from .models import Channel
from import_export.admin import ImportExportModelAdmin

class ChannelAdmin(ImportExportModelAdmin):
    list_display=["user","channel_name","status"]


admin.site.register(Channel, ChannelAdmin)
