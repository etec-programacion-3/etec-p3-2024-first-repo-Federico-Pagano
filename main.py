from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return "holamundo"

@app.route("/chau")
def goodbye():
    return "chau"

app.run()