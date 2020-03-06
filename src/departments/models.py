from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.models import BaseModel


class Department(BaseModel):
    name = models.CharField(_("name"), max_length=120)
    short_name = models.CharField(_("short name"), max_length=3, unique=True)
    address = models.CharField(_("address"), max_length=240)
    created = models.DateTimeField(_("created date"), auto_now_add=True)
    updated = models.DateTimeField(_("updated date"), editable=False, auto_now=True)

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")
        ordering = ("-created",)

    def __str__(self):
        return self.name
