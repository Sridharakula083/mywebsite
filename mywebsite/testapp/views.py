from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from testapp.forms import WebsiteForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    projects_show=[
        {"title":"Bitcoin Price Prediction",
         "path":"images/bitcoinpic.png"},

        {"title": "Basic Employee attendance list",
         "path": "images/employeelist.jpg"},

        {"title": "Share your Blog",
         "path": "images/blogu.png"},

        {"title": "Authentication with Django",
         "path": "images/auth.png"},

        {"title": "TODO Webpage",
         "path": "images/todo.png"},

        {"title": "Insurance Premium Prediction",
         "path": "images/insurance.png"}

    ]
    return render(request,'projects.html',{"projects_show":projects_show})

def achievements(request):
    achievements_show=[
        {"title":"TCS iON Career Edge Young Professional",
         "path":"images/tcs.jpg"},

        {"title": "Technology Virtual ExperienceProgram",
         "path": "images/deloitte.jpg"},

        {"title": "Data Analytics & Visualization Virtual Experience",
         "path": "images/accenture.jpg"},

        {"title": "Data Visualization",
         "path": "images/tata.jpg"},

        {"title": "Machine Learning Intern",
         "path": "images/intern.jpg"}

    ]
    return render(request,'achievements.html',{"achievements_show":achievements_show})

def contact(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form = WebsiteForm()
    return render(request,'contact.html',{'form':form})

def resume(request):
    resume_path = "myapp/AKULA SRIDHAR.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="AKULA SRIDHAR.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)

