from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        """Set up test user and sample task"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.api_authentication()

        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            completed=False,
            user=self.user,
        )

    def api_authentication(self):
        """Authenticate using JWT token"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_tasks(self):
        """Test retrieving tasks for authenticated user"""
        response = self.client.get("/api/tasks/")
        print("Get Tasks Response:", response.data)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Task")

    def test_create_task(self):
        """Test creating a new task"""
        data = {"title": "New Task", "description": "New Description", "completed": False}
        response = self.client.post("/api/tasks/", data, format='json')
        
        print("Create Task Response:", response.data)  # Debugging line
        
        # Check that the task was created and status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        """Test updating an existing task"""
        data = {"title": "Updated Task", "description": "Updated Description", "completed": True}
        response = self.client.put(
            f"/api/tasks/{self.task.id}/",
            data,
            format='json',  # Ensure proper content type
        )
        
        print("Update Task Response:", response.data)  # Debugging line
        
        # Check that the update was successful and status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        """Test deleting a task"""
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_access_restricted(self):
        """Test that a user cannot access another user's tasks"""
        new_user = User.objects.create_user(username="newuser", password="newpassword")
        self.client.force_authenticate(user=new_user)
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
