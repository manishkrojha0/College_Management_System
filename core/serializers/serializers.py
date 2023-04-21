from rest_framework import serializers
from core.models.classes import Classes
from core.models.student import Student
from core.models.teacher import Teacher
from core.models.user_address import UserAddress
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['street_address', 'landmark', 'city', 'pincode']
        
    def create(self, validated_data):
        print(validated_data)
        address = User.objects.create_user(
            street_address=validated_data['street_address'],
            landmark=validated_data['landmark'],
            city=validated_data['city'],
            pincode=validated_data['pincode']
        )
        return address

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    user_address = UserAddressSerializer()
    exclude = ('user',)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user_address_data = validated_data.pop('user_address')
        

        user_serializer = UserSerializer(data={'username': user_data['username'], 'email': user_data['email'], 'password': user_data['password']})
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        user_address_data["user"] = user.id
        user_address = UserAddressSerializer(data=user_address_data)
        user_address.is_valid(raise_exception=True)
        user_address = user_address.save()


        teacher = Teacher.objects.create(user_id=user.id, user_address=user_address, **validated_data)

        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        user_address_data = validated_data.pop('user_address', None)

        if user_data:
            user = instance.user
            user_serializer = UserSerializer(user, data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            user_address_data['user'] = user.id

        if user_address_data:
            user_address = instance.user_address
            user_address_serializer = UserAddressSerializer(user_address, data=user_address_data)
            user_address_serializer.is_valid(raise_exception=True)
            user_address_serializer.save()

        return super().update(instance, validated_data)


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    user_address = UserAddressSerializer()

    class Meta:
        model = Student
        fields = '__all__'
    
        def create(self, validated_data):

            user_data = validated_data.pop('user')
            user_address_data = validated_data.pop('user_address')
            

            user_serializer = UserSerializer(data={'username': user_data['username'], 'email': user_data['email'], 'password': user_data['password']})
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            user_address_data["user"] = user.id
            user_address = UserAddressSerializer(data=user_address_data)
            user_address.is_valid(raise_exception=True)
            user_address = user_address.save()


            teacher = Student.objects.create(user_id=user.id, user_address=user_address, **validated_data)

            return teacher

class ClassSerializer(serializers.ModelSerializer):
    teacher_class = TeacherSerializer(many=True)
    student_class = StudentSerializer(many=True)

    class Meta:
        model = Classes
        fields = '__all__'
    


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
