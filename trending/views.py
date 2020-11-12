from django.shortcuts import render, get_object_or_404, redirect
from . models import Trending


def trending_add(request):

	# login check start
	if not request.user.is_authenticated:
		return redirect('my_login')
	# login check end

	if request.method == 'POST':

		txt = request.POST.get('txt')

		if txt == "":
			error = "All Fields Required"
			return render(request, 'back/error.html', {'error':error})

		b = Trending(txt=txt)
		b.save()

	trending = Trending.objects.all()


	return render(request, 'back/trending.html', {'trending':trending})


def trending_delete(request, pk):

	# login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    try:
        b = Trending.objects.get(pk = pk)
       
        b.delete()

    except:
        error = "Something Wrong !!!"
        return render(request, 'back/error.html', {'error': error})
    return redirect('trending_add')


def trending_edit(request, pk):
	# login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    mytxt = Trending.objects.get(pk=pk).txt

    if request.method == 'POST':

    	txt = request.POST.get('txt')

    	if txt == "":
    		error = "All Fields Required"
    		return render(request, 'back/error.html', {'error':error})

    	b = Trending.objects.get(pk=pk)
    	b.txt = txt
    	b.save()

    	return redirect('trending_add')




    return render(request, 'back/trending_edit.html', {'mytxt':mytxt, 'pk':pk})