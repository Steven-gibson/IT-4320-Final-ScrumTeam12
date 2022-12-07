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

    line = fname + "," + row + "," + seat + "\n"
    print(line)
    f = open("reservations.txt", "a")
    f.write(line)
    f.close()


