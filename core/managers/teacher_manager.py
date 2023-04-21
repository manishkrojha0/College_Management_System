"""Manager file for teacher model."""
from core.models.teacher import Teacher

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


    # first_name = models.CharField(max_length=100)
    # middle_name = models.CharField(max_length=100, null=True)
    # last_name = models.CharField(max_length=100, null=True)
    # dob = models.DateField()
    # gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)
    # email_id = models.EmailField(null=True)
    # contact = models.CharField(max_length=15, validators=[validate_contact])

    # emp_id = models.CharField(max_length=10, null=True, unique=True, db_index=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    # user_address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, related_name='teacher_address')
    
    def create_bulk(self, request_data):
        """Create."""
        print(request_data)
        for data in request_data:
            user_id = data.get('user', {}).get('id', {})
            
            m = Teacher(**data)
            print(m)
            m.save()
        # first_name = data.get('first_name')
        # middle_name = data.get('middle_name')
        # last_name = data.get('last_name')
        # dob = data.get('dob')
        # gender = data.get('gender')
        # email_id = data.get('email_id')
        # contact = data.get('contact')
        # emp_id = data.get('emp_id')

