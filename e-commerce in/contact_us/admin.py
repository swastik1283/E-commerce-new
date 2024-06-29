from django.contrib import admin
from contact_us.models import Contact
from contact_us.models import registration

class contact_admin(admin.ModelAdmin):
    list_display = ('email','phone','issue','order_no','message' )

class register_admin(admin.ModelAdmin):
    list_display = ('name1','contact','email','add1','pin','password')

admin.site.register(Contact,contact_admin)
admin.site.register(registration,register_admin)
# Register your models here.
