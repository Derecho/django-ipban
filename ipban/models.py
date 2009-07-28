from django.db import models
from django.utils.translation import ugettext_lazy as _

class Ban(models.Model):
    ip = models.IPAddressField(_('IP Address'))
    reason = models.TextField(_('Reason for ban'))
    date = models.DateTimeField(_('Date banned'), auto_now_add=True)

    def __str__(self):
        return self.ip

    class Admin: pass
