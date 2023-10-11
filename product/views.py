from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


class CategoryView(viewsets.ViewSet):
    """
    this is a simple view sets categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
