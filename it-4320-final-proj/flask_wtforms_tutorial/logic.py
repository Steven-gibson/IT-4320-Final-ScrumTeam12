from jinja2 import Environment, FileSystemLoader
from flask import current_app as app


def getReservations():
    takenSeats = []
    f = open("reservations.txt", "r")
    for line in f:
        seat = [str(int(line.split(",")[1])-1), str(int(line.split(",")[2])-1)]
        takenSeats.append(seat)
    f.close()
    print(takenSeats)
    return takenSeats

def addReservation(seat, row, fname):
    eTicket = getTicket(fname)
    line = fname + "," + str(int(row)-1) + "," + str(int(seat)-1) + "," + eTicket + "\n"
    print(line)
    f = open("reservations.txt", "a")
    f.write(line)
    f.close()

def getTicket(name):
    fname = name
    base = "INFOTC4320"
    eTicket = ""
    if(len(fname) < len(base)):
        for x in range(len(fname)):
            eTicket += fname[x] + base[x]
        y = len(fname)
        for x in range(len(base)-len(fname)):
            eTicket += base[y]
            y += 1
    elif(len(fname) > len(base)):
        for x in range(len(base)):
            eTicket += fname[x] + base[x]
        y = len(base)
        for x in range(len(fname)-len(base)):
            eTicket += fname[y]
            y += 1
    else: #for lengths being equal
        for x in range(len(fname)):
            eTicket += fname[x] + base[x]
    
    return eTicket

def checkForm(seat, row):
    f = open("reservations.txt", "r")
    lines = f.readlines()
    takenSeats = []
    string = str(int(row)-1) + ',' + str(int(seat)-1)
    for line in lines:
        takenSeats.append(line.split(',')[1] +','+line.split(',')[2])
    if string in takenSeats:
            return False
    print(takenSeats)
    return True

def authenticate(uname, pword):
    auth = open("passcodes.txt", "r")
    for user in auth:
        user, passw = user.split(',')[0], user.split(',')[1]
        user, passw = user.strip(), passw.strip()
        print(user)
        print(passw)
        if user == uname and passw == pword:
            return True
        else:
            continue
        return False

# @app.context_processor
# def toggleLoggedIn(toggle=False):
#     return dict(loggedIn=toggle)
# app.jinja_env.globals.update(loggedIn=toggleLoggedIn)

    


# func_dict = {
#     "getReservations": getReservations,
#     "addReservation": addReservation,
# }

# def render(template):
#     env = Environment(loader=FileSystemLoader("/srv/templates/"))
#     jinja_template = env.get_template(template)
#     jinja_template.globals.update(func_dict)
#     template_string = jinja_template.render()
#     return template_string


# if __name__ == "__main__":
#     print(render(template="form-template"))
