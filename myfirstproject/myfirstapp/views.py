from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Avg,Count,Max,Min,fields,F
from datetime import datetime
import time

# Create your views here.








# library management system ----------------------------------------------------------------------------------------------------------------


def lib(requests):                                    #---------- to open the library 
    return render(requests,'lib.html') 

@login_required(login_url='/userlogin')
def addbook(request):                              #----- to add books
    data=dict(request.GET)
    b_id=int(data['b_id'][0])
    b_name=data['b_name'][0]
    subject=data['subject'][0]
    description=data['description'][0]
    semester=int(data['semester'][0])
    quantity=int(data['quantity'][0])
    price=int(data['price'][0])
    row=models.books(b_id,b_name,subject,description,semester,quantity,price)
    row.save()

    return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">BOOK ADDED<span style="color:green;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> ! SUCCESSFULLY !</span> </h1>')



@login_required(login_url='/userlogin')
def updatebook(request):    #--------------- to update books
    data=dict(request.GET)
    nb_id=int(data['nb_id'][0])
    nb_name=data['nb_name'][0]
    nsubject=data['nsubject'][0]
    ndescription=data['ndescription'][0]
    nsemester=int(data['nsemester'][0])
    nquantity=int(data['nquantity'][0])
    nprice=int(data['nprice'][0])
    models.books.objects.filter(b_id=nb_id).update(b_id=nb_id,b_name=nb_name,subject=nsubject,description=ndescription,semester=nsemester,quantity=nquantity,price=nprice)
    return redirect('/seeallbooks')
    

@login_required(login_url='/userlogin')
def seeallbooks(request):                 #-----------------to see all books
    data=list(models.books.objects.all().values())
    return render(request,'seeallbooks.html',{'books':data})

@login_required(login_url='/userlogin')
def deletebook(request):        #----------delete book
    data=dict(request.GET)
    nb_id=int(data['nb_id'][0])                    
    models.books.objects.filter(b_id=nb_id).delete()
    return redirect('/seeallbooks')
   

    

@login_required(login_url='/userlogin')
def addmember(request):                              #----- to add member
    data=dict(request.GET)
    m_id=int(data['m_id'][0])
    m_name=data['m_name'][0]
    mobile_no=int(data['mobile_no'][0])
    semester=int(data['semester'][0]) 
    branch=data['branch'][0]
    row=models.members(m_id,m_name,mobile_no,semester,branch)
    row.save()

    return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">MEMBER ADDED<span style="color:green;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> ! SUCCESSFULLY !</span> </h1>')


@login_required(login_url='/userlogin')
def updatemember(request):    #--------------- to update members
    data=dict(request.GET)
    nm_id=int(data['nm_id'][0])
    nm_name=data['nm_name'][0]
    nmobile_no=int(data['nmobile_no'][0])
    nsemester=int(data['nsemester'][0]) 
    nbranch=data['nbranch'][0]
    models.members.objects.filter(m_id=nm_id).update(m_id=nm_id,m_name=nm_name,mobile_no=nmobile_no,semester=nsemester,branch=nbranch)
    return redirect('/seeallmembers')
    


@login_required(login_url='/userlogin')
def seeallmembers(request):                 #-----------------to see all members
    data=list(models.members.objects.all().values())
    return render(request,'seeallmembers.html',{'members':data})

@login_required(login_url='/userlogin')
def deletemember(request):        #----------delete members
    data=dict(request.GET)
    nm_id=int(data['nm_id'][0])                    
    models.members.objects.filter(m_id=nm_id).delete()
    return redirect('/seeallmembers')


