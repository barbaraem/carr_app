from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(_("created date"), auto_now_add=True)
    updated = models.DateTimeField(_("updated date"), editable=False, auto_now=True)

    class Meta:
        abstract = True
