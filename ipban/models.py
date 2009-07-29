from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta

class Ban(models.Model):
    ip = models.IPAddressField(_('IP Address'))
    reason = models.TextField(_('Reason for ban'))
    date = models.DateTimeField(_('Date banned'), auto_now_add=True)
    duration = models.IntegerField(_('Ban duration in days (leave blank for permanent)'), blank=True, null=True)
    
    def banned(self):
        if self.duration:
            if datetime.now() > (self.date + timedelta(days=self.duration)):
                return False
            else:
                return True
        else:
            return True
    
    def unbandate(self):
        if self.duration:
            return self.date + timedelta(days=self.duration)
        else:
            return False

    def __str__(self):
        return self.ip

    class Admin: pass
