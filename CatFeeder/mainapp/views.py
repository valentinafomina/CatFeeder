from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime

from .models import Cat, Meals, Medication
from .forms import MealsEntryForm, ManualTimeEntryForm, ManualMedTime


def index(request):

    pulm = Medication.objects.latest('entryTime').entryTime.strftime("%H:%M")
    v_meals, f_meals = Meals.get_latest_meals(6)

    context = {'v_meals': v_meals,
               'f_meals': f_meals,
               'pulmicort': pulm}

    if request.method == "POST":

        form1 = MealsEntryForm(request.POST, prefix='fin')
        form2 = MealsEntryForm(request.POST, prefix='vin')

        if form1.is_valid():
            meal1 = form1.save(commit=False)
            meal1.catId = Cat(id=1)
            meal1.entryTime = datetime.now()
            meal1.save()
            context['form1'] = form1

        if form2.is_valid():
            meal2 = form2.save(commit=False)
            meal2.catId = Cat(id=2)
            meal2.entryTime = datetime.now()
            meal2.save()
            context['form2'] = form2

        if 'med' in request.POST:
            med = Medication(catId=Cat(id=2), entryTime=datetime.now())
            med.save()
            context['med'] = med

        return HttpResponseRedirect('/')

    else:
        form1 = MealsEntryForm(prefix='fin')
        form2 = MealsEntryForm(prefix='vin')
        med = Medication()
        context['form1'] = form1
        context['form2'] = form2
        context['med'] = med
    return render(request, 'mainapp/index.html', context)


def manual_time(request):
    context = {}

    if request.method == "POST":

        manual_form1 = ManualTimeEntryForm(request.POST, prefix='fin')
        manual_form2 = ManualTimeEntryForm(request.POST, prefix='vin')
        medform = ManualMedTime(request.POST)

        if manual_form1.is_valid():
            meal1 = manual_form1.save(commit=False)
            meal1.catId = Cat(id=1)
            # meal1.entryTime = datetime.now()
            meal1.save()
            context['manual_form1'] = manual_form1

        if manual_form2.is_valid():
            meal2 = manual_form2.save(commit=False)
            meal2.catId = Cat(id=2)
            # meal2.entryTime = datetime.now()
            meal2.save()
            context['manual_form2'] = manual_form2

        if medform.is_valid():
            med = medform.save(commit=False)
            med.catId = Cat(id=2)
            med.save()
            context['medform'] = medform

        return HttpResponseRedirect('/')

    else:
        manual_form1 = ManualTimeEntryForm(prefix='fin')
        manual_form2 = ManualTimeEntryForm(prefix='vin')
        medform = ManualMedTime()
        context['manual_form1'] = manual_form1
        context['manual_form2'] = manual_form2
        context['medform'] = medform
    return render(request, 'mainapp/manual_time.html', context)