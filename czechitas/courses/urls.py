from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("kontakty/", views.ContactsView.as_view(), name="contacts"),
    path("kurzy/", views.CourseListView.as_view(), name="course_list"),
    path("pobocky/", views.BranchListView.as_view(), name="branch_list"),
    path("kurz/<int:pk>", views.CourseDetailView.as_view(), name="course_detail"),
    path("branch/<int:pk>", views.BranchDetailView.as_view(), name="branch_detail"),
    path("prihlaska/", views.ApplicationCreateView.as_view(), name="application_create"),
    path("prihlaska/potvrzeni/", views.ApplicationConfirmationView.as_view(), name="application_confirmation"),
    path("registrace-do-tymu/", views.PersonRegisterView.as_view(), name="person_register"),
]
