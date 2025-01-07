from django.urls import path
from testapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("achievements/",views.achievements,name="achievements"),
    path("contact/",views.contact,name="contact"),
    path("resume/",views.resume,name="resume")
]