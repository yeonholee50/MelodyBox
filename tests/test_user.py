import unittest
from unittest.mock import patch
from app import app

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    @patch('controllers.user_controller.users_collection.find_one')
    def test_login(self, mock_find_one):
        mock_find_one.return_value = {'_id': 'test_user_id', 'email': 'test@test.com', 'password': 'test_password'}
        
        response = self.app.post('/login', json={'email': 'test@test.com', 'password': 'test_password'})
        
        self.assertEqual(response.status_code, 200)
    
    @patch('controllers.user_controller.users_collection.find_one')
    def test_login_invalid_credentials(self, mock_find_one):
        mock_find_one.return_value = None
        
        response = self.app.post('/login', json={'email': 'test@test.com', 'password': 'wrong_password'}) 
        self.assertEqual(response.status_code, 401)
    
    @patch('controllers.user_controller.users_collection.delete_one')
    def test_logout(self, mock_delete_one):
        mock_delete_one.return_value = MagicMock(deleted_count=1)
        
        response = self.app.post('/logout')
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
