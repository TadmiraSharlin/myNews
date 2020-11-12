from django.shortcuts import render, get_object_or_404, redirect
from . models import SubCat
from cat.models import Cat

def subcat_list(request):

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
    
    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat':subcat})


def subcat_add(request):

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

    subcat = SubCat.objects.all()
    cat = Cat.objects.all()

    if(request.method == 'POST'):

        name = request.POST.get('name')
        catid = request.POST.get('cat')
 
        if name=="" or catid=="":
            error = "All fields are required !!!"
            return render(request, 'back/error.html', {'error': error})
        
        for n in subcat:
            if name == n.name:
                error = "Name Already Exists !!!"
                return render(request, 'back/error.html', {'error': error})


        catname = Cat.objects.get(pk=catid).name
        b = SubCat(name=name, catname=catname, catid=catid)
        b.save()

        return redirect('subcat_list')
    
    return render(request, 'back/subcat_add.html', {'cat':cat})


def subcat_delete(request, pk):

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

    try:
        b = SubCat.objects.get(pk = pk)
       
        b.delete()

    except:
        error = "Something Wrong !!!"
        return render(request, 'back/error.html', {'error': error})

    return redirect('subcat_list') 