from django.db import models
from django.contrib.auth.models import User



class About_Me(models.Model):
    me = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)


    instagram = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)
    github = models.CharField(max_length=150)


    def __str__(self):
        return self.me

    





class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    
    # این فیلد برای آپلود فایل فشرده وب‌سایت است (مثلاً یک فایل .zip)
    # website_zip_file = models.FileField(upload_to='portfolio_zips/', blank=True, null=True) 
    UrlPortfolio = models.URLField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    
    
    def __str__(self):
        return self.title





class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    body = models.TextField()                
    image = models.FileField(upload_to='test',null=True,blank=True)
    UrlBlog = models.URLField(max_length=2000, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title






class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    status = models.BooleanField(default=False)
    gender = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} - {self.body[:20]}"






    
    

    

