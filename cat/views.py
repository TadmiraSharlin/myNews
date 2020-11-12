from django.shortcuts import render, get_object_or_404, redirect
from . models import Cat

def cat_list(request):

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
    
    cat = Cat.objects.all()
    return render(request, 'back/cat_list.html', {'cat':cat})


def cat_add(request):

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

    cat = Cat.objects.all()

    if(request.method == 'POST'):

        name = request.POST.get('name')
 
        if name=="":
            error = "All fields are required !!!"
            return render(request, 'back/error.html', {'error': error})
        
        for n in cat:
            if name == n.name:
                error = "Category Already Exists !!!"
                return render(request, 'back/error.html', {'error': error})


        b = Cat(name = name)
        b.save()

        return redirect('cat_list')
    
    return render(request, 'back/cat_add.html')


def cat_delete(request, pk):

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
        b = Cat.objects.get(pk = pk)
       
        b.delete()

    except:
        error = "Something Wrong !!!"
        return render(request, 'back/error.html', {'error': error})

    return redirect('cat_list') 