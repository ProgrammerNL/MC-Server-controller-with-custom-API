from flask import Flask, jsonify
from mcstatus import JavaServer

server = JavaServer.lookup("localhost:25565")

status = server.status()

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, this is your API!")

@app.route('/api/getplayercount', methods=['GET'])
def get_player_count():
    return jsonify(message=f"The server has {status.players.online} online at the moment.")

@app.route('/')
def senderror():
    return jsonify(message="An error occured: do /(thethingthatyouwanttoknow)")
    
if __name__ == '__main__':
    app.run(debug=True)
