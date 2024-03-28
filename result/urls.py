from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_result,name="result"),
    path("submit",views.submit_result_form,name="submit_result_form"),
    path("list",views.get_all_results,name="list"),
    path("detail/<int:result_id>/<str:type>",views.get_detail_result,name="get_detail_result"),
]
