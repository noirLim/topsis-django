from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_criteria,name="criteria"),
    path("submit",views.submit_criteria_form,name="submit_criteria_form"),
    path("submit/edit/<int:criteria_id>",views.submit_criteria_form,name="submit_criteria_form"),
    path("list",views.get_all_criteria,name="list"),
    path("edit/<int:criteria_id>",views.get_criteria_by_id,name="get_criteria_by_id"),    
    path("delete/<int:criteria_id>",views.delete_criteria_by_id,name="delete_criteria_by_id"),
]
