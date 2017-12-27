from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_not_zero(value):
    if not value:
        raise ValidationError(_('Zero value is not allowed'))
