from django.db import models
from django.db.models.query import QuerySet
from django.utils.timezone import now
from core.utils.helpers import utc_to_timezone_date
import pytz


class BaseModel(models.Model):
    """Custom model to be inherited as base while making other models."""

    created = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        default_permissions = ('add', 'change', 'delete', 'view')

    def display_created(self, *args, **kwargs):
        """Used to display created in current timezone."""
        return utc_to_timezone_date(self.created).replace(tzinfo=pytz.timezone('UTC'))

