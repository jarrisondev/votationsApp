from django.db import models

# Create your models here.

class Rol(models.Model):
    rol = models.CharField(max_length=30)

class VotationGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)


class User (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE )

class User_VotationGroup(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE )
    idVotationGroup = models.ForeignKey(VotationGroup, on_delete=models.CASCADE )


class Vote(models.Model):
    codUser_VotationGroup = models.ForeignKey(User_VotationGroup, on_delete=models.CASCADE )
    codUser = models.ForeignKey(User, on_delete=models.CASCADE )
    active = models.BooleanField()
    date = models.DateField()