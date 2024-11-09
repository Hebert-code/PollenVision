from django.contrib import admin
from .models import Profile, Plant, Image, AnalysisResult

admin.site.register(Profile)
admin.site.register(Plant)
admin.site.register(Image)
admin.site.register(AnalysisResult)