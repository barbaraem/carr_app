from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.models import BaseModel


class Car(BaseModel):
    registration_no = models.CharField(
        _("registration number"), max_length=7, unique=True
    )
    brand = models.CharField(_("brand of a car"), max_length=60, blank=True, default="")
    model = models.CharField(_("model of a car"), max_length=60, blank=True, default="")
    weight = models.PositiveIntegerField(_("weight"), blank=True, null=True)
    production_date = models.DateField(_("date of production"), blank=True, null=True)
    passengers_no = models.IntegerField(_("maximum number of passengers allowed "), blank=True, null=True)
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name=_("department"),
    )

    class Meta:
        verbose_name = _("car")
        verbose_name_plural = _("cars")
        ordering = ("-created",)

    def __str__(self):
        return self.registration_no
