from locust import HttpUser, task, between, events


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Strip trailing slash from host URL to prevent //api/items double-slash failures."""
    if environment.host and environment.host.endswith("/"):
        environment.host = environment.host.rstrip("/")
        print(f"✅ Host auto-fixed to: {environment.host}")


class CrudFastAPIUser(HttpUser):
    """
    Simulates a real user hitting the FastAPI CRUD backend.
    Wait time is randomized between 1-3 seconds between tasks (realistic behavior).
    """
    wait_time = between(1, 3)

    @task(4)
    def get_all_items(self):
        """Heavily weighted — tests Redis cache under concurrent load."""
        self.client.get("/api/items", name="GET /api/items")

    @task(2)
    def get_single_item(self):
        """Tests single item retrieval with 200ms simulated DB delay."""
        self.client.get("/api/items/1", name="GET /api/items/:id")

    @task(1)
    def create_item(self):
        """Tests POST endpoint and cache invalidation."""
        self.client.post(
            "/api/items",
            json={"name": "Load Test Item"},
            name="POST /api/items",
        )

    @task(1)
    def health_check(self):
        """Hits root endpoint to check API is alive."""
        self.client.get("/", name="GET / (health)")
