from rest_framework import serializers, exceptions
from .models import Student, Course

class StudentSerializer(serializers.Serializer):
    names=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    address=serializers.CharField()
    
    def validate(self, attrs):
        age=attrs.get('age')
        if age < 18:
            raise exceptions.ValidationError('sorry you must be 18 and above to register')
        return attrs
    
    def create(self, validated_data):
        return validated_data
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['name']
    
class StudentCreateSerializer(serializers.ModelSerializer):
    course=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Student
        fields=['names', 'age', 'email', 'address', 'course']

    def Validate(self, attrs):
        age=attrs.get('age')
        if age < 18:
            raise exceptions.ValidationError('sorry you must be 18 and above to register')
        return attrs
    
class StudentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['names', 'age', 'email', 'course']
