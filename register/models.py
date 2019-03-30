from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        temp = 0
        users = User.objects.all()
        for user in users:
            if(user.email == postData['email']):
                temp = 1
        print(temp)
        if(temp==1):
            errors['email'] = "An account with this email already exists!"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        if(int(postData['age'])<18):
            errors['age'] = "You must above 18 years of age to sign up!"
        
        if(str(postData['password'])!=str(postData['confirm_password'])):
            errors['confirm_password'] = "Passwords doesn't match!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER = (
        ("m","Male"),
        ("f","Female"),
    )
    gender = models.CharField(max_length=10,choices=GENDER)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return self.email