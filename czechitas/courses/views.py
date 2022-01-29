from django.views.generic.base import TemplateView
from django.views.generic import ListView
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"

class CourseListView(ListView):
    template_name = "course_list.html"
    model = models.Course
