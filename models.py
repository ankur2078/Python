from django.db import models


class Employee(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=20)
    email = models.EmailField()
    econtact = models.CharField(max_length=10)

    class Meta:
        db_table = "Employee"
