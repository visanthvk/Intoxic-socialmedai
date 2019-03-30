from django.db import models
from profanity_check import predict, predict_prob

class MyPostManager(models.Manager):
    def validator(self, postData):
        errors = {}
        ans = predict([postData['desc']])
        if(int(ans[0]) > 0):
            errors['toxic'] = "Your post has toxic content!"
            
        return errors


class MyPost(models.Model):
    user = models.EmailField(max_length=254)
    desc = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    objects = MyPostManager()
    def __str__(self):
        return(self.user)
