from flask import Flask, jsonify
from mcstatus import JavaServer

server = JavaServer.lookup("localhost:25565")

status = server.status()
print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, this is your API!")

@app.route('/', methods=['GET'])
def get_player_count():
    return jsonify(message=f"The server has {status.players.online} online at the moment.")


if __name__ == '__main__':
    app.run(debug=True)
