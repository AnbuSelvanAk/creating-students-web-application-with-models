from django.shortcuts import render
from apps.models import Student
from apps.form import StudentForm

def home(request):
	stud=Student.objects.all()
	return render(request,'appfile/home.html',{'a':stud})

def forms(request):
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)
	return render(request,'appfile/form.html',{'form':form})

def final(request):
	return render(request,'appfile/final.html')