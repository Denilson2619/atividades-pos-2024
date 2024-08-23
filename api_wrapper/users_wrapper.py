import requests

class UserAPI:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com/users"

    def _request(self, method, endpoint='', json=None):
        """Helper method to handle HTTP requests."""
        url = f"{self.api_url}/{endpoint}" if endpoint else self.api_url
        try:
            response = requests.request(method, url, json=json)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def list_users(self):
        """Retrieve a list of users."""
        return self._request('GET')

    def get_user(self, user_id):
        """Retrieve a single user by ID."""
        return self._request('GET', str(user_id))

    def delete_user(self, user_id):
        """Delete a user by ID."""
        response = self._request('DELETE', str(user_id))
        return response is not None

    def create_user(self, user_data):
        """Create a new user."""
        return self._request('POST', json=user_data)

    def update_user(self, user_id, user_data):
        """Update an existing user by ID."""
        return self._request('PATCH', str(user_id), json=user_data)
