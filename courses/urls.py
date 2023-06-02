from django.urls import path,include
from django.contrib import admin
from courses.views import CourseViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'courses',CourseViewSet)
urlpatterns = [
    path('',include(router.urls))
]
