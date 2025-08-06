from django.shortcuts import render
from .models import Contact, Career, Card, Wedding, BirthDay, Corporate
from django.shortcuts import redirect



# Create your views here.
def home(request):
    card = Card.objects.all()
    data = {
        'card':card,
    }
    return render(request, 'webpage/home.html')

def aboutus(request):
    return render(request, 'webpage/aboutus.html')

def wedding(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        wedding = Wedding(firstname=firstname, lastname=lastname, phone=phone, email= email, date=date)
        wedding.save()
        return redirect('home')
    else:
        return render(request, "webpage/wedding.html")



def birth_day(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        birth_day = BirthDay(name=name, phone=phone,email= email,message=message)
        birth_day.save()
        return redirect('home')
    
    return render(request, "webpage/birth_day.html")

 
def conference(request):
    return render(request, "webpage/conference.html")

def corporate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        corporate = Corporate(name=name, phone=phone,email= email,message=message)
        corporate.save()
        return redirect('home')
    
    return render(request, "webpage/birth_day.html")
    return render(request, "webpage/corporate.html")

def our_work(request):
    return render(request, "webpage/our_work.html")

def team(request):
    return render(request, "webpage/team.html")

def special_events(request):
    return render(request, "webpage/special_events.html")

def career(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        file = request.POST.get('file')
        message = request.POST.get('message')
  
        career = Career(name=name, email= email, file=file, message=message)
        career.save()
        return redirect('home')
    return render(request, 'webpage/career.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
  
        contact = Contact(name=name, address=address, email= email, phone=phone, subject=subject, message=message)
        contact.save()
        return redirect('home')
    return render(request, 'webpage/contact.html')



