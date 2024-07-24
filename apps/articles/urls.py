from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleAPIView 

router = DefaultRouter()
router.register(r'articles', ArticleAPIView)


urlpatterns = [
    path('', include(router.urls)),
]