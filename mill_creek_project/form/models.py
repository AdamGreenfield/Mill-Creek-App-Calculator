from django.db import models
from django.utils import timezone
from django import forms

class Costs(models.Model):
	name = models.CharField(max_length=10, default="Costs", editable=False)
	iOSCost = models.IntegerField(default=0, verbose_name="iOS")
	androidCost = models.IntegerField(default=0, verbose_name="Android")
	webCost = models.IntegerField(default=0, verbose_name="Web")
	loginCost = models.IntegerField(default=0, verbose_name="Login")
	emailLoginCost = models.IntegerField(default=0, verbose_name="Email login")
	socialLoginCost = models.IntegerField(default=0, verbose_name="Social login")
	upfrontCost = models.IntegerField(default=0, verbose_name="Upfront")
	inappCost = models.IntegerField(default=0, verbose_name="In-app purchases")
	connectionCost = models.IntegerField(default=0, verbose_name="Connectivity")
	stockCost = models.IntegerField(default=0, verbose_name="Stock design")
	beautifulCost = models.IntegerField(default=0, verbose_name="Beautiful design")
	musicCost = models.IntegerField(default=0, verbose_name="Audio/Music")
	calendarCost = models.IntegerField(default=0, verbose_name="Calendar")
	geolocationCost = models.IntegerField(default=0, verbose_name="Geolocation")
	cameraCost = models.IntegerField(default=0, verbose_name="Camera/Video")
	mapsCost = models.IntegerField(default=0, verbose_name="Maps")
	smsCost = models.IntegerField(default=0, verbose_name="SMS integration")
	ecommerceCost = models.IntegerField(default=0, verbose_name="Ecommerce")
	searchCost = models.IntegerField(default=0, verbose_name="Search")
	feedCost = models.IntegerField(default=0, verbose_name="Activity feed")
	ratingCost = models.IntegerField(default=0, verbose_name="Rating system")
	sharingCost = models.IntegerField(default=0, verbose_name="Social sharing")
	dashboardCost = models.IntegerField(default=0, verbose_name="Dashboard")
	alotCost = models.IntegerField(default=0, verbose_name="Great deal of content management")
	notmuchCost = models.IntegerField(default=0, verbose_name="Not much content management")
	
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Cost'
		verbose_name_plural = 'Costs'