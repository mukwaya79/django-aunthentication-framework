from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.views.generic import View
from django.contrib import messages
from django.utils.http  import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.conf import settings
from django.contrib.auth import authenticate,login,logout



# Create your views here.

class RegistrationView(View):
    def get(self,request):
        return render(request,'hardapp/register.html')

    def post(self,request):
         
          
            firstname1 = request.POST.get("name")
            lastname1 = request.POST.get("ln")
            password1 = request.POST.get("password_confirmation")
            email2 = request.POST.get("email")
            mobile1 = request.POST.get("num")
            address1 = request.POST.get("address")
            gender1 = request.POST.get("g")
            country1= request.POST.get("country")
            hobbies1 = request.POST.getlist("x[]")
            date1 = request.POST.get("datetoday")
            file2 = request.FILES.get("file")

            obj33 = Register(Firstname =firstname1, Lastname = lastname1, Password = password1, Email = email2, 
                                Mobile= mobile1, Address = address1, Gender = gender1, Country = country1,
                                Hobbies = hobbies1, Date = date1, File =file2)

            obj33.save()

            user=User.objects.create_user(username=firstname1,email=email2)
            user.set_password(password1)
            user.first_name = firstname1
            user.last_name =lastname1
            User.is_active = False
            user.save()

            current_site = get_current_site(request)
            email_subject = 'Account Activation'
            message = render_to_string('hardapp/activate.html',
            {
                'user':user,
                'domain' :current_site.domain,
                'uid' :urlsafe_base64_encode(force_bytes (user.pk)),
                'token' :generate_token.make_token(user)

                }
            )

            email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email2]
    
            )

            email_message.send()



           

            return redirect ('login')

       


class LoginView(View):
     def get(self,request):
        return render(request,'hardapp/login.html')

     def post(self,request):
         
             username =request.POST.get('username')
             password =request.POST.get('password')

             user=authenticate(request,username=username,password=password)

             login(request,user)

             return redirect( "home")


             return render(request,'hardapp/login.html')

class ActivateView(View):
     def get (self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            pass
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user,token):
            user_active = True
            user.save()

            messages.add_message(request,messages.SUCCESS, 'Account activated Successfully')

            return redirect ('login')

        return render(request,'hardapp/activate_failed.html')
        
class HomeView(View):
    def get(self,request):
        return render (request,'hardapp/index.html')

class LogoutView(View):
    def get(self,request):
        logout(request)
        
        return render ( request ,'hardapp/login.html')