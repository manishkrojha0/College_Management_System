"""Manager file for classes."""
from models.classes import Classes


class ClassesManager(object):
    """Class for classes manager."""

    def __init__(self) -> None:
        pass

    def load_by_id(self, id):
        """Load class by id."""
        try:
            class_obj = Classes.objects.get(pk=id)
        except Exception:
            class_obj = None
        
        return class_obj

    def load_by_filter(self, **kwargs):
        """Load class by filter."""
        try:
            class_objs = Classes.objects.filter(**kwargs)
        except Exception:
            class_objs = None
        
        return class_objs
        
