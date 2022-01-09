# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CatFeeder.settings")
#
# import django
# django.setup()
#
# from models import Meals, Medication
#
# Meals.objects.all().delete()
# Medication.objects.all().delete()

from django.db import connection
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE `Meals`")
