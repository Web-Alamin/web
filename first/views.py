from django import forms
from django.http import request
from django.shortcuts import render
from .models import Student

from first import forms

# Create your views here.
def index(request):
    student_list= Student.objects.order_by("first_name")
    diction = {"title":"index", "student_list":student_list}
    return render(request,"index.html", context=diction)


def student_form(request):
    form= forms.Studentform
    if request.method=="POST":
        form= forms.Studentform(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
    diction = {"title":"studen_form","student_form":form}        
    return render(request,"student-form.html", context=diction)

def student_info(request,student_id):
    student_info=Student.objects.get(pk=student_id)
    diction= {"student_info":student_info}
    return render(request, "student_info.html", context= diction)

def student_update(request,student_id):
    student_info=Student.objects.get(pk=student_id)
    form = forms.Studentform(instance=student_info)

    if request.method=="POST":
        form = forms.Studentform(request.POST,instance=student_info)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
    diction= {"student_form":form}
    return render(request, "student_update.html", context= diction) 

def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction= {"delete_massage": "Delete Done"}
    return render(request, "student_delet.html", context= diction)    