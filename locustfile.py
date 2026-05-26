from locust import HttpUser, task, between

class CrudBackendUser(HttpUser):
    # Wait time between simulated user actions
    wait_time = between(1, 3)

    @task
    def get_items(self):
        # This endpoint has a simulated 1-second delay
        self.client.get("/api/items")

    @task(3) # Higher weight, runs more often if we want, but let's keep GET mostly
    def get_items_weighted(self):
        self.client.get("/api/items")
