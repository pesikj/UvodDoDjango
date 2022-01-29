from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("kontakty/", views.ContactsView.as_view(), name="contacts"),
    path("kurzy/", views.CourseListView.as_view(), name="course_list")
]
