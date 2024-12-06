from rest_framework import serializers

from application.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','phone_no','email']