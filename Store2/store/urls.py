from django.urls import path
from .import views
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register("products", views.ProductViewSet)
routers.register("collections", views.CollectionViewSet)
# routers.urls

urlpatterns = routers.urls


# urlpatterns = [
#      path('products/', views.ProductList.as_view()),
#      path('products/<int:pk>/', views.ProductDetail.as_view()),

#      path('collections/', views.CollectionList.as_view()),
#      path('collections/<int:pk>/', views.CollectionDetail.as_view()),




# ]