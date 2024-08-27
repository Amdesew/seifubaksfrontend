from rest_framework import serializers
from .models import NewStudent, StudentResult

class NewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewStudent
        fields = "__all__"

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = "__all__"