from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.http import HttpResponse
from django.template.loader import render_to_string
from form.models import Costs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email import validate_email
# The 'validate_email' method will have to be installed via pip in order to function

# Start page, assigns every session variable to a blank string in order to avoid key errors
def startpage(request):
	# When the submit button is pressed, redirect to a different page
	if request.method == "POST":
		request.session['iOS'] = ''
		request.session['android'] = ''
		request.session['web'] = ''
		request.session['login'] = ''
		request.session['email'] = ''
		request.session['social'] = ''
		request.session['upfront'] = ''
		request.session['inapp'] = ''
		request.session['free'] = ''
		request.session['connection'] = ''
		request.session['stock'] = ''
		request.session['beautiful'] = ''
		request.session['audio'] = ''
		request.session['calendar'] = ''
		request.session['geolocation'] = ''
		request.session['video'] = ''
		request.session['maps'] = ''
		request.session['sms'] = ''
		request.session['ecommerce'] = ''
		request.session['search'] = ''
		request.session['dashboard'] = ''
		request.session['ratings'] = ''
		request.session['feed'] = ''
		request.session['sharing'] = ''
		request.session['greatdeal'] = ''
		request.session['some'] = ''
		request.session['none'] = ''
		request.session['platformString'] = []
		request.session['loginTypeString'] = []
		request.session['paymentString'] = []
		request.session['connectionString'] = []
		request.session['designString'] = []
		request.session['deviceFunctionsString'] = []
		request.session['additionalFunctionsString'] = []
		request.session['contentManagementString'] = []
		return redirect('choose_platform')
	# Otherwise, redirect to the start page
	return render(request, 'form/start_page.html/')
	
def choose_platform(request):
	# To prevent users from attempting to bypass the start page by typing in the exact URL of this page
	if 'platformString' not in request.session:
		return redirect('startpage')
	# When the submit button is pressed
	if request.method == "POST":
		list = []
		# Assigns the values of the checkboxes on the web page to variables. The variables are empty strings if not selected
		if 'answeriOS' in request.POST:
			platformiOS = request.POST['answeriOS']
		else:
			platformiOS = ""
		if 'answerAndroid' in request.POST:
			platformandroid = request.POST['answerAndroid']
		else:
			platformandroid = ""
		if 'answerWeb' in request.POST:
			platformWeb = request.POST['answerWeb']
		else:
			platformWeb = ''
		# Assigns True or False to the session variables, used in calculate_total method
		request.session['iOS'] = (platformiOS == 'iOS')
		request.session['android'] = (platformandroid == 'Android')
		request.session['web'] = (platformWeb == 'Web')
		# Forming the string that is used in the email
		request.session['platformString'] = ''
		# '______String' session variables are used when sending the email at the end of the program
		if request.session['iOS']:
			list.append('iOS')
		if request.session['android']:
			list.append('Android')
		if request.session['web']:
			list.append('Web')
		request.session['platformString'] = list
		return redirect('choose_login')
	return render(request, 'form/choose_platform.html/')

def choose_login(request):
	if 'loginTypeString' not in request.session:
		return redirect('startpage')
	# Calling the calculate_total method. This method was implemented rather than just storing the running total in a session variable to fix some problems that were encountered upon pressing the browser's back button
	total = calculate_total(request, 1)
	if request.method == "POST":
		if 'answerYes' in request.POST:
			answerYes = request.POST['answerYes']
		else:
			answerYes = ""
		if 'answerNo' in request.POST:
			answerNo = request.POST['answerNo']
		else:
			answerNo = ""
		if answerYes == "Yes":
			request.session['login'] = True
			return redirect('choose_login_type')
		elif answerNo == "No":
			total = total
			request.session['login'] = False
			request.session['email'] = False
			request.session['social'] = False
			return redirect('choose_payment')
	# Formatting the total and then passing it to the page
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_login.html/', {'total': total})
	
