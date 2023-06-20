from django.urls import path
from .import views

urlpatterns = [
     path('products/', views.ProductList.as_view()),
     path('products/<int:id>/', views.ProductDetail.as_view()),
     # path('collections/', views.CollectionList.as_view(),name = "collection-detail"),

     path('collections/<int:pk>/', views.collection_detail,name = "collection-detail"),
     # path('collections/', views.collection_list),
     path('collections/', views.CollectionList.as_view()),



]