
# Create your models here.
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cat_info'

class Book(models.Model):
    title = models.CharField(max_length=30)
    #If category is deleted then every book record associated with that perticular category should also be deleted
    #from the database..
    category= models.ForeignKey(Category,related_name="books",on_delete=models.CASCADE)

    #Every book has isbn unumber and it is 13 digit number
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    #if that category is delelted all the product online should be deleted..
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)

    price =  models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']  #i want to be most recently added item at the top.

    def __str__(self):
        #i choose prod name and prod price..
        return '{} {}'.format(self.product_tag,self.name)