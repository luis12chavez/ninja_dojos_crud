from flask import render_template,redirect,request,session

from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def show_dojos():
    dojos_students = Dojo.dojo_all_info()
    dojos = Dojo.dojos_available()
    print(dojos)
    return render_template('dojos.html', dojos_students = dojos_students, dojos = dojos)

@app.route('/dojos/create', methods = ['POST'])
def add_dojo():
    data = {
        "name" : request['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojos_id>')
def select_dojo(dojos_id):

    dojo_students = Dojo.students_per_dojo(dojos_id)
    # print(dojo_students)
    return render_template ("dojo_show.html", dojo_students = dojo_students)