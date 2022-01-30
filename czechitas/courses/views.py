from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from . import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"

class ApplicationConfirmationView(TemplateView):
    template_name = "application_confirmation.html"

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

class CourseDetailView(DetailView):
    template_name = "course_detail.html"
    model = models.Course

class BranchDetailView(DetailView):
    template_name = "branch_detail.html"
    model = models.Branch

class ApplicationCreateView(CreateView):
    template_name = "application_create.html"
    model = models.Application
    fields = ["email", "name", "course"]
    success_url = reverse_lazy("application_confirmation")

class PersonRegisterView(CreateView):
    template_name = "application_create.html"
    model = models.Person
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("application_confirmation")
