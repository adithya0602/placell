from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("profilestud",views.profilestud,name="profilestud"),
    path("main",views.main,name="main"),
    path("main1",views.main1,name="main1"),
    path("student_login",views.student_login,name="student_login"),
    path("recruiter_login",views.recruiter_login,name="recruiter_login"),
    path("contact",views.contact,name="contact"),
    path("contactus",views.contactus,name="contactus"),
    path("placed",views.placed,name="placed"),
    path("recruiter_register",views.recruiter,name="Recruiter_register"),
    path("student_register",views.student,name="student_register"),
    path("companies_visited",views.companies_visited,name="companies_visted"),
]

