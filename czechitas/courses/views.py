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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "Ahoj"
        context["branches"] = models.Branch.objects.all()
        return context

class BranchListView(ListView):
    template_name = "branch_list.html"
    model = models.Branch


