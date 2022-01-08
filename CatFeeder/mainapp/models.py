from django.db import models
from datetime import datetime


class Cat(models.Model):
    name = models.CharField(verbose_name='имя кошки', max_length=64,
                            unique=True)


class Meals(models.Model):
    entryTime = models.DateTimeField(verbose_name='когда покормлен',
                                     default=datetime.now, blank=True)
    catId = models.ForeignKey(Cat, on_delete=models.CASCADE)
    size = models.IntegerField(verbose_name='размер порции', default=0)

    @staticmethod
    def get_latest_meals(qtty):
        meals_finik = Meals.objects.filter(catId=1).order_by('-entryTime')[:qtty]
        meals_vishenka = Meals.objects.filter(catId=2).order_by('-entryTime')[:qtty]
        latest_meal_size_v = []
        latest_meal_size_f = []
        latest_meal_time_v = []
        latest_meal_time_f = []
        for item in meals_vishenka:
            latest_meal_size_v.append(item.size)
            latest_meal_time_v.append(item.entryTime.strftime("%H:%M"))
        for item in meals_finik:
            latest_meal_size_f.append(item.size)
            latest_meal_time_f.append(item.entryTime.strftime("%H:%M"))
        v_meals = zip(latest_meal_time_v, latest_meal_size_v)
        f_meals = zip(latest_meal_time_f, latest_meal_size_f)
        return v_meals, f_meals

        # return latest_meal_size_v, latest_meal_time_v, latest_meal_size_f,\
        #        latest_meal_time_f

        # latest_meals_vishenka = {}
        # latest_meals_finik = {}
        # for item in meals_finik:
        #     latest_time = item.entryTime.strftime("%H:%M:%S")
        #     print(latest_time)
        #     latest_meals_finik[latest_time] = item.size
        # for item in meals_vishenka:
        #     latest_time = item.entryTime.strftime("%H:%M:%S")
        #     latest_meals_vishenka[latest_time] = item.size
        # return latest_meals_vishenka, latest_meals_finik


class Medication(models.Model):
    entryTime = models.DateTimeField(verbose_name='когда дали таблетку',
                                     default=datetime.now, blank=True)
    catId = models.ForeignKey(Cat, on_delete=models.CASCADE)



