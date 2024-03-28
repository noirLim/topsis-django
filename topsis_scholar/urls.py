from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
      path('',views.index_home,name="home"),
      path("students/",include("students.urls")),
      path("criteria/",include("criteria.urls")),
      path("alternative/",include("criteria.alternative_urls")),
      path("result/",include("result.urls"))
]
