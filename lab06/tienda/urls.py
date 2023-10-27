from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    #Tarea lab 8
    path('',views.IndexView.as_view(),name='index'), 

    path('producto',views.ProductoView.as_view(),name='productos'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),

    path('categoria',views.CategoriaView.as_view(),name='categorias'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),

    #Lab anterior
    #path('', views.index, name='index'),
    #path('producto/<int:producto_id>/', views.producto, name='producto'),
    #path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
]