from itemsApp.models import Item
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
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
    UserLoginSerializer,
    AddressCreateSerializer,
    OrderSerializer,
    MiddleManSerializer,
 )

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            print(valid_data)
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class ItemDetailAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'

class AddressCreateAPIView(CreateAPIView):
    serializer_class= AddressCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class OrderAPIView(APIView):


    def post(self,request):
        order_obj=Order.objects.create(user=request.user, address=request.user.address)

        for obj in request.data:
            serializer=MiddleManSerializer(data=obj)
            order_obj.middleman_set.add(obj)
            order_obj.save()
            print(obj)
        order_serializer = OrderSerializer(order_obj)
        return Response(order_serializer.data, status=HTTP_201_CREATED)
