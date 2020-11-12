from django.shortcuts import render, get_object_or_404, redirect
from . models import ContactForm
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import datetime


def contact_add(request):

	now = datetime.datetime.now()
	year = now.year
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute
	
	if len(str(day)) == 1:
		day = "0" + str(day)
	if len(str(month)) == 1:
		month = "0" + str(month)

	today = str(day) + "/" + str(month) + "/" + str(year)
	time = str(hour) + ":" + str(minute)

	if request.method == 'POST':

		name = request.POST.get('name')
		email = request.POST.get('email')
		txt = request.POST.get('msg')



		if name=="" or email=="" or txt=="":
			msg = "All fields required"
			return render(request, 'front/msgbox.html', {'msg':msg})

		b = ContactForm(name=name, email=email, txt=txt, date=today, time=time)
		b.save()
		msg = "Your message received"
		return render(request, 'front/msgbox.html', {'msg':msg})


	return render(request, 'front/msgbox.html')



def contact_show(request):
	# login check start
	if not request.user.is_authenticated:
		return redirect('my_login')
	# login check end
	

	msg = ContactForm.objects.all()

	return render(request, 'back/message_list.html', {'msg':msg})


def contact_delete(request, pk):

	# login check start
	if not request.user.is_authenticated:
		return redirect('my_login')
	# login check end

	try:
		b = ContactForm.objects.filter(pk=pk)
	   
		b.delete()

	except:
		error = "Something Wrong !!!"
		return render(request, 'back/error.html', {'error': error})

	

	return redirect('contact_show')