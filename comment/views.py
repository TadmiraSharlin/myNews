from django.shortcuts import render, get_object_or_404, redirect
from . models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import datetime
# Create your views here.

def news_cm_add(request, pk):

	if request.method == "POST":

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
	    

		cm = request.POST.get('msg')

		if request.user.is_authenticated:
			manager = Manager.objects.get(utxt=request.user)

			b = Comment(name=manager.name, news_id=pk, email=manager.email, cm=cm, date=today, time=time)
			b.save()

		else:

			name = request.POST.get('name')
			email = request.POST.get('email')

			b = Comment(name=name, news_id=pk, email=email, cm=cm, date=today, time=time)
			b.save()



	return redirect('news_details', pk=pk)


def comments_list(request):

	# login check start
	if not request.user.is_authenticated:
		return redirect('my_login')
	# login check end

	perm = 0
	for n in request.user.groups.all():
		if n.name == "masteruser":
			perm = 1

	if perm == 0:
		error = "Access Denied!"
		return render(request, 'back/error.html', {'error':error})

	comment = Comment.objects.all()


	return render(request, 'back/comments_list.html', {'comment':comment})


def comment_delete(request, pk):
	# login check start
	if not request.user.is_authenticated:
		return redirect('my_login')
	# login check end

	perm = 0
	for n in request.user.groups.all():
		if n.name == "masteruser":
			perm = 1

	if perm == 0:
		error = "Access Denied!"
		return render(request, 'back/error.html', {'error':error})

	b = Comment.objects.get(pk=pk)
	b.delete()


	return redirect('comments_list')