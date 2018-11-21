from itemsApp.models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
	UserCreateSerializer,
	ItemListSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
