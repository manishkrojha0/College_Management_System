"""Manager file for student model."""
from models.student import student

class studentManager(object):
    """class of student manager."""

    def __init__(self) -> None:
        pass

    def load_by_id(self, id):
        """laod student by id."""
        try:
            student_obj = student.objects.get(pk=id)
        except Exception:
            student_obj = None
        
        return student_obj
    
    def load_all(self):
        """Load all the students."""
        try:
            student_objs = student.objects.all()
        except Exception:
            student_objs = None
        
        return student_objs
    
    def load_by_roll_no(self, emp_id):
        """Load student by roll id."""
        try:
            student_obj = student.objects.get(roll_no=emp_id)
        except Exception:
            student_obj = None
        
        return student_obj
