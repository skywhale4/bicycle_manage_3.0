from django.db import models

# Create your models here.
class User(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True)
    userpwd=models.CharField(max_length=50)
    regtime=models.DateTimeField()
    logtime=models.DateTimeField(null=True)

class Admin(models.Model):
    adminid=models.AutoField(primary_key=True)
    adminname=models.CharField(max_length=50,unique=True)
    adminpwd=models.CharField(max_length=50)

class Bicycle(models.Model):
    carid=models.AutoField(primary_key=True)
    carbrand=models.CharField(max_length=50) #品牌
    layplace=models.CharField(max_length=50) #车的位置
    status=models.CharField(max_length=50) #车的使用状态

class Record(models.Model):  #用车记录
    username=models.CharField(max_length=50)
    carid=models.IntegerField()
    borrowtime=models.DateTimeField() #借车时间
    returntime=models.DateTimeField(null=True) #还车时间
    borrowplace = models.CharField(max_length=50)  # 借车地点
    returnplace = models.CharField(max_length=50,null=True)  # 还车地点
