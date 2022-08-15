from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import School, SchoolType
from .serializers import SchoolSerializer, SchoolTypeSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for listing or retrieving school.
        """

    def list(self, request):
        queryset = School.objects.all()
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = School.objects.all()
        school = get_object_or_404(queryset, pk=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class SchoolTypeViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for listing or retrieving school type.
        """

    def list(self, request):
        queryset = SchoolType.objects.all()
        serializer = SchoolTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SchoolType.objects.all()
        school_type = get_object_or_404(queryset, pk=pk)
        serializer = SchoolTypeSerializer(school_type)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
