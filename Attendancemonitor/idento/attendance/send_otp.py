
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('daspriyank000@gmail.com', 'rrdvendfboltlmov')
emailid = input("Enter your email: ")
s.sendmail('daspriyank000@gmail.com',emailid, msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
    # message.success(request, "OTP has been sent successfully")
    # return redirect(request,"home.html")
else:
    print("Please Check your OTP again")
    # message.error(request,"Invalid otp. Please send again")
    # return render(request, "signin.html")
s.quit()