from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from .models import Users,Stock,Query
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random,csv


# Create your views here.
# Home page
def index(request):
    welcome=(request.session.get("name"))
    return render(request,"index.html",{"welcome":welcome})

# views for signup
def signup(request):
    validate=request.session.get("name")
    if not validate:
        if request.method=="POST":
            usermail=request.POST.get("usermail")
            name=request.POST.get("name")
            password=request.POST.get("password")
            request.session["email"] = usermail      
            Users(name=name,email=usermail,password=password).save()
            request.session["name"] = name     
            return redirect("/login")    
        return render(request, "signup.html")
    else:
        return redirect("/stocks")

# function for generating otp
def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

# views for sending otp
def send_otp(request):
    if request.method=="POST":
        email=request.POST.get("email")
        print(email)
        if Users.objects.filter(email=email).exists():       
            return HttpResponse("")
            
        else:
            o=generateOTP()
            print(o)
            htmlgen = "<p> Your OTP is </p>"  +  " " "<strong>" + str(o)  + "</strong>"
            send_mail('E-mail verification',o,'xyz@gmail.com',[email], fail_silently=False, html_message=htmlgen)
            return HttpResponse(o)
 

# views for login form
def login(request):
    validate=request.session.get("name")
    if not validate:
     if request.method=="POST":
        request.session.clear()      
        usermail=request.POST.get("usermail")
        password=request.POST.get("password")
        filter_data=Users.objects.filter(email=usermail,password=password)
        if filter_data.exists():
            request.session["email"] = usermail
            for i in filter_data:
                request.session["name"] = i.name
            
            return redirect("/stocks")
        else:
            return render(request,"login.html",{"alert_redirect":"Invalid Email or Password"})
     else:
         return render(request,"login.html",{"alert_redirect":"Please Login Here"})
    else:
        return redirect("/stocks")
 
#  views for logout
def logout(request):
    validate=request.session.get("name")
    if validate:
        request.session.clear()
        return redirect("/login")
    else:
        return redirect("/login")
        
# views for stocks_list
def stocks(request): 
    validate=request.session.get("name")
    if validate:
        total_data=Stock.objects.count()
        data=Stock.objects.all()[:5]
        return render(request,"stocks.html",{"data":data,"total_data":total_data,"validate":validate})
    else:
        return render(request,"login.html",{"alert_redirect":"Please login to continue"})
# views for loading more stock data
def load_data(request):
    if request.session.get("name"):
        offset=int(request.GET["offset"])
        print("offset",offset)
        limit=int(request.GET["limit"])
        print("limit",limit)
        data=Stock.objects.all()[offset:offset+limit]  
        convert=render_to_string("load_data.html",{"data":data,"offset":offset})
        return JsonResponse({"data":convert})
    else:
         return render(request,"login.html",{"alert_redirect":"Please login to continue"})
    
# views for submitting query form

def query(request,id):
    validate=request.session.get("name")
    if validate:
        if request.method=='POST':
            usermail=request.session.get("email")
            if usermail:
                query=request.POST.get("query")
                # about=request.POST.get("about")
                user=Users.objects.get(email=usermail)
                stock_id=Stock.objects.filter(id=id)
                if stock_id:
                    for i in stock_id:
                        req_stock=i.symbol
                    a=Query.objects.create(name=user,query=query,user=validate,stock_regarding=req_stock)
                    a.save()    
                return render(request,"query.html",{"validate":validate,"success":"Query form has been submitted successfully"})
                
        return render(request,"query.html",{"validate":validate,"id":id})
    else:
         return render(request,"login.html",{"alert_redirect":"Please login to continue"})
        
        
# views for searching functionality
def search(request):
    validate=request.session.get("name")
    data=Stock.objects.all()[:5]
    if validate:
        query=request.GET.get("search")
        if query=="":
            return redirect("/stocks")
        else:
            stock_search=Stock.objects.filter(name__icontains=query)
            if stock_search:   
                return render(request,"stocks.html",{"data":stock_search,"validate":validate})
            else:
                return render(request,"stocks.html",{"data":data,"validate":validate,"msg":"notfound"})
            
            
    else:
        return render(request,"login.html",{"alert_redirect":"Please login to continue"})
    
# views for stock description using slug
def details(request,slug):
    validate=request.session.get("name")
    if validate:
        fetch_data=Stock.objects.filter(slug=slug)
        if request.method=="GET":
            if fetch_data: 
                return render(request,"details.html",{"data":fetch_data,"validate":validate})
            else:
                return redirect("/stocks")
    else:
        return redirect("/login")
        
# view for exporting form to excel or csv   
def export(request):
     validate=request.session.get("name")
     if validate:
         if request.user.is_superuser:
            response=HttpResponse(content_type="text/csv")
            writer=csv.writer(response)
            writer.writerow(["UserId","Users","Queries Regarding Stocks","Queries"])
            obj=Query.objects.all().values_list("name","user","stock_regarding","query")
            for query in obj:
                writer.writerow(query)
            response['Content-Disposition']='attachment;filename="User_Query.csv"'
            return response
         else:
             return render(request,"query.html",{"validate":validate,"success":"Sorry only admin have rights to export"})
     else:
        return render(request,"login.html",{"alert_redirect":"Please login to continue"})
         
         
def admin(request):
     validate=request.session.get("name")
     if validate:
         if not request.user.is_superuser:
             return HttpResponse("<h1>Page Not Found </h1>")
     else:
         return render(request,"login.html",{"alert_redirect":"Please login to continue"})
         
      
        
             

    
    
    
    
            
        

