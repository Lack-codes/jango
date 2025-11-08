from django.db import models

# Create your models here.

class EmployeeTable(models.Model):
    Employee_Name = models.CharField()
    Age = models.IntegerField()
    Email_Address = models.EmailField(unique=True)
    Date_of_Joining = models.DateField(default=True)
    
    def __str__(self):
        return self.Employee_Name 
    
class  Product_Table(models.Model):
      Product_Name = models.CharField()
      Brand_Name = models.CharField(choices=[('Iphone','Apple'),('Sliper','VKC')]) 
      price= models.PositiveIntegerField()    
      Manufacturing_Date =models.DateField(auto_now_add=True)
      
      def __str__(self):
        return self.Product_Name 
        
      
class Book_Table(models.Model):
   Book_Title = models.CharField()
   Author_Name =models.CharField()
   Genre = models.CharField(choices=[('m',"comic"),("f",'love'),("o",'Action')],null=True)
   Published_Year = models.IntegerField()
   
   def __str__(self):
       return  self. Book_Title 
   

class  Movie_Table(models.Model) :
    Movie_Title  = models.CharField()
    Director_Name = models.CharField()
    Date = models.DateField()
    Language = models.CharField(default='English')
    
    def __str__(self):
        return  self. Movie_Title

      
class Student_Table(models.Model):
     Student_Name = models.CharField()
     Age = models.IntegerField()
     Email_Address = models.EmailField()
     Date_of_Birth = models.DateField()
     
     def __str__(self):
         return  self.Student_Name
 
         
    

 

  
        
        
 



















 
