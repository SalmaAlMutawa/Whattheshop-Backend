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
	ItemDetailSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class ItemDetailAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
