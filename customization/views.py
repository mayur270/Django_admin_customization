from django.shortcuts import render
from django.views.generic import FormView
from .forms import CoffeeForm
from .models import coffee_file, coffee
from django.contrib.auth.models import User
import csv

# Create your views here.
def home(request):
    form = CoffeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=CoffeeForm()
        obj=coffee_file.objects.get(activated=False)
        with open(obj.csv_file.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    name =row[0]
                    price = row[1]
                    description = row[2]
                    coffee.objects.create(
                    name=name,
                    price=price,
                    description=description
                    )
            obj.activated = True
            obj.save()
    return render(request, 'home.html', {'form':form})
