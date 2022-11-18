from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import user_registration, admin_registration
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
import math
import random
import smtplib
# Create your views here.

# class registerationView(View):
#     def post(self, request):
#         name = request.post.get('name')
#         username = request.post.get('username')
#         email  = request.post.get('email')
#         password1 = request.post.get('psw')
#         password2 = request.post.get('psw-repeat')

#         if password1 == password2:
#             if User.objects.filter(username=username).exists(): 
#                 messages.error(request,"Username already exists")
#                 return render(request, "register.html")

#             elif  User.objects.filter(email=email).exists():
#                 messages.error(request,"Email already exists")
#                 return render(request, "register.html")
            
#             else:   
#                 user = User.objects.create(username = username, password= password1, email= email)
#                 register = userRegistration(name= name, username=username, email=email, password= password1, user=user)
#                 register.save()
#                 return render(request,"register.html")
             
#         else:
#             messages.error(request,"Password does not match")
#             return render(request,"register.html")
        
@login_required(login_url='login')           
def home(request):
    retrieve_user = user_registration.objects.all()
    print(retrieve_user)

    return render(request, "home.html", {'retrieve_user': retrieve_user})


def index(request):
    
    return render(request, "index.html")

   
def userRegistration(request):
     
        if request.method == 'POST':
            postData = request.POST
            name = postData.get('name')
            gender = postData.get('gender')
            username = postData.get('username')
            email  = postData.get('email')
            password1 = postData.get('psw')
            password2 = postData.get('psw-repeat')

            if password1 == password2:
                if User.objects.filter(username=username).exists(): 
                    messages.error(request,"Username already exists")
                    return render(request, "User/user_register.html")

                elif  User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists")
                    return render(request, "User/user_register.html")
                elif len(username)<0:
                    messages.error(request,"Please Enter empty field")
                    return render(request, "User/user_register.html")
                elif len(email)<0:
                    messages.error(request,"Please enter empty field")
                    return render(request, "User/user_register.html")  
                elif len(password1)<0:
                    messages.error(request,"Please Enter empty field")
                    return render(request, "User/user_register.html")  
                elif len(password2)<0:
                    messages.error(request,"Please Enter empty field")
                    return render(request, "User/user_register.html")  
                elif name == 0:   
                    messages.error(request,"Please Enter empty field")
                    return render(request, "User/user_register.html")         

                else:   
                    user = User.objects.create_user(username = username, password= password1, email= email)
                    register1 = user_registration(name= name, gender=gender, username=username, email=email,user=user)
                    register1.save()
                    return redirect('signin')
                
            else:
                messages.error(request,"Password does not match")
                return render(request,"User/user_register.html")
            
        return render(request,"User/user_register.html")

def otp(request, reg):
    print(reg)
    # if request.method == 'POST':
    #     postData = request.POST
    #     otp1 = postData.get('sendotp')
    #     print(otp1)
    #     if otp1 == "123":

    #         print("Verified")
    #         print(reg)
    #         user = User.objects.create_user(username = reg['username'],email= reg['email'], password= reg['password1'])
    #         register2 = admin_registration(name_of_org= reg['name_of_org'],year_of_foundation= reg['year_of_foundation'], contact_number= reg['contact_number'],username=reg['username'], email=reg['email'], user=user)
    #         register2.save()
    #         return redirect('signin')
    #         # message.success(request, "OTP has been sent successfully")
    #         # return redirect(request,"home.html")
    #     else:
    #         print("Please Check your OTP again")

    # else:
    #     messages.error(request,"Invalid otp. Please send again")
    #     return render(request, "otp.html")
        
    print(reg)
    return render(request,"otp.html", {'reg':reg})

def adminRegistration(request):
     
        if request.method == 'POST':
            postData = request.POST
            name_of_org = postData.get('nameoforganization')
            year_of_foundation = postData.get('foundationyear')
            contact_number = postData.get('contact')
            username = postData.get('username')
            email  = postData.get('email')
            password1 = postData.get('psw')
            password2 = postData.get('psw-repeat')
            # reg = {'name_of_org':name_of_org, 'year_of_foundation':year_of_foundation,'contact_number':contact_number,'username':username,'email':email,'password1':password1} 
            reg1 = [name_of_org,year_of_foundation,contact_number,username,email,password1]

            if password1 == password2:
                if User.objects.filter(username=username).exists(): 
                    messages.error(request,"Username already exists")
                    return render(request, "Admin/admin_register.html")

                # elif  User.objects.filter(email=email).exists():
                #     messages.error(request,"Email already exists")
                #     return render(request, "Admin/admin_register.html")
                # elif len(username)<0:
                #     messages.error(request,"Please Enter empty field")
                #     return render(request, "Admin/admin_register.html")
                # elif len(email)<0:
                #     messages.error(request,"Please enter empty field")
                #     return render(request, "Admin/admin_register.html")  
                # elif len(password1)<0:
                #     messages.error(request,"Please Enter empty field")
                #     return render(request, "Admin/admin_register.html")  
                # elif len(password2)<0:
                #     messages.error(request,"Please Enter empty field")
                #     return render(request, "Admin/admin_register.html")        

                else:  
                        # digits="0123456789"
                        # OTP=""
                        # for i in range(6):
                        #     OTP+=digits[math.floor(random.random()*10)]
                        # otp = OTP + " is your OTP"
                        # msg= otp
                        # s = smtplib.SMTP('smtp.gmail.com', 587)
                        # s.starttls()
                        # s.login('daspriyank000@gmail.com', 'rrdvendfboltlmov')
                        # s.sendmail('daspriyank000@gmail.com', email, msg)
                        # reg = {'name_of_org':name_of_org, 'year_of_foundation':year_of_foundation,'contact_number':contact_number,'username':username,'email':email,'password1':password1, 'otp':otp} 
                        return otp(request, reg1)


                    # user = User.objects.create_user(username = username,email= email, password= password1)
                    # register2 = admin_registration(name_of_org= name_of_org,year_of_foundation= year_of_foundation, contact_number= contact_number,username=username, email=email, user=user)
                    # register2.save()
                    #return redirect('signin')
                
            else:
                messages.error(request,"Password does not match")
                return render(request,"Admin/admin_register.html")
            
        return render(request,"Admin/admin_register.html")

def signin(request):
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password1 = postData.get('psw')
        user = authenticate(username= username, password= password1) 
        print(username)  
        print(password1)
        print(user)              
        if user is not None:
            login(request, user)
            return redirect('home')    #enters into dashboard page             
        else:
            messages.error(request,"Invalid username or password!")
            return render(request, "login.html") 
    else:
        #messages.error(request,"Please enter the fields")       
        return render(request, "login.html")

def signout(request):
    logout(request)
    return redirect('index')



        #check for validity

    #     if (not name):
    #         messages.error(request,"Required name")
    #     elif len(name)<= 4:
    #         messages.error(request,"Name should be greater than equal to 10")
    #     elif not email:
    #         messages.error(request,"Required email") 
    #     elif len(email)<6:
    #         messages.error(request,"Required email length more than 6")    
    #     elif (not password1):   
    #         messages.error(request,"Required first password") 
    #     elif (not password2):   
    #         messages.error(request,"Required second password") 
    #     elif  password1!= password2:   
    #         messages.error("Entered password does not matches")   
    #     elif User.objects.filter(name = self.cleaned_data['name'], email = self.cleaned_data ['email']).exists:
    #         messages.error(request,"Already exists")
    #    # check if previously registered with same creds or not
       
    #     if not messages:
    #         register = userRegistration(name, email, password1, password2)
    #         register.save()
        
    #     return render('login', register)

    # else:
           
        
