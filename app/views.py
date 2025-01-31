from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Citizen, Service, Complaint, Feedback
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'is_published', 'author']
    template_name = 'app/blog_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'is_published', 'author']
    template_name = 'app/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')

class CitizenListView(ListView):
    model = Citizen
    context_object_name = 'citizen'
    template_name = 'app/citizen_list.html'

class CitizenDetailView(DetailView):
    model = Citizen
    context_object_name = 'citizen'
    template_name = 'app/citizen_detail.html'

class CitizenCreateView(CreateView):
    model = Citizen
    fields = ['first_name', 'last_name', 'email', 'address', 'date_of_birth', 'gender']
    template_name = 'app/citizen_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class CitizenUpdateView(UpdateView):
    model = Citizen

    fields = ['first_name', 'last_name', 'email', 'address', 'date_of_birth', 'gender']
    template_name = 'app/citizen_update.html'

class CitizenDeleteView(DeleteView):
    model = Citizen
    template_name = 'app/citizen_delete.html'
    success_url = reverse_lazy('citizen')

class ServiceListView(ListView):
    model = Service
    context_object_name = 'service'
    template_name = 'app/service_list.html'

class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'app/service_detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description']
    template_name = 'app/service_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ServiceUpdateView(UpdateView):
    model = Service

    fields = ['name', 'description']
    template_name = 'app/service_update.html'

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'app/service_delete.html'
    success_url = reverse_lazy('service')

class ComplaintListView(ListView):
    model = Complaint
    context_object_name = 'complaint'
    template_name = 'app/citizen_list.html'

class ComplaintDetailView(DetailView):
    model = Complaint
    context_object_name = 'complaint'
    template_name = 'app/citizen_detail.html'

class ComplaintCreateView(CreateView):
    model = Complaint
    fields = ['title', 'citizen', 'description', 'submission_date']
    template_name = 'app/complaint_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ComplaintUpdateView(UpdateView):
    model = Complaint

    fields = ['title', 'citizen', 'description', 'submission_date']
    template_name = 'app/complaint_update.html'

class ComplaintDeleteView(DeleteView):
    model = Complaint
    template_name = 'app/complaint_delete.html'
    success_url = reverse_lazy('complaint')

class FeedbackListView(ListView):
    model = Feedback
    context_object_name = 'feedback'
    template_name = 'app/service_list.html'

class FeedbackDetailView(DetailView):
    model = Feedback
    context_object_name = 'feedback'
    template_name = 'app/feedback_detail.html'

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['citizen', 'service', 'comments', 'rating']
    template_name = 'app/feedback_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class FeedbackUpdateView(UpdateView):
    model = Feedback

    fields = ['citizen', 'service', 'comments', 'rating']
    template_name = 'app/feedback_update.html'

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'app/feedback_delete.html'
    success_url = reverse_lazy('feedback')


    
