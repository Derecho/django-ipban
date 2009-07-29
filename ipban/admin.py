from django.contrib import admin
from models import Ban

class BanAdmin(admin.ModelAdmin):
    list_display = ('ip', 'date', 'duration', 'reason', 'banned')
    list_filter = ('date',)

admin.site.register(Ban, BanAdmin)
