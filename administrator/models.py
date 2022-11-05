from django.db import models

# Create your models here.

class Rol(models.Model):
    name = models.CharField(max_length=30)

class VotationGroup(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)


class User (models.Model):
    name = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    dni = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Candidate(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idVotationGroup = models.ForeignKey(VotationGroup, on_delete=models.CASCADE)


class Vote(models.Model):
    codCandidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    codUser = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField()
    date = models.DateField()