from flask import Flask

command = "echo started"

app = Flask()

@app.route("/")
def getcommand():
    return command

@app.route("/set/<path:path>")
def setcommand(path):
    global command
    command = path
    return command

app.run(debug=False, port=8000)
