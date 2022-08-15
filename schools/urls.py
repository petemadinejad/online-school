from rest_framework.routers import DefaultRouter

from schools.views import *

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='schools')
router.register(r'school-types', SchoolTypeViewSet, basename='school-types')