@login_required(login_url='/userlogin')
def addrecord(request):                              #----- to add record
    try:  
            data=dict(request.GET)
            r_id=int(data['r_id'][0])
            m_id=int(data['m_id'][0])
            m_name=data['m_name'][0]
            nb_id=int(data['nb_id'][0])
            b_name=data['b_name'][0]
            issue_date=data['issue_date'][0]
            return_date=data['return_date'][0]
            status=data['status'][0]


            if return_date>issue_date:
              
              row=models.records(r_id,m_id,m_name,nb_id,b_name,issue_date,return_date,status)
              row.save()
              models.books.objects.filter(b_id=nb_id).update(quantity=F('quantity') - 1)
              return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">RECORD ADDED<span style="color:green;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> ! SUCCESSFULLY !</span> </h1>')
            else:
              return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">RETURN DATE IS LESS THEN ISSUE DATE ,RECORD ADD<span style="color:red;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> !UNSUCCESSFUL!</span> </h1>')
    except:
        
        return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">CONSTRAINT DID NOT MATCH,RECORD ADD <span style="color:red;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> !! UNSUCCESSFUL !!</span> </h1>')

@login_required(login_url='/userlogin')
def updaterecord(request):    #--------------- to update members
    data=dict(request.GET)
    nr_id=int(data['nr_id'][0])
    nm_id=int(data['nm_id'][0])  #---- no need
    nm_name=data['nm_name'][0]
    nb_id=int(data['nb_id'][0])   #---- no need
    nb_name=data['nb_name'][0]
    nissue_date=data['nissue_date'][0]
    nreturn_date=data['nreturn_date'][0]
    nstatus=data['nstatus'][0]
    
    if nreturn_date>nissue_date:
        if nstatus=='RETURNED':
            models.books.objects.filter(b_id=nb_id).update(quantity=F('quantity') + 1)
            models.records.objects.filter(r_id=nr_id).update(m_name=nm_name,b_name=nb_name,issue_date=nissue_date,return_date=nreturn_date,status=nstatus)
            return redirect('/seeallrecords') 
        else:
            models.records.objects.filter(r_id=nr_id).update(m_name=nm_name,b_name=nb_name,issue_date=nissue_date,return_date=nreturn_date,status=nstatus)
            return redirect('/seeallrecords')    
    else:
        return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">RETURN DATE IS LESS THEN ISSUE DATE ,RECORD UPDATE<span style="color:red;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> !UNSUCCESSFUL!</span> </h1>')



@login_required(login_url='/userlogin')
def seeallrecords(request):                 #-----------------to see all record

    data=list(models.records.objects.all().values())

    date1=models.records.objects.values('issue_date')  #------------- to select a single coulmn
    # print(type(date1[0]))
    # date2=data[0]['issue_date'].strftime("%Y-%m-%d")         #  ------ sirs logic
    # print(type(date2))
    # for i in data:
    #     a=data[0]['issue_date'].strftime("%Y-%m-%d")
    #     print(list(i))
    # # print(data)
    # print(date1)
     
    return render(request,'seeallrecords.html',{'records':data})

@login_required(login_url='/userlogin')
def seesearchrecords(request):                 #-----------------to see search record
    data=dict(request.GET)
    nb_id=int(data['nb_id'][0])
    data=list(models.records.objects.filter(b_id=nb_id).values())
    return render(request,'seeallrecords.html',{'records':data})

@login_required(login_url='/userlogin')
def deleterecord(request):        #----------delete members
    data=dict(request.GET)
    nr_id=int(data['nr_id'][0])                    
    models.records.objects.filter(r_id=nr_id).delete()
    return redirect('/seeallrecords')




#--------------------- authentication and authorization ------------------------


def usersignup(request):
    signupform = UserCreationForm()
    return render(request,'signup.html',{'signupform':signupform})


def handlesignup(request):
    data=request.POST
    user = UserCreationForm(data)

    if user.is_valid():
        user.save()
        return redirect('/userlogin')
    else:
        return redirect('/usersignup')

def userlogin(request):
    return render(request,'login.html')

    
def handlelogin(request):
    data = request.POST
    username = data['username']
    password = data['password']

    user = authenticate(request=request,username=username,password=password)

    if user:
        login(request,user)
        return redirect('/lib')
    else:
        return redirect('/userlogin')
    
def userlogout(request):
    logout(request)

    return HttpResponse('<h1  style="color:blue;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;">LOGGED OUT<span style="color:green;text-shadow: 0 0 20px black,0 0 40px black,0 0 80px black;"> ! SUCCESSFULLY !</span> </h1>')



  #--------------------- rough work
     #     date3=[i][0].strftime("%Y-%m-%d")  
