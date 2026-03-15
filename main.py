from flask import Flask
import os

command = "echo started"
awable = 1

app = Flask(__name__)

@app.route("/")
def getcommand():
    return command

@app.route("/set/<path:path>")
def setcommand(path):
    global command
    command = path
    return command

@app.route("/awable")
def getawable():
    global awable
    if awable:
        awable = 0
    return awable

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
