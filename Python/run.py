from clientUDP import ClientUDP

# Send UDP packets to localhost, port 52733 (make sure is the same as the server).
c = ClientUDP("127.0.0.1" , 52733)
c.connect()

# As a test send 1…100 to the server (make sure the C# server is running).
i = 1
while(i<=100):
    c.sendMessage(i)
    i = i+1
input("Press any key to disconnect.")
c.disconnect()