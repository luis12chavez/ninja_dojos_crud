from flask import render_template,redirect,request,session

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def index():
    ninjas = Ninja.show_ninjas()
    dojos = Dojo.dojos_available()
    return render_template('/ninjas.html', ninjas = ninjas, dojos= dojos )

@app.route('/create', methods = ['POST'])
def ninja_added():
    if not Ninja.validate_ninja(request.form):
        return redirect('/ninjas')
    
    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }
    print("Dojo id value:")
    print(request.form["dojo_id"])
    Ninja.create_ninja(data)
    return  redirect('/dojos')