people_in_the_commute = int(input("¿Cuántas personas viajarán en el auto? "))
distance_of_each_passenger_to_destination = []

for index in range(people_in_the_commute):
    distance_of_each_passenger_to_destination.append(
        int(
            input(
                "¿Cuál será la distancia recorrida (km)? "
                if index == 0
                else f"¿A qué distancia está el pasajero N° {index} del destino? "
            )
        )
    )

# the distance between each of the pickup points
length_of_all_segments = []

for index, length_of_segment in enumerate(distance_of_each_passenger_to_destination):
    value_to_subtract = 0

    if index + 1 < len(distance_of_each_passenger_to_destination):
        value_to_subtract = distance_of_each_passenger_to_destination[index + 1]

    length_of_all_segments.append(length_of_segment - value_to_subtract)

# the first value in the list is the distance traveled by the driver, therefore the total distance
total_distance = distance_of_each_passenger_to_destination[0]

percentage_each_segment_is_of_total_distance = []

for length_of_segment in length_of_all_segments:
    percentage_each_segment_is_of_total_distance.append(
        length_of_segment / total_distance
    )

percentage_each_person_pays_per_segment = []

for index in range(people_in_the_commute):
    people_in_the_car = index + 1

    # we get the inverse of the ammount of people in the car
    percentage_each_person_pays_per_segment.append(pow(people_in_the_car, -1))

total_percentage_each_pays = []

for index in range(people_in_the_commute):
    percentage_sum = 0

    index_of_next_element = index
    while index_of_next_element < len(range(people_in_the_commute)):
        percentage_sum += (
            percentage_each_segment_is_of_total_distance[index_of_next_element]
            * percentage_each_person_pays_per_segment[index_of_next_element]
        )

        index_of_next_element += 1

    print(
        f"El conductor debe pagar {percentage_sum * 100}% del total."
        if index == 0
        else f"El pasajero N° {index + 1} debe pagar {percentage_sum * 100}% del total."
    )
