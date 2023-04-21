"""Manager file for notification manager."""

from core.models.notification import Notification

class NotificationManager(object):
    """Notification manager class."""

    def __init__(self) -> None:
        pass

    def load_by_id(self, id):
        """Load by id."""
        try:
            noti_obj = Notification.objects.get(pk=id)
        except Exception:
            noti_obj = None
        
        return noti_obj
    
    def load_by_filter(self, **kwargs):
        """Load by filter."""
        try:
            noti_objs = Notification.objects.filter(**kwargs)
        except Exception:
            noti_objs = None
        
        return noti_objs

