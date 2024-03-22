from django.db import models

# Create your models here.
#-------------------------------------------------------------------------------------


#--------------------------------------------------------------------------

class books(models.Model):
    b_id=models.IntegerField(primary_key=True)
    b_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    semester=models.IntegerField()
    quantity=models.IntegerField()
    price=models.IntegerField()

class members(models.Model):
    m_id=models.IntegerField(primary_key=True)
    m_name=models.CharField(max_length=100)
    mobile_no=models.IntegerField()
    semester=models.IntegerField()
    branch=models.CharField(max_length=30)

class records(models.Model):
    r_id=models.IntegerField(primary_key=True)
    m_id=models.ForeignKey(members,on_delete=models.SET_NULL,null=True)
    m_name=models.CharField(max_length=100)
    b_id=models.ForeignKey(books,on_delete=models.SET_NULL,null=True)
    b_name=models.CharField(max_length=100)
    issue_date=models.DateField()
    return_date=models.DateField()
    status=models.CharField(max_length=100)
#-----------------------------------------------------------------------------------------------------









    











    

    
