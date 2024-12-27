from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework.authtoken.models import Token

class MenuViewTest(APITestCase):
    
    def setUp(self):
        # Create a user and get the token for authentication
        self.user = User.objects.create_user(username='admin', password='12345678')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a menu item
        self.menu_item = Menu.objects.create(Title="Pizza", Price=10.00, Inventory=100)

    def test_get_menus(self):
        # Test GET method to retrieve menus
        response = self.client.get('/restaurant/menus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One item created
        self.assertEqual(response.data[0]['Title'], 'Pizza')

    def test_post_menu(self):
        # Test POST method to create a new menu item
        data = {'Title': 'Burger', 'Price': 5.00, 'Inventory': 50}
        response = self.client.post('/restaurant/menus/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['Title'], 'Burger')

    def test_post_menu_invalid(self):
        # Test POST with missing data (invalid request)
        data = {'Title': 'Burger', 'Price': 5.00}  # Missing 'Inventory'
        response = self.client.post('/restaurant/menus/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)
