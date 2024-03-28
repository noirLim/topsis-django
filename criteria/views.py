from django.shortcuts import redirect, render,get_object_or_404
from .forms import CriteriaForm,AlternativeForm
from .models import Criteria,Alternative
from django.core.paginator import Paginator,EmptyPage

# Create your views here.

# criteria function
# index page criteria
def index_criteria(request):
    form = CriteriaForm()
    context = {"form":form}
    return render(request,"criteria_input.html",context)

# input / update criteria
def submit_criteria_form(request,criteria_id=None):
    if criteria_id:
        criteria = get_object_or_404(Criteria,pk=criteria_id)
        if request.method == "POST":
            form = CriteriaForm(request.POST,instance=criteria)
            # check if form is valid
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                form = CriteriaForm(request.POST,instance=criteria)

    else:
        if request.method == "POST":
            form = CriteriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                form = CriteriaForm()
   
    return render(request,'index.html')

# get all criteria record
def get_all_criteria(request):
    data = Criteria.objects.all().order_by('id')
    custom_labels = {
            'code':"Criteria Id",
            'name':"Criteria Name",
            'attribute':"Attribute",
            'weight':"Weight"
    }

    return render(request,"criteria_list.html",{"data":data,"custom_labels":custom_labels})

# get criteria by id
def get_criteria_by_id(request,criteria_id):
    item = get_object_or_404(Criteria,pk=criteria_id)
    form = CriteriaForm(instance=item)
    return render(request,"criteria_input.html",{"item":item,"form":form})

# delete criteria by id
def delete_criteria_by_id(request,criteria_id):
    item = get_object_or_404(Criteria,pk=criteria_id)
    item.delete()

    return render(request,"index.html")

# alternative section
def index_alternative(request):
    form = AlternativeForm()
    context = {"form":form}
    return render(request,"alternative_input.html",context)

# input /edit alternative
def submit_alternative_form(request,alt_id=None):
    if alt_id:
        alternative = get_object_or_404(Alternative,pk=alt_id)
        if request.method == "POST":
            form = AlternativeForm(request.POST,instance=alternative)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                form = AlternativeForm(instance=alternative)
    else:
        if request.method == "POST":
            form = AlternativeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                form = AlternativeForm()

# get all alternative list
def get_all_alternative(request):
    data = Alternative.objects.select_related("students","criteria").all()
    data_list = list(
        data.values(
            'id',
            'value',
            'student__id',
            'student__name',
            'criteria__id',
            'criteria__name'
        )
    )
    # print(data_list)
    p = Paginator(data_list,4)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    custom_labels = {
        'value':"Value",
        "criteria":"Criteria",
        "student":"Student"
    }

    return render(request,"alternative_list.html",{"data":page,"custom_labels":custom_labels})

# get alternative by id
def get_alternative_by_id(request,alt_id):
    item = get_object_or_404(Alternative,pk=alt_id)
    form = AlternativeForm(instance=item)
    return render(request,"alternative_input.html",{"item":item,"form":form})

def delete_alternative_by_id(request,alt_id):
    item = get_object_or_404(Alternative,pk=alt_id)
    item.delete()
    
    return render(request,"index.html")

