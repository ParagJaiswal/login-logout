from django.db import models

class Users(models.Model):
	username= models.CharField(max_length=30)
	password= models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	mobile = models.CharField(max_length=30)

	def __str__(self):
		return self.username+" "+self.password+" "+self.email+" "+self.mobile

class Res(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	city = models.CharField(max_length=20)
	mobile = models.CharField(max_length=12)
	education = models.CharField(max_length=50)
	fieldstudy=models.CharField(max_length=100)
	university = models.CharField(max_length=100)
	tpstartm = models.CharField(max_length=50)
	tpstarty = models.CharField(max_length=50)
	tpendm = models.CharField(max_length=50)
	tpendy = models.CharField(max_length=50)
	exptitle =models.CharField(max_length=100)
	expcompany =models.CharField(max_length=100)
	expstartm =models.CharField(max_length=100)
	expstarty =models.CharField(max_length=100)
	expendm =models.CharField(max_length=100)
	expendy =models.CharField(max_length=100)

	def __str__(self):
		return self.first_name+" "+self.last_name+" "+self.city+" "+self.mobile+" "+self.education+" "+self.fieldstudy+" "+self.university+" "+self.tpstartm+" "+self.tpstarty+" "+self.tpendm+" "+self.tpendy+" "+self.exptitle+" "+self.expcompany+" "+self.expstartm+" "+self.expstarty+" "+self.expendm+" "+self.expendy



