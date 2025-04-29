from xmlrpc.server import SimpleXMLRPCServer
import threading
import logging

# Configure logging
logging.basicConfig(filename="rpc_server.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to compute factorial iteratively
def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer")
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        logging.info(f"Computed factorial({n}) = {result}")
        return result
    except Exception as e:
        logging.error(f"Error computing factorial({n}): {str(e)}")
        return str(e)

# Function to run the server
def start_server():
    with SimpleXMLRPCServer(("localhost", 8000), allow_none=True) as server:
        server.register_function(factorial, "factorial")
        print("RPC Server is running on port 8000...")
        server.serve_forever()

# Run the server in a separate thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Keep the script running
while True:
    pass
