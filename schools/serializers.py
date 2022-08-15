from rest_framework import serializers
from .models import School, SchoolType


class SchoolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolType
        fields = ('name', 'description', 'is_enable',)


class SchoolSerializer(serializers.ModelSerializer):
    school_type = SchoolTypeSerializer()

    class Meta:
        model = School
        fields = ('name', 'address', 'zipcode', 'phone', 'website', 'school_type', 'head_master', 'is_enable', 'image')
