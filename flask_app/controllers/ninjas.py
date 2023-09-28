from flask import render_template,redirect,request,session

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def index():
    ninjas = Ninja.show_ninjas()
    dojos = Dojo.show_all()
    return render_template('/ninjas.html', ninjas = ninjas, dojos= dojos )

@app.route('/create')
def ninja_added():
    data = {
        "dojos_id" = request.form['dojo_id']
    }
    return 0