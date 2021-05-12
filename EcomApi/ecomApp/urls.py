from django.contrib import admin
from django.urls import path
from ecomApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category',views.ListCategory.as_view()),
    path('detcat/<int:pk>',views.DetailCategory.as_view()),

    path('product',views.ListProduct.as_view()),
    path('detpro/<int:pk>',views.DetailProduct.as_view()),

    path('books',views.ListBook.as_view()),
    path('detbook/<int:pk>',views.DetailBook.as_view())
]
