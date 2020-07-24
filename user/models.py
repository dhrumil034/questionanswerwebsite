from django.conf import settings
from django.db import models
from django.utils import timezone 
import os
import hashlib 



class Password(models.Model): 
    salt = models.BinaryField(max_length=32)
    key = models.CharField(max_length=40)

    def verify_password(self,original_password):
        new_key = hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                original_password.encode('utf-8'), # Convert the password to bytes
                self.salt, # Provide the salt
                100000 # It is recommended to use at least 100,000 iterations of SHA-256
                )
        if str(new_key) == str(self.key):
            return True
        return False

def get_image_path(instance, filename):
    return os.path.join('', str(instance.id), filename)

class User(models.Model): 	
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="gallery", blank=True, null=True)
    password = models.ForeignKey(Password, on_delete=models.CASCADE)  

    def verify_password(self,original_password): 
        return self.password.verify_password(original_password)

    class Meta:
        unique_together = ('name', 'email',)




            


