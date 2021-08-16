from django.contrib import admin
from .models import User,Employer,Employee,Asset,AssignedAsset,Leave
class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(AssignedAsset)
admin.site.register(Leave)
