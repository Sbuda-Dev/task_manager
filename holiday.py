# Write a program that will calculate a user's holiday costs

cities = {"Johannesburg": 2199.99, "Durban": 5250, "Cape Town": 8500, "Port Elizabeth": 4250,
          "Rustenburg": 3600, "Polokwane": 2200, "Nelspruit": 1500}

print('''Cities:\n
    1. Johannesburg
    2. Durban
    3. Cape Town
    4. Port Elizabeth
    5. Rustenburg
    6. Polokwane
    7. Nelspruit\n''')
    

def hotel_cost (num_nights):
    total = 3400 * num_nights
    return total

def plane_cost (city_flight):
    if city_flight == 1:
        plane_price = float(cities["Johannesburg"])
        return plane_price


    elif city_flight == 2:
        plane_price = float(cities["Durban"])
        return plane_price

    elif city_flight == 3:
        plane_price = float(cities["Cape Town"])
        return plane_price

    elif city_flight == 4:
        plane_price = float(cities["Port Elizabeth"])
        return plane_price
    
    elif city_flight == 5:
        plane_price = float(cities["Rustenburg"])
        return plane_price

    elif city_flight == 6:
        plane_price = float(cities["Polokwane"])
        return plane_price

    elif city_flight == 7:
        plane_price = float(cities["Nelspruit"])
        return plane_price

    else:
        print("Incorrect option selected.")

def car_rental(rental_days):
    car_rent = rental_days * 1250
    return car_rent

def holiday_cost (hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + float(plane_cost) + car_rental
    return total_cost

city_flight = int(input("Please select city you wish to visit (Enter number 1 - 7): "))
num_nights = int(input("Please enter number nights you'll be spending: "))
rental_days = int(input("Enter number of days you'll be hiring the car: "))

hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)
total_cost = holiday_cost(hotel, plane, car)
print(f"""Holiday: \nPlane will be: R{plane} \nHotel for {num_nights} nights will be: R{hotel}
Car rental for {rental_days} days will be R{car}. \nTotal holiday cost: R{total_cost}""")

        



