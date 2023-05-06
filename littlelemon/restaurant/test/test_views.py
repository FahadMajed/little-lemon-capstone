from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from restaurant.models import MenuItem
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model

        self.menu1 = MenuItem.objects.create(
            title='item 1', price=10, inventory=100)
        self.menu2 = MenuItem.objects.create(
            title='item 2', price=20, inventory=100)
        self.menu3 = MenuItem.objects.create(
            title='item 3', price=30,  inventory=100)
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # Authenticate the test client
        self.client.login(username='testuser', password='testpassword')

    def test_getall(self):
        # Retrieve all the Menu objects added for test purpose
        response = self.client.get(reverse('menu-items'))

        # Serialize the retrieved Menu objects
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Check if the serialized data equals the response

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
