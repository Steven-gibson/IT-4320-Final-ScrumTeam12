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
            row = seat[0] - 1
            s = seat[1] - 1
            seatingChart[row][s] = "X"

       #print(takenSeats)
        return dict(seats=seatingChart)

    app.jinja_env.globals.update(getReservations=getReservations)

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


