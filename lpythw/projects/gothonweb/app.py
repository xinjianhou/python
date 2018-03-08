from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)


@app.route('/')
def index():
    # This is used to 'setup' the session with starting value
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))


@app.route("/hello")
def hello_world():
    greet = request.args.get('greet', 'Hello')

    name = request.args.get('name', 'Nobody')

    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"

    return render_template('index.html', greeting=greeting)


@app.route("/greet", methods=['POST', 'GET'])
def greet():
    greeting = 'Hello World'

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


@app.route("/game", methods=['POST', 'GET'])
def game():
    room_name = session.get('room_name')

    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here
            return render_template("you_died.html")
    else:
        action = request.form.get('action')
        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
        return redirect(url_for("game"))


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()
