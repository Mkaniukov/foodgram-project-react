import csv

from django.core.management.base import BaseCommand
from api.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('api/data/ingredients.csv') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                name, unit = row
                Ingredient.objects.get_or_create(
                    name=name, measurement_unit=unit,
                )
