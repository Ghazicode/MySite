from django.shortcuts import render, redirect, HttpResponse
from .models import About_Me, Contact, Portfolio, Blog
import requests


TELEGRAM_BOT_TOKEN = 'token'
TELEGRAM_CHAT_ID = 'chat id'

def home(request):

    def send_telegram_message(name, email, body):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': f"پیام جدید \n\nاسم: {name}\n ایمیل : {email}\n پیام : {body}"
    }
        response = requests.post(url, json=payload)
        return response.status_code == 200

    

    #تماس با ما

    if request.method == 'POST':
        if request.POST.get('gender') == 'male':
            gender = Contact.gender = False
        else:
            gender = True
            
            
        
        
        
        


        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        send_telegram_message(name, email, body)
        Contact.objects.create(name = name, email = email, body = body,gender = gender )
        return redirect('/')







    about_me = About_Me.objects.all().last()

 






    portfolios = Portfolio.objects.all().order_by('-id')
    




    blog_list = Blog.objects.filter(status = True)[:3]

    testimonials = Contact.objects.filter(status=True).order_by('-id')[:4]




    
    

    return render (request, "blog_app/home.html", {'about':about_me , 'project':portfolios, 'blog_list':blog_list, 'testimonials':testimonials })



    
        

def error(request,pk):
    return render(request, 'blog_app/error.html',{'pk':pk})

    
