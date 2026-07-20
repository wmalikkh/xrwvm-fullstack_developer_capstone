def initiate():
    from .models import CarMake, CarModel

    car_make_data = [
        {"name": "Toyota",
         "description": "Toyota Motor Corporation, a renowned automaker."},
        {"name": "Honda",
         "description": "Honda, known for reliability and innovation."},
        {"name": "Ford",
         "description": "Ford Motor Company, an American automaker."},
        {"name": "BMW",
         "description": "BMW, a German brand known for luxury vehicles."},
        {"name": "Chevrolet",
         "description": "Chevrolet, a division of General Motors."},
    ]
    car_make_instances = []
    for data in car_make_data:
        cm = CarMake.objects.get_or_create(
            name=data["name"], defaults={"description": data["description"]}
        )[0]
        car_make_instances.append(cm)

    car_model_data = [
        {"name": "Corolla", "type": "Sedan", "year": 2021, "car_make": car_make_instances[0]},
        {"name": "RAV4", "type": "SUV", "year": 2022, "car_make": car_make_instances[0]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Civic", "type": "Sedan", "year": 2021, "car_make": car_make_instances[1]},
        {"name": "CR-V", "type": "SUV", "year": 2022, "car_make": car_make_instances[1]},
        {"name": "Accord", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "Mustang", "type": "Hatchback", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "F-150", "type": "Truck", "year": 2022, "car_make": car_make_instances[2]},
        {"name": "Explorer", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "3 Series", "type": "Sedan", "year": 2021, "car_make": car_make_instances[3]},
        {"name": "X5", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "5 Series", "type": "Sedan", "year": 2022, "car_make": car_make_instances[3]},
        {"name": "Malibu", "type": "Sedan", "year": 2021, "car_make": car_make_instances[4]},
        {"name": "Equinox", "type": "SUV", "year": 2022, "car_make": car_make_instances[4]},
        {"name": "Silverado", "type": "Truck", "year": 2023, "car_make": car_make_instances[4]},
    ]
    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data["name"], car_make=data["car_make"],
            defaults={"type": data["type"], "year": data["year"]},
        )
    print("Car makes and models populated successfully.")