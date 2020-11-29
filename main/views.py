from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'form_submission': "Form Submission"
    }
    return render(request, 'index.html', context)

def process(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    email = request.POST['email']
    
    print(f"The user submitted was: {first_name} {last_name},{age} and their email was {email}")

    return redirect(f'/{first_name}/{last_name}/{age}/{email}')

def results(request, first_name, last_name, age, email):
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'email': email,
    }
    return render(request,"index2.html",context)


# Create your views here.
