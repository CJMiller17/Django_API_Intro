from rest_framework import serializers
from .models import Student, Instructor, Course, Grade

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'courses']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'instructor']

class GradeSerializer(serializers.ModelSerializer):
    # letter_grade = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ['id', 'course', 'score', 'student'] #'letter_grade'
    
    # def get_letter_grade(self, obj):
    #     if (obj.score >= 90):
    #         return 'A'
    #     elif (obj.score >= 80):
    #         return 'B'
    #     elif (obj.score >= 70):
    #         return 'C'
    #     elif (obj.score >= 60):
    #         return 'D'
    #     else:
    #         return 'F'




# course = Course.objects.get(id = 1)

# print('*****************************')

# print(f'Before Serializer: {course}')
# course_serializer = CourseSerializer(course)
# print('*****************************')
# print(f'After Serializer: {course_serializer.data}')
# print('*****************************')