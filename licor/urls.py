from django.urls import path
from .views import *
from .views import index

urlpatterns=[
    path('api/producto',Producto_APIView.as_view()),
    path('index/',index),
    
]