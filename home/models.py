from django.db import models

# Create your models here.
class Region(models.Model): # viloyat
    region = models.CharField(max_length=100)

class City(models.Model): # shahar
    city = models.CharField(max_length=100)

class Languages(models.Model): # tillar
    name = models.CharField(max_length=100)

class User_Type(): # foydalanuvchining turlari
    user_type = models.TextField()
    
    # user_type ni shunchaki choises qilib client va freelancer dan iborat qilmaganligimning sababi, kelajakda boshqa type lar ham qo'shilishi mumkin: masalan Premium    

class Certificate(models.Model):
    certificate_name = models.TextField()
    
class Freelancer(models.Model): # freelancer
    
    name = models.CharField(max_length=50)
    
    family_name = models.CharField(max_length=50)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    phone_number = models.IntegerField()
    
    telegram_username = models.TextField()

    type = models.ForeignKey(User_Type) # bu type foydalanuvchining 'freelancer' yoki mijoz ligini anglatadi
    
    languages = models.ForeignKey(Languages)
    
    plastic_card = models.IntegerField()
    
    certificate = models.ForeignKey(Certificate)
    
    example = models.TextField()
    
class Client(models.Model): # mijoz
    name = models.CharField(max_length=50)
    
    family_name = models.CharField(max_length=50)
    
    phone_number = models.IntegerField()
    
    telegram_username = models.TextField()
    
    type = models.ForeignKey(User_Type, on_delete=models.CASCADE) # bu type foydalanuvchining 'freelancer' yoki mijoz ligini anglatadi
    
    plastic_card = models.IntegerField()


