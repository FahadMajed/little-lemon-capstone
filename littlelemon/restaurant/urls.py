# define URL route for index() view

from django.urls import include, path

from rest_framework import routers

from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('category/', views.CategoryView.as_view()),
    path('cart/', views.CartMenuItemView.as_view()),
    path('orders/', views.OrderItemView.as_view()),
    path('orders/<int:orderId>/', views.SingleOrderItemView.as_view()),
    path('groups/manager/users/', views.GroupUserView.as_view()),
    path('groups/manager/users/<int:userId>/',
         views.SingleGroupUserView.as_view())
]
