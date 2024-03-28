from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import Students

# Create your views here.
def index_student(request):
    form = StudentForm()
    context = {"form":form}
    return render(request,"input.html",context)

def submit_student_form(request,student_id=None):
    # update student record
    if student_id:
        student = get_object_or_404(Students,pk=student_id)
        if request.method == "POST":
            form = StudentForm(request.POST,instance=student)
            if form.is_valid():
               form.save()
               return redirect('/')
        else:
            form = StudentForm(instance=student)
    # create new student record
    else:
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = StudentForm()
    

# get all student record
def get_all_students(request):
    data = Students.objects.all()
    custom_labels = {
        "code" : "Student Id",
        "name" : "Student Name"
    }

    return render(request,"list.html",{"data":data,"custom_labels":custom_labels})

# delete student by id
def delete_student_by_id(request,student_id):
     item = get_object_or_404(Students, pk=student_id)
     item.delete()

     return render(request, 'index.html')

# get student by id
def get_student_by_id(request,student_id):
    item = get_object_or_404(Students, pk=student_id)
    form = StudentForm(instance=item)
    return render(request,"input.html",{"item":item,"form":form})