# Every following method up to choose_content_management is basically a copy of the previous method, with some occasional and minor adjustments based on how many options there are on each page
def choose_login_type(request):
	if 'loginTypeString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 2)
	if request.method == "POST":
		list = []
		if 'answerEmail' in request.POST:
			answerEmail = request.POST['answerEmail']
		else:
			answerEmail = ''
		if 'answerSocial' in request.POST:
			answerSocial = request.POST['answerSocial']
		else:
			answerSocial = ''
		request.session['email'] = (answerEmail == 'email')
		request.session['social'] = (answerSocial == 'social')
		request.session['loginTypeString'] = ''
		if request.session['email']:
			list.append('Email')
		if request.session['social']:
			list.append('Social')
		if request.session['email'] == False and request.session['social'] == False:
			list.append('None')
		request.session['loginTypeString'] = list
		return redirect('choose_payment')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_login_type.html/', {'total' : total})
	
def choose_payment(request):
	if 'paymentString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 3)
	if request.method == "POST":
		list = []
		if 'answerUpfront' in request.POST:
			answerUpfront = request.POST['answerUpfront']
		else:
			answerUpfront = ''
		if 'answerInapp' in request.POST:
			answerInapp = request.POST['answerInapp']
		else:
			answerInapp = ''
		if 'answerFree' in request.POST:
			answerFree = request.POST['answerFree']
		else:
			answerFree = ''
		request.session['upfront'] = (answerUpfront == 'up front cost')
		request.session['inapp'] = (answerInapp == 'in-app purchases')
		request.session['free'] = (answerFree == 'free')
		request.session['paymentString'] = ''
		if  request.session['upfront']:
			list.append('Up front cost')
		if request.session['inapp']:
			list.append('In-app purchases')
		if request.session['free']:
			list.append('No monetization')
		request.session['paymentString'] = list
		return redirect('choose_connection')
	total = "$" + format(total, ",d")
	if request.session['login']:
		url = "/choose_login_type/"
	else:
		url = "/choose_login/"
	return render(request, 'form/choose_payment.html/', {'total': total, 'url' : url})

def choose_connection(request):
	if 'connectionString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 4)
	answerYes = ""
	answerNo = ""
	if request.method == "POST":
		list = []
		if 'answerYes' in request.POST:
			answerYes = request.POST['answerYes']
		else:
			answerYes = ""
		if 'answerNo' in request.POST:
			answerNo = request.POST['answerNo']
		else:
			answerNo = ""
		request.session['connection'] = (answerYes == 'Yes')
		request.session['connectionString'] = ''
		if request.session['connection']:
			list.append('Yes')
		elif request.session['connection'] == False:
			list.append('No')
		request.session['connectionString'] = list
		return redirect('choose_design')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_connection.html/', {'total': total})
	
def choose_design(request):
	if 'designString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 5)
	if request.method == "POST":
		list = []
		if 'answerStock' in request.POST:
			answerStock = request.POST['answerStock']
		else:
			answerStock = ""
		if 'answerBeautiful' in request.POST:
			answerBeautiful = request.POST['answerBeautiful']
		else:
			answerBeautiful = ""
		request.session['stock'] = (answerStock == 'Stock')
		request.session['beautiful'] = (answerBeautiful == 'Beautiful')
		request.session['designString'] = ''
		if request.session['stock']:
			list.append('Not very important')
		elif request.session['beautiful']:
			list.append('Very important')
		request.session['designString'] = list
		return redirect('choose_device_functions')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_design.html/', {'total': total})
	
