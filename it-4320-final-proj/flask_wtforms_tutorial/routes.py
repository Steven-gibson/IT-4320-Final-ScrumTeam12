from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .logic import *

#@app.route("/", methods=['GET', 'POST'])

loggedIn = False

@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()
    err = None
    loggedIn = False
    if len(request.form) > 0:
        loggedIn = authenticate(request.form['username'], request.form['password'])
        
        if loggedIn:
            toggleLoggedIn(True)
            return redirect('/reservations')
        else:
            err = "That is the wrong username/password combination."

    return render_template("admin.html", form=form, template="form-template", err=err, loggedIn=loggedIn)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    form = ReservationForm()
    err = None
    if len(request.form) > 0:
        if(checkForm(request.form['seat'], request.form['row'])):
            addReservation(request.form['seat'], request.form['row'], request.form['first_name'])
            err = None
        else:
            err = "That seat is taken."

    rule = request.url_rule
    print(rule.rule)
    if "reservations" in rule.rule:
        return render_template("reservations.html", form=form, template="form-template", err=err, loggedIn=True)
    return render_template("reservations.html", form=form, template="form-template", err=err, loggedIn=False)

