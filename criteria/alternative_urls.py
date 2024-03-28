from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_alternative,name="alternative"),
    path("submit",views.submit_alternative_form,name="submit_alternative_form"),
    path("submit/edit/<int:alt_id>",views.submit_alternative_form,name="submit_alternative_form"),
    path("list",views.get_all_alternative,name="list"),
    path("edit/<int:alt_id>",views.get_alternative_by_id,name="get_alternative_by_id"),    
    path("delete/<int:alt_id>",views.delete_alternative_by_id,name="delete_alternative_by_id"),
]
