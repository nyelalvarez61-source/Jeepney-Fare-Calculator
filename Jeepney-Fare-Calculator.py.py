# JEEPNEY FARE CALCULATION SYSTEM
# Route: Cogon -> Carmen -> Patag -> Apovel -> Bulua

stops = ["Cogon", "Carmen", "Patag", "Apovel", "Bulua"]

# Distance between each stop and the next stop
distances = [2.4, 7.4, 2.4, 1.6, 5.8]


# =============================
# CHOOSE A STOP
# =============================

def choose_stop():

    while True:
        for i in range(len(stops)):
            print(i + 1, ".", stops[i])

        choice = input("Choose a stop: ")

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= len(stops):
                return choice - 1

        print("Invalid choice. Please try again.")


# =============================
# GET DISTANCE
# =============================

def get_distance(start, destination):

    distance = 0
    current = start

    while current != destination:

        distance = distance + distances[current]

        current = current + 1

        if current == len(stops):
            current = 0

    return distance


# =============================
# CHOOSE PASSENGER TYPE
# =============================

def choose_passenger_type():

    while True:
        print("\n1. Regular - P12")
        print("2. Discounted (Student/Senior/PWD) - P10")

        passenger = input("Passenger type: ")

        if passenger == "1":
            return "Regular", 12

        elif passenger == "2":
            return "Discounted", 10

        else:
            print("Invalid choice. Please try again.")


# =============================
# CALCULATE FARE
# =============================

def calculate_fare():

    print("\n=== FARE CALCULATOR ===")

    # PASSENGER QUANTITY
    while True:
        quantity = input("Number of passengers: ")

        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break

        print("Please enter a valid number greater than zero.")

    # Lists to store passenger information
    passenger_types = []
    passenger_fares = []
    passenger_quantities = []

    # PASSENGER TYPE
    if quantity == 1:

        passenger_type, fare = choose_passenger_type()

        passenger_types.append(passenger_type)
        passenger_fares.append(fare)
        passenger_quantities.append(quantity)

    else:

        while True:
            print("\nAre all passengers the same type?")
            print("1. Yes")
            print("2. No")

            same_type = input("Choose: ")

            if same_type == "1":
                passenger_type, fare = choose_passenger_type()

                passenger_types.append(passenger_type)
                passenger_fares.append(fare)
                passenger_quantities.append(quantity)
                break

            elif same_type == "2":

                print("\nEnter the number of each passenger type.")

                while True:
                    regular = input("Regular passengers: ")

                    if regular.isdigit():
                        regular = int(regular)
                        break

                    print("Please enter a whole number.")

                while True:
                    discounted = input(
                        "Discounted passengers (Student/Senior/PWD): "
                    )

                    if discounted.isdigit():
                        discounted = int(discounted)
                        break

                    print("Please enter a whole number.")

                total_quantity = regular + discounted

                if total_quantity != quantity:
                    print("\nThe passenger quantities do not match.")
                    print("You entered:", total_quantity)
                    print("Expected:", quantity)
                    print("Please enter the quantities again.")
                    continue

                if regular > 0:
                    passenger_types.append("Regular")
                    passenger_fares.append(12)
                    passenger_quantities.append(regular)

                if discounted > 0:
                    passenger_types.append("Discounted")
                    passenger_fares.append(10)
                    passenger_quantities.append(discounted)

                break

            else:
                print("Invalid choice. Please try again.")

    # BOARDING POINT
    print("\n=== BOARDING POINT ===")
    start = choose_stop()

    # DESTINATION
    while True:
        print("\n=== DESTINATION ===")
        destination = choose_stop()

        if start != destination:
            break

        print("Boarding point and destination cannot be the same.")
        print("Please choose another destination.")

    # GET DISTANCE
    km = get_distance(start, destination)

    # CALCULATE DISTANCE FARE
    if km > 4:

        extra_km = km - 4
        extra_steps = int(extra_km / 4)

        if extra_km % 4 != 0:
            extra_steps = extra_steps + 1

        extra_fare = extra_steps * 2

    else:
        extra_fare = 0

    # CALCULATE TOTAL FARE
    total_fare = 0

    for i in range(len(passenger_types)):

        fare = passenger_fares[i] + extra_fare
        passenger_total = fare * passenger_quantities[i]

        total_fare = total_fare + passenger_total

    # SHOW RESULT AND FARE BREAKDOWN
    print("\n=== FARE RESULT ===")

    print("+------------------------+-----------------+")

    for i in range(len(passenger_types)):

        basic_fare = 12

        if passenger_types[i] == "Discounted":
            discount = 2
        else:
            discount = 0

        fare = basic_fare - discount + extra_fare
        passenger_total = fare * passenger_quantities[i]

        print("| Passenger Type         |",
              passenger_types[i].ljust(15), "|")

        print("| Quantity               |",
              str(passenger_quantities[i]).ljust(15), "|")

        print("| Basic Fare             |",
              ("P" + str(basic_fare)).ljust(15), "|")

        print("| Discount               |",
              ("P" + str(discount)).ljust(15), "|")

        print("| Extra Distance Charge  |",
              ("P" + str(extra_fare)).ljust(15), "|")

        print("| Fare Per Person        |",
              ("P" + str(fare)).ljust(15), "|")

        print("| Subtotal               |",
              ("P" + str(passenger_total)).ljust(15), "|")

        print("+------------------------+-----------------+")

    print("| Route                  |",
          (stops[start] + " to " + stops[destination]).ljust(15), "|")

    print("| Distance               |",
          (str(km) + " km").ljust(15), "|")

    print("| Total Fare             |",
          ("P" + str(total_fare)).ljust(15), "|")

    print("+------------------------+-----------------+")

    # PAYMENT
    while True:
        payment = input("\nPassenger payment: P")

        if payment.isdigit():
            payment = int(payment)

            if payment >= total_fare:
                change = payment - total_fare
                print("Change: P", change)
                break

            else:
                print("Not enough payment.")
                print("Short by: P", total_fare - payment)
                print("Please enter the payment again.")

        else:
            print("Please enter a whole number.")


# =============================
# VIEW ROUTE
# =============================

def view_route():

    print("\n=== ROUTE AND DISTANCES ===")

    print("+============+============+==========+")

    print("| Start      | Next Stop  | Distance |")

    print("+============+============+==========+")

    for i in range(len(stops)):

        next_stop = i + 1

        if next_stop == len(stops):
            next_stop = 0

        print("|", stops[i].ljust(10),
              "|", stops[next_stop].ljust(10),
              "|", (str(distances[i]) + " km").ljust(8), "|")

    print("+============+============+==========+")


# =============================
# MAIN MENU
# =============================

while True:

    print("\n===============================")
    print(" JEEPNEY FARE CALCULATION SYSTEM")
    print("===============================")

    print("1. Calculate Fare")
    print("2. View Route and Distances")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        calculate_fare()

    elif choice == "2":
        view_route()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
