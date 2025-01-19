from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from django.urls import path
from .views import CurrentUserView



router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns = [
    path('auth/users/me/', CurrentUserView.as_view(), name='current-user'),
]



