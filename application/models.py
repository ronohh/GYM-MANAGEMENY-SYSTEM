from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.IntegerField()

    def __str__(self):
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name

#     admin
# create a class that students can book classes with( morning and evening )
# create a user side form html

# subscription monthly

class MonthlyPackage(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class HalfPackage(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.name

class YearlyPackage(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

#     sign up a new admin new admin details

class NewAdmin(models.Model):
    name = models.CharField(max_length=100)
    employee_no = models.IntegerField()
    password = models.IntegerField()
    confirm_password = models.IntegerField()

    def __str__(self):
        return self.name


    # add class where a admin can add  new class
