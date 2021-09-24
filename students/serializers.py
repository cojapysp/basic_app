from rest_framework import serializers
from .models import student_data

class student_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_data
        fields = ['id', 'name', 'roll_no', 'grade', 'result']