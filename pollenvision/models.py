from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.AutoField(primary_key=True) 
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

  
class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    plant_name = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)  

    
class Image(models.Model):
    image_id = models.AutoField(primary_key=True) 
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE) 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='pollenvision/imagesimport/%Y/%m/%d')

 
class AnalysisResult(models.Model):
    result_id = models.AutoField(primary_key=True) 
    image = models.ForeignKey(Image, on_delete=models.CASCADE)  
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE) 
    viability = models.DecimalField(max_digits=5, decimal_places=2) 
    grain_count = models.IntegerField() 
    error = models.DecimalField(max_digits=5, decimal_places=2) 
    analysis_date = models.DateTimeField(auto_now_add=True) 