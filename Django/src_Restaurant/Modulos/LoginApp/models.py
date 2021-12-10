from django.db import models
from Modulos.LoginApp.choice import ROLES


class Login(models.Model):
    iduser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    passworduser = models.CharField(max_length=30)
    rol = models.CharField(max_length=30, choices=ROLES,default="ADMIN")
    state = models.CharField(max_length=1)
    
    class Meta:
        db_table = "Login"
    def __str__(self):
        return self.username


        
