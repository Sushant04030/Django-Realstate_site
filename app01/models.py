from django.db import models

# Create your models here.



# # # # property type Model # # # # #  
class PropertyType(models.Model):
    title               = models.CharField(max_length=200,blank = True, null= True)
    image               = models.ImageField(upload_to='static/images', blank = True, null= True)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}" 

# # # # locations Model # # # # #  
class City(models.Model):
    title               = models.CharField(max_length=200,blank = True, null= True)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.title}'

# # # # gallery Model # # # # #  
class Property(models.Model):
    title               = models.CharField(max_length=200,blank = True, null= True)
    image               = models.ImageField(upload_to='static/images', blank = True, null= True)
    type                = models.ForeignKey(PropertyType, on_delete=models.SET_NULL,null=True)
    city                = models.ForeignKey(City, on_delete=models.SET_NULL,null=True)
    description         = models.TextField(blank=True,null=True)
    address             = models.CharField(max_length=250,blank=True,null=True)

    room                = models.IntegerField(default=0)
    hall                = models.IntegerField(default=0)
    kitchen             = models.IntegerField(default=0)
    bathroom            = models.IntegerField(default=0)
    area                = models.CharField(default=None,null=True, max_length=200)

    featured            = models.BooleanField(default=False)
    sale                = models.BooleanField(default=False)
    rent                = models.BooleanField(default=False)

    price_in_text       = models.CharField(max_length=250,blank=True,null=True)
    price               = models.IntegerField(default=0)

    ## aminities ##
    parking             = models.BooleanField(default=False)
    camera              = models.BooleanField(default=False)
    water               = models.BooleanField(default=False)
    balcony             = models.BooleanField(default=False)
    power               = models.BooleanField(default=False)
    garden              = models.BooleanField(default=False)
    furnished           = models.BooleanField(default=False)
    gym                 = models.BooleanField(default=False)
    swimming_pool       = models.BooleanField(default=False)
    garbage_disposal    = models.BooleanField(default=False)
    modular_kitchen     = models.BooleanField(default=False)
    hot_water           = models.BooleanField(default=False)
    lift                = models.BooleanField(default=False)
    ac                  = models.BooleanField(default=False)
    wifi                = models.BooleanField(default=False)
    washing_machine     = models.BooleanField(default=False)
    security            = models.BooleanField(default=False)
    solar               = models.BooleanField(default=False)

    map_link            = models.TextField(blank = True, null= True)
    available           = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}" 
    
    class Meta:
        verbose_name= 'Property'
        verbose_name_plural = 'Properties'
    

# # # # agents Model # # # # #  
class Agent(models.Model):
    fullname            = models.CharField(max_length=200,blank = True, null= True)
    image               = models.ImageField(upload_to='static/images', blank = True, null= True)
    city                = models.ForeignKey(City, on_delete=models.SET_NULL,null=True)
    phone               = models.CharField(max_length=200,null=True,default=None)
    email                = models.CharField(max_length=200,null=True,default=None)
    facebook            = models.CharField(max_length=200,null=True,default=None)
    instagram           = models.CharField(max_length=200,null=True,default=None)
    twitter             = models.CharField(max_length=200,null=True,default=None)
    tiktok              = models.CharField(max_length=200,null=True,default=None)
    skype               = models.CharField(max_length=200,null=True,default=None)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}" 

# # # # testimonial Model # # # # #  
class Testimonial(models.Model):
    fullname            = models.CharField(max_length=200,blank = True, null= True)
    image               = models.ImageField(upload_to='static/images', blank = True, null= True)
    profession          = models.CharField(max_length=200,null=True,default=None)
    comment             = models.TextField(null=True,default=None)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}" 
    

# # # # gallery Model # # # # #  
class Gallery(models.Model):
    property            = models.ForeignKey(Property, on_delete=models.CASCADE,default=None)
    title               = models.CharField(default=None,null=True, max_length=200)
    image               = models.ImageField(upload_to='static/images', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name= 'Gallery'
        verbose_name_plural = 'Galleries'
    

# # # # contact model # # # # #
class Contact(models.Model):
    fullname            = models.CharField(max_length=200,blank = True, null= True)
    email               = models.TextField(blank = True, null= True)
    subject             = models.CharField(max_length=200,blank = True, null= True)
    message             = models.TextField(blank = True, null= True)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} {self.fullname}"
    