def choose_device_functions(request):
	if 'deviceFunctionsString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 6)
	if request.method == "POST":
		list = []
		if "answerAudio" in request.POST:
			answerAudio = request.POST['answerAudio']
		else:
			answerAudio = ""
		if "answerCalendar" in request.POST:
			answerCalendar = request.POST['answerCalendar']
		else:
			answerCalendar = ""
		if "answerGeolocation" in request.POST:
			answerGeolocation = request.POST['answerGeolocation']
		else:
			answerGeolocation = ""
		if "answerCompass" in request.POST:
			answerCompass = request.POST['answerCompass']
		else:
			answerCompass = ""
		if "answerVideo" in request.POST:
			answerVideo = request.POST['answerVideo']
		else:
			answerVideo = ""
		if "answerPhotos" in request.POST:
			answerPhotos = request.POST['answerPhotos']
		else:
			answerPhotos = ""
		if "answerMaps" in request.POST:
			answerMaps = request.POST['answerMaps']
		else:
			answerMaps = ""
		if "answerSMS" in request.POST:
			answerSMS = request.POST['answerSMS']
		else:
			answerSMS = ""
		request.session['audio'] = (answerAudio == 'audio')
		request.session['calendar'] = (answerCalendar == 'calendar')
		request.session['geolocation'] = (answerGeolocation == 'geolocation')
		request.session['video'] = (answerVideo == 'video')
		request.session['maps'] = (answerMaps == 'maps')
		request.session['sms'] = (answerSMS == 'SMS')
		request.session['deviceFunctionsString'] = ''
		if request.session['audio']:
			list.append('Audio')
		if request.session['calendar']:
			list.append('Calendar')
		if request.session['geolocation']:
			list.append('Geolocation')
		if request.session['video']:
			list.append('Video')
		if request.session['maps']:
			list.append('Maps')
		if request.session['sms']:
			list.append('SMS')
		request.session['deviceFunctionsString'] = list
		return redirect('choose_additional_functions')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_device_functions.html/', {'total': total})
	
def choose_additional_functions(request):
	if 'additionalFunctionsString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 7)
	if request.method == 'POST':
		list = []
		if "answerEcommerce" in request.POST:
			answerEcommerce = request.POST['answerEcommerce']
		else:
			answerEcommerce = ""
		if "answerSearch" in request.POST:
			answerSearch = request.POST['answerSearch']
		else:
			answerSearch = ""
		if "answerDashboard" in request.POST:
			answerDashboard = request.POST['answerDashboard']
		else:
			answerDashboard = ""
		if "answerRatings" in request.POST:
			answerRatings = request.POST['answerRatings']
		else:
			answerRatings = ""
		if "answerFeed" in request.POST:
			answerFeed = request.POST['answerFeed']
		else:
			answerFeed = ""
		if "answerSharing" in request.POST:
			answerSharing = request.POST['answerSharing']
		else:
			answerSharing = ""
		request.session['ecommerce'] = (answerEcommerce == 'ecommerce')
		request.session['search'] = (answerSearch == 'search')
		request.session['dashboard'] = (answerDashboard == 'dashboard')
		request.session['ratings'] = (answerRatings == 'ratings')
		request.session['feed'] = (answerFeed == 'feed')
		request.session['sharing'] = (answerSharing == 'sharing')
		request.session['additionalFunctionsString'] = ''
		if request.session['ecommerce']:
			list.append('Ecommerce')
		if request.session['search']:
			list.append('Search')
		if request.session['dashboard']:
			list.append('Dashboard')
		if request.session['ratings']:
			list.append('Ratings')
		if request.session['feed']:
			list.append('Feed')
		if request.session['sharing']:
			list.append('Sharing')
		request.session['additionalFunctionsString'] = list
		return redirect('choose_content_management')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_additional_functions.html/', {'total': total})
	
def choose_content_management(request):
	if 'contentManagementString' not in request.session:
		return redirect('startpage')
	total = calculate_total(request, 8)
	if request.method == "POST":
		list = []
		if 'answerGreatDeal' in request.POST:
			answerAGreatDeal = request.POST['answerGreatDeal']
		else:
			answerAGreatDeal = ''
		if 'answerSome' in request.POST:
			answerSome = request.POST['answerSome']
		else:
			answerSome = ''
		if 'answerNone' in request.POST:
			answerNone = request.POST['answerNone']
		else:
			answerNone = ''
		request.session['greatdeal'] = (answerAGreatDeal == 'great deal')
		request.session['some'] = (answerSome == 'some')
		request.session['none'] = (answerNone == 'none')
		request.session['contentManagementString'] = ''
		if request.session['greatdeal']:
			list.append('A good deal')
		elif request.session['some']:
			list.append('Some')
		elif request.session['none']:
			list.append('None')
		request.session['contentManagementString'] = list
		return redirect('total_page')
	total = "$" + format(total, ",d")
	return render(request, 'form/choose_content_management.html/', {'total': total})
	
