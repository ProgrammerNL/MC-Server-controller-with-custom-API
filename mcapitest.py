from mcstatus import JavaServer

server = JavaServer("localhost", port=25565)
status = server.status()
print(status)