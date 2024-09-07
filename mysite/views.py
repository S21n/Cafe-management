from pdb import post_mortem
from django.shortcuts import render
def Home(request):
    return render(request,"Home.html")
def About(request):
    return render(request,"About.html")
def Contact(request):
    return render(request,"Contact.html")
def Index(request):
    return render(request,"index.html")
def Menu(request):
    return render(request,"Menu.html")
def Ragister(request):
    return render(request,"Ragister.html")
def SignUp(request):
    try:
         # if request.methode=="post":
             email=request.POST.get('email')
             password=request.POST.get('psw')
             repeatPassword=request.POST.get('psd-repeat')
             print(email+password)    
    except:
     pass
    return render(request,"Signup.html")







# copy from internet 
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'posts/create.html')  

        else:
                return render(request,'posts/create.html')


