from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_student,name="students"),
    path("submit",views.submit_student_form,name="submit_student_form"),
    path("list",views.get_all_students,name="list"),
    path("edit/<int:student_id>",views.get_student_by_id,name="get_student_by_id"),
    path("submit/edit/<int:student_id>",views.submit_student_form,name="submit_student_form"),
    path("delete/<int:student_id>",views.delete_student_by_id,name="delete_student_by_id"),
]
