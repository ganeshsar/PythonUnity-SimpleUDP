// Just copy the ServerUDP script into your unity project.
// Then use it like below. 
// Run on a new thread if you don't want to block the main one.

ServerUDP server = new ServerUDP("127.0.0.1",52733);
server.Connect();
server.StartListening();