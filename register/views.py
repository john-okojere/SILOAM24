from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def home(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form_data = form.save()
            print(form_data)
            return redirect('card', uid = form_data.uid)
    form = PersonForm()
    print(request.method)
    return render(request, 'register/index.html', {'form' : form})

def success(request, uid):
    person = Person.objects.get(uid=uid)
    return render(request, 'register/success.html', {'person':person})
    
def cards(request):
    persons = Person.objects.all()
    return render(request, 'card.html',{'persons':persons})