from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Links(models.Model):
    link = models.CharField(max_length=500, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class JobDetail(models.Model):
    company_id = models.CharField(max_length=300, blank=True, null=True)
    job_title = models.CharField(max_length=1000, blank=True, null=True)
    is_approved = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)
    is_filled = models.IntegerField(default=0)
    is_featured = models.IntegerField(default=0)
    job_country = models.CharField(max_length=1000, blank=True, null=True)
    job_state = models.CharField(max_length=1000, blank=True, null=True)
    job_zip_code = models.CharField(max_length=1000, blank=True, null=True)
    job_city = models.CharField(max_length=200, blank=True, null=True)
    job_address = models.CharField(max_length=200, blank=True, null=True)

    category = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    payment_method = models.CharField(max_length=1000, blank=True, null=True)
    job_created_at = models.CharField(max_length=1000, blank=True, null=True)
    job_expires_at = models.CharField(max_length=1000, blank=True, null=True)
    company_website = models.CharField(max_length=1000, blank=True, null=True)
    wpjobboard_am_data = models.CharField(max_length=1000, blank=True, null=True)

    company_name = models.CharField(max_length=1000, blank=True, null=True)
    company_email = models.CharField(max_length=1000, blank=True, null=True)
    company_logo = models.CharField(max_length=1000, blank=True, null=True)
    company_country = models.CharField(max_length=1000, blank=True, null=True)
    company_state = models.CharField(max_length=1000, blank=True, null=True)
    company_zip_code = models.CharField(max_length=1000, blank=True, null=True)
    company_location = models.CharField(max_length=1000, blank=True, null=True)
    company_info = models.CharField(max_length=1000, blank=True, null=True)

    is_public = models.CharField(max_length=1000, blank=True, null=True)
    company_slogan = models.CharField(max_length=1000, blank=True, null=True)
    remote_ready = models.CharField(max_length=1000, blank=True, null=True)
    company_size = models.CharField(max_length=1000, blank=True, null=True)
    twitter_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_link = models.CharField(max_length=1000, blank=True, null=True)
    facebook_link = models.CharField(max_length=1000, blank=True, null=True)
    job_description = RichTextField(default=None, blank=True, null=True)
    job_description_format = models.CharField(max_length=20, default="html")
    price_per_hour = models.CharField(max_length=1000, blank=True, null=True)
    salary = models.CharField(max_length=1000, blank=True, null=True)
    job_link = models.CharField(max_length=1000, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ('-create_at',)
