from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, status

from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.models import MenuItem, Booking, Category, Cart, Order, OrderItem
from restaurant.permissions import CartPermission, CatagoryPermission, MenuItemsPermission

from django.http import HttpResponse
from restaurant.serializers import MenuItemSerializer, BookingSerializer, CategorySerializer, CartMenuItemSerializer, OrderItemSerializer, OrderSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CategoryView(generics.ListCreateAPIView):
    permission_classes = [CatagoryPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartMenuItemView(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = [CartPermission]
    # queryset= Cart.objects.all()
    serializer_class = CartMenuItemSerializer

    def get_queryset(self):
        userid = self.request.user.pk
        return Cart.objects.all().filter(user=userid)

    def destroy(self, request):
        userid = self.request.user.pk
        UserCart = Cart.objects.all().filter(user=userid)
        UserCart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrdersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        userid = self.request.user.pk
        orderid = Order.objects.all().filter(user=userid).first()
        return OrderItem.objects.all().filter(order=orderid)

    def create(self, request, *args, **kwargs):
        # your implementation
        userid = self.request.user.pk
        orderitem = Cart.objects.all().filter(user=userid)

        return Response(status=status.HTTP_201_CREATED)


class SingleOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [MenuItemsPermission]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class GroupUserView(generics.ListCreateAPIView):
    permission_classes = [MenuItemsPermission]
    queryset = User.objects.all()


class SingleGroupUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [MenuItemsPermission]
    queryset = User.objects.all()


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return HttpResponse({"message": "This view is protected"})
