from django.contrib import admin
from .models import Cat
from .models import Dog


admin.site.register(Cat)
admin.site.register(Dog)