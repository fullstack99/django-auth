from __future__ import unicode_literals
from django.db import models
# from validate_email import validate_email
from email_validator import validate_email, EmailNotValidError

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['firstName'] = "First name can not be shorter than 2 characters"
            pass

        if len(postData['lastName']) < 2:
            errors['lastName'] = "Last name can not be shorter than 2 characters"
            pass

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
            pass
        try:
            valid_info = validate_email(postData['email'], allow_smtputf8=False)
            email = valid_info["email"]
        except EmailNotValidError as e:
            errors['email'] = str(e)

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"
            pass

        if (postData['password'] != postData['confirmPassword']):
            errors['confirmPassword'] = "Password does not matched!"
            pass

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    picture = models.ImageField(upload_to = 'pictures')
    permission = models.CharField(max_length=255, default="user")
    objects = UserManager()

    class Meta:
        db_table = "users"