import requests
from autos.models import Car, CarModel, Brand, Category
import os
from django.conf import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MEDIA_ROOT = settings.MEDIA_ROOT

car_details = [
    {"price": 30000, "description": "A compact and fuel-efficient car perfect for city driving."},
    {"price": 35000, "description": "A robust SUV with all-terrain capabilities."},
    {"price": 27000, "description": "A stylish and economic hatchback, ideal for young professionals."},
    {"price": 45000, "description": "A luxury sedan with advanced features and a smooth ride."},
    {"price": 32000, "description": "A reliable family car with a spacious interior and modern technology."},
    {"price": 29000, "description": "A sporty coupe with a powerful engine and sleek design."},
    {"price": 33000, "description": "A hybrid vehicle offering great fuel efficiency and low emissions."},
    {"price": 28000, "description": "A compact crossover with a versatile interior and strong performance."},
    {"price": 36000, "description": "An electric vehicle with a long range and fast charging capability."},
    {"price": 25000, "description": "An entry-level sedan offering value for money and reliability."},
    {"price": 37000, "description": "A midsize SUV with advanced safety features and comfortable seating."},
    {"price": 41000, "description": "A luxury SUV with top-of-the-line features and a powerful engine."},
    {"price": 27000, "description": "A compact car with excellent fuel economy and a smooth ride."},
    {"price": 34000, "description": "A sporty sedan with a turbocharged engine and dynamic handling."},
    {"price": 29000, "description": "A family-friendly SUV with a spacious interior and modern features."},
    {"price": 33000, "description": "A compact SUV with off-road capabilities and a stylish design."},
    {"price": 31000, "description": "A reliable pickup truck with a powerful engine and large cargo space."},
    {"price": 38000, "description": "A luxury coupe with a high-performance engine and premium features."},
    {"price": 26000, "description": "A fuel-efficient sedan with a comfortable interior and smooth handling."},
    {"price": 40000, "description": "A high-performance sports car with a sleek design and advanced technology."}
]

def get_car_data():
    url = "https://www.carqueryapi.com/api/0.3/?cmd=getModels&make=chevrolet"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            return response.json()['Models']
        except requests.exceptions.JSONDecodeError:
            logger.error("Error al decodificar el JSON.")
            return None
    else:
        logger.error(f"Error al obtener datos de la API: {response.status_code}")
        return None

def populate_cars():
    Car.objects.all().delete()
    logger.info("Todos los registros de autos han sido eliminados.")

    car_data = get_car_data()
    if car_data is None:
        logger.error("No se pudo obtener datos de autos. Verifica la API.")
        return
    
    category, _ = Category.objects.get_or_create(name="General", description="General category")

    for i, car in enumerate(car_data[:20]):  
        brand, _ = Brand.objects.get_or_create(name=car['model_make_id'])
        model, _ = CarModel.objects.get_or_create(name=car['model_name'], brand=brand)

        image_path = f"cars/{i+1}.png" 
        
        car_instance = Car.objects.create(
            model=model,
            category=category,
            year=2022,
            price=car_details[i]["price"],
            image=image_path,
            description=car_details[i]["description"]
        )
        car_instance.save()
        logger.info(f"Añadido auto: {car['model_name']}")

    logger.info("Todos los autos han sido agregados exitosamente.")

populate_cars()
