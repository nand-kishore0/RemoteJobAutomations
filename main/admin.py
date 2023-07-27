from django.contrib import admin
from .models import Links, JobDetail
from import_export.admin import ExportActionMixin

# Register your models here.

admin.site.register(Links)


class JobDetailAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'job_title', 'job_country', 'job_created_at', 'type', 'company_name',
                    'company_website', 'price_per_hour', 'salary', 'category',  'wpjobboard_am_data', 'create_at')
    list_filter = ('create_at',)
    exclude = ('job_link',)


# job_description
admin.site.register(JobDetail, JobDetailAdmin)