def total_page(request):
	total = calculate_total(request,9)
	if request.method=="POST":
		return redirect('contact_form')
	total = "$" + format(total, ",d")
	return render(request, 'form/total_page.html', {'total': total})
	
# This method redirects to the contact form as well as creates and sends an email
def contact_form(request):
	total = calculate_total(request, 9)
	if request.method == 'POST':
		# Getting the information that the user entered into the contact form
		firstname = request.POST['FirstName']
		lastname = request.POST['LastName']
		phonenumber = request.POST['PhoneNumber']
		clientemail = request.POST['EmailAddress']
		extrainfo = request.POST['ExtraInfo']
		firstNameError = ''
		lastNameError = ''
		phoneNumberError = ''
		clientEmailError = ''
		total = calculate_total(request, 9)
		# Valdiating the entered email address. Again, this requires the 'validate_email' method to be installed via pip
		is_valid = validate_email(clientemail)
		total = "$" + format(total, ",d")
		# Assigning the strings that will be used in the email
		platform = ', '.join(request.session['platformString'])
		login = ', '.join(request.session['loginTypeString'])
		monetization = ', '.join(request.session['paymentString'])
		connection = ', '.join(request.session['connectionString'])
		design = ', '.join(request.session['designString'])
		devicefunctions = ', '.join(request.session['deviceFunctionsString'])
		additionalfunctions = ', '.join(request.session['additionalFunctionsString'])
		contentmanagement = ', '.join(request.session['contentManagementString'])
		# If the entered email is valid, an email will be sent. This simply uses the gmail SMTP server to send an email to itself
		if is_valid:
			# Throwaway gmail account I made for the purposes of testing, can be changed to any gmail address and password
			me = 'test2312580@gmail.com'
			you = 'test2312580@gmail.com'
			username = 'test2312580@gmail.com'
			password = 'notacommonword'
			msg = MIMEMultipart('alternative')
			msg['Subject'] = "%s's App Cost" % firstname
			msg ['From'] = me
			msg ['To'] = you
			text = "Name: %s %s\nPhone Number: %s\nEmail: %s\nExtra Info: %s\n\nPlatform(s): %s\nLogin Type: %s\nMonetization: %s\nDatabase Connection: %s\nDesign: %s\nDevice Functions: %s\nAdditional Functions: %s\nContent Management: %s\nEstimate: %s" % (firstname, lastname, phonenumber, clientemail, extrainfo, platform, login, monetization, connection, design, devicefunctions, additionalfunctions, contentmanagement, total)
			html = """
			<html>
				<head></head>
				<body>
					<b>Name</b>: %s %s<br>
					<b>Phone Number</b>: %s<br>
					<b>Email</b>: %s<br>
					<b>Extra Info</b>: %s<br><br>
					<b>Platform(s)</b>: %s<br>
					<b>Login Type</b>: %s<br>
					<b>Monetization</b>: %s<br>
					<b>Database Connection</b>: %s<br>
					<b>Design</b>: %s<br>
					<b>Device Functions</b>: %s<br>
					<b>Additional Functions</b>: %s<br>
					<b>Content Management</b>: %s<br>
					<b>Estimate</b>: %s
				</body>
			</html>
			"""  % (firstname, lastname, phonenumber, clientemail, extrainfo, platform, login, monetization, connection, design, devicefunctions, additionalfunctions, contentmanagement, total)
			part1 = MIMEText(text,'plain')
			part2 = MIMEText(html, 'html')
			msg.attach(part1)
			msg.attach(part2)
			server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
			server_ssl.ehlo()
			server_ssl.login(username,password)  
			server_ssl.sendmail(me, you, msg.as_string())
			server_ssl.close()
		else:
			clientEmailError = 'Please enter a valid email.'
		if firstname == '':
			firstNameError = 'This field is required.'
		if lastname == '':
			lastNameError = 'This field is required.'
		if phonenumber == '':
			phoneNumberError = 'This field is required.'
		if clientemail == '':
			clientEmailError = 'This field is required.'
		if firstname == '' or lastname == '' or phonenumber == '' or clientemail == '' or clientEmailError == 'Please enter a valid email.':
			return render(request,'form/contact_form_error.html', {'total' : total, 'firstNameError' : firstNameError, 'lastNameError' : lastNameError, 'phoneNumberError' : phoneNumberError, 'clientEmailError' : clientEmailError})
		return redirect('endpage')
	total = "$" + format(total, ",d")
	return render(request, 'form/contact_form.html', {'total' : total})
	
