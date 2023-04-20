"""Manager file for teacher model."""
from models.teacher import Teacher

class TeacherManager(object):
    """class of teacher manager."""

    def __init__(self) -> None:
        pass

    def load_by_id(self, id):
        """laod teacher by id."""
        try:
            teacher_obj = Teacher.objects.get(pk=id)
        except Exception:
            teacher_obj = None
        
        return teacher_obj
    
    def load_all(self):
        """Load all the teachers."""
        try:
            teacher_objs = Teacher.objects.all()
        except Exception:
            teacher_objs = None
        
        return teacher_objs
    
    def load_by_emp_id(self, emp_id):
        """Load teacher by employee id."""
        try:
            teacher_obj = Teacher.objects.get(emp_id=emp_id)
        except Exception:
            teacher_obj = None
        
        return teacher_obj
