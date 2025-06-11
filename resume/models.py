from django.db import models

# Create your models here.
class WorkExperience(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    prev_job_title1 = models.CharField(max_length=250, blank=True)
    prev_job_title2 = models.CharField(max_length=250, blank=True)
    prev_job_title3 = models.CharField(max_length=250, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(default="", blank=True, null=True)
    work_description = models.TextField(default="")

    def __str__(self):
        return f"{self.name} working at {self.company}"

class Certificates(models.Model):
    course_title = models.CharField(max_length=250)
    skill = models.CharField(max_length=100)
    certificate_obtained_from = models.CharField(max_length=250, default="")
    course_completion_date = models.DateField()
    certificate_obtained = models.BooleanField(default=True)
    certificate_link = models.CharField(max_length=1000, default="")

    def __str__(self):
        return f"{self.course_title}"

class Education(models.Model):
    degree = models.CharField(max_length=250)
    university = models.CharField(max_length=250)
    college = models.CharField(max_length=500, default="")
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    subjects = models.TextField(default="")
    graduated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.degree} from {self.university}"