# Final page
def endpage(request):
	total = calculate_total(request, 9)
	total = "$" + format(total, ",d")
	return render(request, 'form/endpage.html', {'total' : total})
	
# Calculates the total. This was done in place of putting the running total in a session variable
def calculate_total(request, page):
	total = 0
	# Gets the list of costs from the database. This database can be accessed and the values can be changed at any time
	Cost = Costs.objects.get(name="Costs")
	iOS = request.session['iOS']
	android = request.session['android']
	web = request.session['web']
	login = request.session['login']
	email = request.session['email']
	social = request.session['social']
	upfront = request.session['upfront']
	inapp = request.session['inapp']
	free = request.session['free']
	connection = request.session['connection']
	stock = request.session['stock']
	beautiful = request.session['beautiful']
	audio = request.session['audio']
	calendar = request.session['calendar']
	geolocation = request.session['geolocation']
	video = request.session['video']
	maps = request.session['maps']
	sms = request.session['sms']
	ecommerce = request.session['ecommerce']
	search = request.session['search']
	dashboard = request.session['dashboard']
	ratings = request.session['ratings']
	feed = request.session['feed']
	sharing = request.session['sharing']
	greatdeal = request.session['greatdeal']
	some = request.session['some']
	none = request.session['none']
	# Every view calls this method with a number. That number tells this method when to stop adding to the total
	if page > 0:
		if iOS:
			total = total + Cost.iOSCost
		if android:
			total = total + Cost.androidCost
		if web:
			total = total + Cost.webCost
	if page > 1:
		if login:
			total = total + Cost.loginCost
	if page > 2:
		if email:
			total = total + Cost.emailLoginCost
		if social:
			total = total + Cost.socialLoginCost
	if page > 3:
		if upfront:
			total = total + Cost.upfrontCost
		if inapp:
			total = total + Cost.inappCost
		if free:
			total = total
	if page > 4:
		if connection:
			total = total + Cost.connectionCost
	if page > 5:
		if stock:
			total = total + Cost.stockCost
		if beautiful:
			total = total + Cost.beautifulCost
	if page > 6:
		if audio:
			total = total + Cost.musicCost
		if calendar:
			total = total + Cost.calendarCost
		if geolocation:
			total = total + Cost.geolocationCost
		if video:
			total = total + Cost.cameraCost
		if maps:
			total = total + Cost.mapsCost
		if sms:
			total = total + Cost.smsCost
	if page > 7:
		if ecommerce:
			total = total + Cost.ecommerceCost
		if search:
			total = total + Cost.searchCost
		if dashboard:
			total = total + Cost.dashboardCost
		if ratings:
			total = total + Cost.ratingCost
		if feed:
			total = total + Cost.feedCost
		if sharing:
			total = total + Cost.sharingCost
	if page > 8:
		if greatdeal:
			total = total + Cost.alotCost
		if some:
			total = total + Cost.notmuchCost
	return total