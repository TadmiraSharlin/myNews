from django.shortcuts import render, get_object_or_404, redirect
from . models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from comment.models import Comment



def news_details(request,pk):
    
    shownews = News.objects.filter(pk = pk)
    
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]

    tagname = News.objects.get(pk=pk).tag
    tag = tagname.split(',')

    try:
        mynews = News.objects.get(pk = pk)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't add show")

    code = News.objects.get(pk=pk).pk
    comments = Comment.objects.filter(news_id=pk)

    return render(request, 'front/news_details.html', {'comments':comments,'code':code, 'shownews':shownews, 'site':site, 'news':news, 'cat':cat, 'subcat': subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'tag':tag})


def news_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    perm = 0
    for n in request.user.groups.all():
        if n.name == "masteruser":
            perm = 1
    if perm == 0:
        news = News.objects.filter(writer=request.user)
    elif perm == 1:
        news = News.objects.all()

    return render(request, 'back/news_list.html', {'news':news})



def news_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

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
    
    cat = SubCat.objects.all()

    if(request.method == 'POST'):

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')


        if newstitle=="" or newscat=="" or newstxtshort=="" or newstxt=="" :
            error = "All fields are required !!!"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            
            if str(myfile.content_type).startswith("image"):
                
                if myfile.size < 5000000 :

                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, time=time, picname=filename, picurl=url, writer=request.user, show=0, catname=newsname, catid=newsid, ocatid=ocatid, tag=tag)
                    b.save()

                    count = len(News.objects.filter(ocatid=ocatid))
        
                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()

                    return redirect('news_list')
                
                else:
                    error = "Your file is bigger than 5 MB !!!"
                    return render(request, 'back/error.html', {'error': error})
            
            else:
                error = "File format not supported !!!"
                return render(request, 'back/error.html', {'error': error})
        
        except:
            error = "Please Input Your Image !!!"
            return render(request, 'back/error.html', {'error': error})


    return render(request, 'back/news_add.html', {'cat': cat})



def news_delete(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    perm = 0
    for n in request.user.groups.all():
        if n.name == "masteruser":
            perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})

    try:
        b = News.objects.get(pk = pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid
       
        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))
        
        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()

    except:
        error = "Something Wrong !!!"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list') 



def news_edit(request, pk):

    if len(News.objects.filter(pk=pk))==0:
        error = "News Not Found !!!"
        return render(request, 'back/error.html', {'error': error})


    perm = 0
    for n in request.user.groups.all():
        if n.name == "masteruser":
            perm = 1
            
    if perm == 0:
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})



    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()

    if(request.method == 'POST'):

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')


        if newstitle=="" or newscat=="" or newstxtshort=="" or newstxt=="" :
            error = "All fields are required !!!"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            
            if str(myfile.content_type).startswith("image"):
                
                if myfile.size < 5000000 :

                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag
                    b.act = 0

                    b.save()
                    return redirect('news_list')
                
                else:
                    error = "Your file is bigger than 5 MB !!!"
                    return render(request, 'back/error.html', {'error': error})
            
            else:
                error = "File format not supported !!!"
                return render(request, 'back/error.html', {'error': error})
        
        except:
                newsname = SubCat.objects.get(pk=newsid).name

                b = News.objects.get(pk=pk)


                b.name = newstitle
                b.short_txt = newstxtshort
                b.body_txt = newstxt
                b.catname = newsname
                b.catid = newsid
                b.tag = tag

                b.save()
                return redirect('news_list')


    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'cat':cat})


def news_publish(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()


    return redirect('news_list')

def news_unpublish(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    # login check end

    news = News.objects.get(pk=pk)
    news.act = 0
    news.save()


    return redirect('news_list')