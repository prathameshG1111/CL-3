import xmlrpc.client

# Connect to the RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

def main():
    while True:
        try:
            num = int(input("\nEnter a non-negative integer to compute factorial: "))
            result = proxy.factorial(num)
            print(f"✅ Factorial of {num} is: {result}")
        except Exception as e:
            print(f"Error communicating with server: {e}")

        # Ask the user if they want to continue
        choice = input("\nDo you want to enter another number? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
