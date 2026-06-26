port = "8080"

# converts to int
port = int(port)

if 1 <=port <= 65535:
    print("Valid port number")
else:
    print("Invalid port number")