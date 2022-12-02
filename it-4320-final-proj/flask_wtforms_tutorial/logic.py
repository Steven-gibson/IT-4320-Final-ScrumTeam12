#from jinja2 import Environment, FileSystemLoader

def getReservations():
    takenSeats = []
    f = open("reservations.txt", "r")
    for line in f:
        seat = [line.split(",")[1], line.split(",")[2]]
        takenSeats.append(seat)
    f.close()
    print(takenSeats)
    return takenSeats

def addReservation(seat, row, fname):
    print("BITCH!")

    line = fname + "," + row + "," + seat + "\n"
    print(line)
    f = open("reservations.txt", "a")
    f.write(line)
    f.close()

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
