from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewSetCategories,ViewSetPost

router = DefaultRouter()

router.register(r'',ViewSetPost,basename='post')
router.register(r'',ViewSetCategories,basename='categories')


urlpatterns = [
    path('', include(router.urls)),
]