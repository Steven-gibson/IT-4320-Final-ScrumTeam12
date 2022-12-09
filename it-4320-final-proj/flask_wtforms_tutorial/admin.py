
admin = input('passwords.txt')

with open(admin, 'w', encoding='utf-8') as f:
    f.write(input('Reservations.txt'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminLoginForm()

    return render_template("reservations.html", form=form, template="form-template", err=err)