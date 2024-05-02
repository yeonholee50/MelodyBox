import unittest
from unittest.mock import patch, MagicMock
from app import app
from bson.objectid import ObjectId

class TestPlaylist(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    @patch('pymongo.collection.Collection.insert_one')
    def test_create_playlist(self, mock_insert_one):
        mock_insert_one.return_value = MagicMock(inserted_id=ObjectId())
        
        response_invalid_input = self.app.post('/playlists', json={'name': ''})
        self.assertEqual(response_invalid_input.status_code, 400)
        
        response_valid_input = self.app.post('/playlists', json={'name': 'Test Playlist'})
        self.assertEqual(response_valid_input.status_code, 201)
    
    @patch('pymongo.collection.Collection.update_one')
    def test_update_playlist(self, mock_update_one):
        mock_update_one.return_value = MagicMock(modified_count=1)
        
        response_non_existing = self.app.put('/playlists/non_existing_id', json={'name': 'Updated Playlist'})
        self.assertEqual(response_non_existing.status_code, 404)
        
        playlist_id = str(ObjectId())
        response_invalid_input = self.app.put(f'/playlists/{playlist_id}', json={'name': ''})
        self.assertEqual(response_invalid_input.status_code, 400)
        
        response_valid_input = self.app.put(f'/playlists/{playlist_id}', json={'name': 'Updated Playlist'})
        self.assertEqual(response_valid_input.status_code, 200)
    
    @patch('pymongo.collection.Collection.delete_one')
    def test_delete_playlist(self, mock_delete_one):
        mock_delete_one.return_value = MagicMock(deleted_count=1)
        
        response_non_existing = self.app.delete('/playlists/non_existing_id')
        self.assertEqual(response_non_existing.status_code, 404)
        
        playlist_id = str(ObjectId())
        response = self.app.delete(f'/playlists/{playlist_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

