from django.shortcuts import render,redirect,get_object_or_404
from .forms import ResultForm
from .models import Result,Students,Det_Result
from criteria.models import  Criteria, Alternative
from django.http import HttpResponse
from .utils import *
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from io import BytesIO
import pandas as pd


# Create your views here.
def index_result(request):
    form = ResultForm()
    context = {"form":form}
    return render(request,"result_input.html",context)

def submit_result_form(request):
    criteria_data = list(Criteria.objects.values('id','code','name','attribute','weight').order_by('id'))

    student_data = list(Students.objects.values('id','name').order_by("id"))

    data = Alternative.objects.select_related("students","criteria").all()
    alt_data = list(
        data.values(
            'id',
            'value',
            'student__id',
            'student__name',
            'criteria__id',
            'criteria__name'
        )
    )

    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            topsis_formula = calc_topsis(alt_data,criteria_data,student_data)
            result = form.save()
            
            # save to result detail
            saved_result = get_object_or_404(Result,id=result.id)
            det_hasil = [
                Det_Result(result=saved_result,value=val["value"],student_id=val["student_id"])
                for val in topsis_formula
            ]

            Det_Result.objects.bulk_create(det_hasil)

    return render(request,"index.html")

def get_all_results(request):
    data = Result.objects.all()
    custom_labels = {
        'name':'Name',
        'email':'Email',
        'date':'Date'
    }
    return render(request,"result_list.html",{"data":data,"custom_labels":custom_labels})

# get detail result by result id
def get_detail_result(request,result_id,type):
    data_detail = list(Det_Result.objects.filter(result_id=result_id).select_related("students").values(
        'id',
        'value',
        'student__id',
        'student__name',
    ).order_by("-value"))


    custom_labels = {
        "rank":"Rank",
        'student':"Student",
        'value':"Value"
    }

    template_path = 'result_report.html'  
    context = {
        'custom_labels': custom_labels,  # Replace with your custom labels
        'data': data_detail,  # Replace with your data
    }

    if type == 'pdf':
        html_content = render_to_string(template_path, context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="topsis_report.pdf"'
        pisa_status = pisa.CreatePDF(html_content, dest=response)

        # return pdf as response
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html_content + '</pre>', content_type='text/html')
        return response
    
    elif type == 'excel':
        html_data = create_html_excel(context)

        df_list = pd.read_html(html_data)
        df = df_list[0]

        # Create a BytesIO buffer for the Excel file
        excel_buffer = BytesIO()

        # Save DataFrame to Excel buffer
        df.to_excel(excel_buffer, index=False)

        # Set response headers for Excel file download
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=output.xlsx'

        # Write Excel buffer to the response
        excel_buffer.seek(0)
        response.write(excel_buffer.read())

        return response

