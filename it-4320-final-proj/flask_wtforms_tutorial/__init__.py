"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
    app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

    @app.context_processor
    def getReservations():
        seatingChart = (["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],
        ["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"])
        takenSeats = []
        f = open("reservations.txt", "r")
        for line in f:
            seat = [int(line.split(",")[1]), int(line.split(",")[2])]
            takenSeats.append(seat)
        f.close()
        for seat in takenSeats:
            row = seat[0]
            s = seat[1]
            print("row: " + str(row))
            print("s: " + str(s))
            seatingChart[row][s] = "X"

       #print(takenSeats)
        return dict(seats=seatingChart)

    app.jinja_env.globals.update(getReservations=getReservations)

    def get_cost_matrix():
            cost_matrix = [[100, 75, 50, 100] for row in range(12)]
            return cost_matrix

    @app.context_processor
    def total_cost():
        seat_numbers =[]
        row_numbers = []
        counter = 0
        f = open("reservations.txt","r")
        lines = f.readlines()
        for line in lines:
            row = int(line.split(",")[1])
            seat = int(line.split(",")[2])
            row_numbers.append(row)
            seat_numbers.append(seat)
        prices = get_cost_matrix()
        for row,seat in zip(row_numbers,seat_numbers):
            for price in prices:
                counter = counter + prices[row][seat]
        counter = counter / 12
        return dict(total=counter)

    app.jinja_env.globals.update(total_cost=total_cost)




    # @app.context_processor
    # def authenticate(uname, pword):
        
    #     auth = open("passcodes.txt", "r")
    #     for user in auth:
    #         user, passw = user.split(',')[0], user.split(',')[1]
    #         if user == uname and passw == pword:
    #             allow = True
    #         else:
    #             allow = False
    #         return dict(allow=allow)

    # app.jinja_env.globals.update(authenticate=authenticate)

    # @app.context_processor
    # def utility_processor():
    #     def addReservation():
    #         print("BITCH!")
    #     return dict(addReservation=addReservation)
    
    # app.jinja_env.globals.update(addReservation=addReservation)

            # line = fname + "," + row + "," + seat

            # f = open("reservations.txt", "a")
            # f.write(line)
            # f.close()

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes

        return app


