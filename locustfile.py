import os
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def load_test(self):
        endpoint = os.getenv('API_URL', 'default_api_url_if_not_set')
        self.client.get(f"{endpoint}BLACK%20VELVET")
