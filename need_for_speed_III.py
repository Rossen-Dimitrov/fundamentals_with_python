def drive_car(cur_car, cur_distance, cur_needed_fuel):
    if cars_dict[cur_car]["FUEL"] >= cur_needed_fuel:
        cars_dict[cur_car]["FUEL"] -= cur_needed_fuel
        cars_dict[cur_car]["MILEAGE"] += cur_distance
        return f"{cur_car} driven for {cur_distance} kilometers. {cur_needed_fuel} liters of fuel consumed."
    else:
        return "Not enough fuel to make that ride"


def refuel_car(cur_car, cur_refuel):
    if cars_dict[cur_car]["FUEL"] + cur_refuel > 75:
        cur_refuel = 75 - cars_dict[cur_car]["FUEL"]
        cars_dict[cur_car]["FUEL"] = 75
    else:
        cars_dict[cur_car]["FUEL"] += cur_refuel
    print(f"{cur_car} refueled with {cur_refuel} liters")


def revert_mileage(cur_car, cur_reverted_km):
    if cars_dict[cur_car]["MILEAGE"] - cur_reverted_km > 10000:
        cars_dict[cur_car]["MILEAGE"] -= cur_reverted_km
        print(f"{cur_car} mileage decreased by {cur_reverted_km} kilometers")
    else:
        cars_dict[cur_car]["MILEAGE"] = 10000


def time_to_sell(cur_car):
    if cars_dict[cur_car]["MILEAGE"] >= 100000:
        print(f"Time to sell the {cur_car}!")
        del cars_dict[cur_car]


n = int(input())
cars_dict = {}

for i in range(n):
    car_1, mileage, fuel = input().split("|")
    cars_dict[car_1] = {"MILEAGE": int(mileage), "FUEL": int(fuel)}

data_in = input()
while not data_in == "Stop":
    data_in = data_in.split(" : ")
    command = data_in[0]
    car = data_in[1]
    if command == "Drive":
        distance = int(data_in[2])
        needed_fuel = int(data_in[3])
        print(drive_car(car, distance, needed_fuel))
        time_to_sell(car)

    elif command == "Refuel":
        refuel = int(data_in[2])
        refuel_car(car, refuel)

    elif command == "Revert":
        kilometers = int(data_in[2])
        revert_mileage(car, kilometers)

    data_in = input()

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car]['MILEAGE']} kms, Fuel in the tank: {cars_dict[car]['FUEL']} lt.")