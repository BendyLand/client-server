"""  
Echo Server and Client
Project Description: An echo server simply sends back whatever data it receives from the client. This project will help you understand the basics of socket programming, how to set up a connection, and the basics of sending and receiving data over a network.
Learning Outcomes: TCP/IP basics, socket programming, handling client-server connections.
"""

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "index page!\n"

@app.route("/hello")
def hello():
    return "hello page!\n"
