from django.db import models
from django.urls import reverse
from django.conf import settings

class Citizen(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("citizen_detail", kwargs={"pk": self.pk})


class Service(models.Model):
    name = models.CharField(max_length=200, default='dog control')
    description = models.TextField()

    def __str__(self):
        return f"Service: {self.name}"


class Complaint(models.Model):
    title = models.CharField(max_length=100, null=True)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name="complaints")
    description = models.TextField(null=True)
    submission_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Complaint {self.id} from {self.citizen}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Citizen, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

class Feedback(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name="feedbacks")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name="feedbacks")
    comments = models.TextField(null=True)
    rating = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Feedback from {self.citizen.first_name} {self.citizen.last_name} ({self.rating} stars)"
    

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    