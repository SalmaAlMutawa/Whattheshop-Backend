from django.urls import path
from .views import (
	UserCreateAPIView,
	ItemListAPIView,
	ItemDetailAPIView,
	UserLoginAPIView,
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('list/', ItemListAPIView.as_view(), name='list'),
    path('<int:item_id>/detail/', ItemDetailAPIView.as_view(), name='detail'),
]
