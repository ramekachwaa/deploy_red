from django.contrib import admin
from .models import Amenity,House,Image_of_house,Message,Inquiry,Company,Project,footer_text,about
# Register your models here.
admin.site.register(Amenity)
admin.site.register(House)
admin.site.register(Image_of_house)
admin.site.register(Message)
admin.site.register(Inquiry)
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(footer_text)
admin.site.register(about)

