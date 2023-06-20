from django.shortcuts import HttpResponse,get_object_or_404
from django.db.models.aggregates import Count
# from django.db import Count 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import status
from .serializer import ProductSerializer,CollectionSerializer
from store.models import Product,Collection,OrderItem

# Create your views here.

class ProductList(ListCreateAPIView):
          queryset = Product.objects.select_related('collection').all()
          serializer_class = ProductSerializer
          def get_serializer_context(self):
               return  {'request':self.request}


class ProductDetail(RetrieveDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     def delete(self,request,pk):
          product = get_object_or_404(Product,pk=pk)
          if product.orderitems.count()> 0:
               return Response({"error":"Product can not be deleted"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
          product.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
     queryset = Collection.objects.annotate(products_count=Count('products')).all()
     serializer_class = CollectionSerializer
     

class CollectionDetail(RetrieveDestroyAPIView):
     queryset  = Collection.objects.annotate(products_count=Count('products')).all()
     serializer_class = CollectionSerializer
     def delete(self, request,pk):
          collection = get_object_or_404(Collection,pk=pk)
          if collection.products.count()> 0:
               return Response({"error":"Product can not be deleted"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
          collection.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
          