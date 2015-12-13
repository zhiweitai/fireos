from django.contrib import admin
from .models import Dgroup,Zgroup,User,Admin,Reinforce,Fireinfo
# Register your models here.

admin.site.register(Dgroup)
admin.site.register(Zgroup)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Reinforce)
admin.site.register(Fireinfo)