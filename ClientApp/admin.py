from django.contrib import admin
from.models import Client,Project

# Register your models here.

""" class AdminClient(admin.ModelAdmin): """
"""  list_display=('name','email','phone','address') """
    
admin.site.register(Client)


""" class AdminProject(admin.ModelAdmin): """
""" list_display=('client','name','description','users')  """   
    
admin.site.register(Project)    