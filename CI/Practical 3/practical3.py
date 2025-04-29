import random
import threading
import time

class ClientRequest:
    """Represents a client request with a unique ID and processing time."""
    def __init__(self, request_id):
        self.request_id = request_id
        self.arrival_time = time.time()
        self.processing_time = random.uniform(1, 3)  # Random processing time (1-3 sec)

class Server:
    """Represents a server handling requests."""
    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight
        self.total_requests_handled = 0

    def handle_request(self, request):
        """Simulate handling a request."""
        self.total_requests_handled += 1
        print(f"🔹 Server {self.name} handling request {request.request_id}")
        time.sleep(request.processing_time)  # Simulate processing
        print(f"✅ Server {self.name} completed request {request.request_id}")

class WeightedRoundRobinLoadBalancer:
    """Load Balancer that uses Weighted Round Robin strategy."""
    def __init__(self, servers):
        self.servers = servers
        self.lock = threading.Lock()
        self.total_requests = 0

        # Build weighted server list
        self.weighted_servers = []
        for server in servers:
            self.weighted_servers.extend([server] * server.weight)

    def distribute_request(self, request):
        """Assign a request to a server based on Weighted Round Robin."""
        with self.lock:
            server = random.choice(self.weighted_servers)

        # Process request in a new thread
        threading.Thread(target=server.handle_request, args=(request,)).start()
        self.total_requests += 1

def simulate_client_requests(load_balancer, num_requests):
    """Generates and distributes client requests."""
    for i in range(num_requests):
        request = ClientRequest(i+1)
        threading.Thread(target=load_balancer.distribute_request, args=(request,)).start()
        time.sleep(random.uniform(0.5, 1.5))  # Random inter-arrival time

# Create servers with different weights
server_list = [Server("S1", weight=2), Server("S2", weight=1), Server("S3", weight=3)]

# Create Load Balancer (Weighted Round Robin only)
load_balancer = WeightedRoundRobinLoadBalancer(server_list)

# Run the simulation for 10 client requests
simulate_client_requests(load_balancer, 10)

# Wait for all requests to finish
time.sleep(10)

# Print statistics
print("\n📊 Load Balancing Summary:")
print(f"🔹 Total Requests Processed: {load_balancer.total_requests}")
for server in server_list:
    print(f"✅ {server.name}: {server.total_requests_handled} requests handled")
