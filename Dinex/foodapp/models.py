from django.db import models

# Create your models here.

class AdminDetails(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


#Category model
class Category(models.Model):
    category_name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.category_name
    
#sub-category models
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategories")
    sub_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.sub_category_name


#product model
class Product(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    prod_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prod_name
