import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from reviews.models import Category, Genre, Title

class Command(BaseCommand):
    help = 'Import data from csv'

    def handle(self, *args, **kwargs):
        #Category.objects.all().delete()
        file_models = [
            ("category.csv", Category),
            ("genre.csv", Genre),
            ("titles.csv", Title),
        ]

        for file_name, model in file_models:
            import_from_file(os.path.join(settings.DATA_DIR, file_name), model)  
 

def import_from_file(file_name, model):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        field_names = next(csv_reader)
        for i, field_name in enumerate(field_names):
            if model._meta.get_field(field_name).is_relation and not field_name.endswith("_id"):
                field_names[i] += "_id"

        for row in csv_reader:
            a = {field: row[i] for i,field in enumerate(field_names)}
            _, created = model.objects.get_or_create(**a) 
