from django.urls import path
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, PublicationListCreateView, \
    PublicationRetrieveUpdateDestroyView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('publications/', PublicationListCreateView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationRetrieveUpdateDestroyView.as_view(), name='publication-detail')
]