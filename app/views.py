from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import registerforms,authentication,superusers

from django.db.models import Count
from datetime import date
def dele(request,id):
    employe=registerforms.objects.filter(id=id)
    employe.delete()
    return redirect('old')
def old(request):
    v=registerforms.objects.all()[::-1]
    return render(request,"oldreports.html",{"i":v})
def back(request):
    v = registerforms.objects.values('Hospital_Name', 'Doctor_Appointment_Date').order_by(
        "Doctor_Appointment_Date").annotate(dcount=Count('Hospital_Name')).filter(
        Doctor_Appointment_Date__isnull=False).reverse()
    return render(request, 'numberofpatients.html', {"g": v})
def loginpage(request):
     return render(request, "rigistration.html")
def home(request):
    return render(request, "rigistration.html")
def login(request):
    return render(request, "login.html")
def today(request):
        password =request.session['password']
        startdate = date.today()
        v = registerforms.objects.filter(Hospital_Name=password,Doctor_Appointment_Date__isnull=False,Doctor_Appointment_Date=startdate)
        return render(request, "todaypatient.html",{"i":v,"password":password})
def index(request):
   if request.method == "POST":
       sub=request.POST.get('action')
       if sub == 'Save':
           return (Save(request))
       if sub=='login':
           return (lon(request))
       if sub == "Submit":
           return (dara(request))
       if sub=="fubmit":
           return (superuserd(request))
def edit(request,id):
    employee=registerforms.objects.get(id=id)
    return render(request,'update.html',{'employee':employee})
def update(request):
    id = request.POST.get('id')
    das = request.POST.get('dap')

    registerforms.objects.filter(id=id).update(Doctor_Appointment_Date=das)
    return redirect('today')
def dara(request):
    date=request.POST.get("dd")
    password=request.session['password']
    t = registerforms.objects.filter(Hospital_Name=password,Doctor_Appointment_Date=date)
    return render(request,"todaypatient.html",{"i":t,"password":password})
def Save(request):
            firstname=request.POST.get("fname")
            lastname=request.POST.get("lname")
            mobilenumber=request.POST.get("mobile")
            adharnumber=request.POST.get("adhar")
            dateofbirth=request.POST.get("dateofbirth")
            sex=request.POST.get("sex")
            hospitalname=request.POST.get("hospital")
            address=request.POST.get("address")
            request.session['firstname'] = firstname
            request.session['lastname'] = lastname
            request.session['mobilenumber'] = mobilenumber
            request.session['adharnumber'] = adharnumber
            request.session['sex'] = sex
            request.session['hospitalname'] = hospitalname
            request.session['address'] = address
            request.session['password'] = dateofbirth
            if (len(mobilenumber) == 10) and (len(adharnumber) == 12):
                    if hospitalname=="Kims Hospital,ongole":
                        hospitalname="KIMS"
                        user = registerforms(First_Name=firstname, Last_Name=lastname, Mobile_Number=mobilenumber,
                                             Adhar_Number=adharnumber, Date_Of_Birth=dateofbirth, Sex=sex,
                                             Hospital_Name=hospitalname, Address=address)
                        user.save()
                        return render(request, "patientsubmit.html", {"k": {user}})
                    else:
                        hospitalname = "NIMS"
                        user = registerforms(First_Name=firstname, Last_Name=lastname, Mobile_Number=mobilenumber,
                                             Adhar_Number=adharnumber, Date_Of_Birth=dateofbirth, Sex=sex,
                                             Hospital_Name=hospitalname, Address=address)
                        user.save()
                        return render(request, "patientsubmit.html", {"k": {user}})

            if hospitalname == 'KIMS':
                hospitals = "Kims Hospital,Ongole"
                request.session['hospitals'] = hospitals
            if hospitalname=="NIMS":
                hospitals = "Nims Hospital,Guntur"
                request.session['hospitals'] = hospitals

            if (len(mobilenumber) != 10 and len(adharnumber) != 12):
                error_message = "Mobile number should be 10 digits!"
                error_messages = "Adhar number should be 12 digits!"
                request.session['firstname'] = firstname
                request.session['lastname'] = lastname
                request.session['mobilenumber'] = mobilenumber
                request.session['adharnumber'] = adharnumber
                request.session['sex'] = sex
                request.session['hospitalname'] = hospitalname
                request.session['address'] = address
                request.session['dateofbirth'] = dateofbirth
                hospitals=request.session['hospitals']


                value = {
                    'firstname': firstname,
                    'lastname': lastname,
                    'mobilenumber': mobilenumber,
                    'adharnumber': adharnumber,
                    'dateofbirth': dateofbirth,
                    'address': address,
                    'hospitalnames': hospitals,

                    'sex': sex,
                    'error_message': error_message,
                    'error_messages':error_messages
                }
                return render(request, "rigistration.html", {'values': value})
            elif (len(mobilenumber) != 10):
                error_message = "Mobile number should be 10 digits!"
                request.session['firstname'] = firstname
                request.session['lastname'] = lastname
                request.session['mobilenumber'] = mobilenumber
                request.session['adharnumber'] = adharnumber
                request.session['sex'] = sex
                request.session['hospitalname'] = hospitalname
                request.session['address'] = address
                hospitals=request.session['hospitals']



                value = {
                    'firstname': firstname,
                    'lastname': lastname,
                    'mobilenumber': mobilenumber,
                    'adharnumber': adharnumber,
                    'dateofbirth': dateofbirth,
                    'address': address,
                    'hospitalnames': hospitals,

                    'sex': sex,
                    'error_message': error_message
                }
                return render(request, "rigistration.html", {'values': value})
            elif len(adharnumber) !=12 :
                    error_messages = "Adhar number should be 12 digits!"
                    request.session['firstname'] = firstname
                    request.session['lastname'] = lastname
                    request.session['mobilenumber'] = mobilenumber
                    request.session['adharnumber'] = adharnumber
                    request.session['sex'] = sex
                    request.session['hospitalname'] = hospitalname
                    request.session['address'] = address
                    request.session['dateofbirth'] = dateofbirth
                    hospitals = request.session['hospitals']


                    value = {
                        'firstname': firstname,
                        'lastname': lastname,
                        'mobilenumber': mobilenumber,
                        'adharnumber': adharnumber,
                        'dateofbirth': dateofbirth,
                        'address': address,
                        'hospitalnames': hospitals,

                        'sex': sex,
                        'error_messages': error_messages
                    }
                    return render(request, "rigistration.html", {'values': value})


def lon(request):
      username = request.POST.get('username')
      password = request.POST.get('password')
      request.session['username']=username
      request.session['password'] = password
      startdate = date.today()
      if (authentication.objects.filter(User_Name=username).exists()):
        if (authentication.objects.filter(Password=password).exists()):
          v = registerforms.objects.filter(Hospital_Name=password,Doctor_Appointment_Date__isnull=False,Doctor_Appointment_Date=startdate)
          return render(request, "todaypatient.html",{"i":v,"password":password})
        else:
          error_message = "Invalid Password!"
          return render(request, 'login.html', {'error_message': error_message,"username":username,"password":password})
      elif  (registerforms.objects.filter(Mobile_Number = username).exists()):
           if (registerforms.objects.filter(Adhar_Number=password).exists()):
                if (registerforms.objects.filter(Adhar_Number=password,Mobile_Number=username,Doctor_Appointment_Date__isnull=True).exists()):
                   v = registerforms.objects.filter(Adhar_Number=password,Mobile_Number=username,Doctor_Appointment_Date__isnull=True).last()
                   return render(request, 'statushtml.html',{"k":{v}})
                elif (registerforms.objects.filter(Adhar_Number=password,Mobile_Number=username,Doctor_Appointment_Date__isnull=False).exists()):
                       v = registerforms.objects.filter(Adhar_Number=password,Mobile_Number=username,Doctor_Appointment_Date__isnull=False).last()
                       print(v)
                       return render(request, 'statusupdate.html', {"k": {v}})
           else:
               error_message = "Invalid Password!"
               return render(request, 'login.html', {'error_message': error_message,"username":username,"password":password})
      elif (superusers.objects.filter(Username=username).exists()):
          if (superusers.objects.filter(Password=password).exists()):
               v=registerforms.objects.values('Hospital_Name','Doctor_Appointment_Date').order_by("Doctor_Appointment_Date").annotate(dcount=Count('Hospital_Name')).filter(Doctor_Appointment_Date__isnull=False).reverse()
               return render(request,'numberofpatients.html',{"g":v})
          else:
               error_message = "Invalid Password!"
          return render(request, 'login.html', {'error_message': error_message,"username":username,"password":password})
      else:
           error_message = "Invalid Username and Password!"
      return render(request,'login.html', {'error_message': error_message,"username":username,"password":password})
def newpatient(request):
    password = request.session['password']
    print(password)
    l = registerforms.objects.filter(Hospital_Name=password,Doctor_Appointment_Date__isnull=True)[::-1]
    return render(request, "DoctorAppointment.html",{"i":l,"password":password})
def superuserd(request):
    dats=request.POST.get("d")
    v = registerforms.objects.values('Hospital_Name','Doctor_Appointment_Date').order_by(
        "Doctor_Appointment_Date").annotate(dcount=Count('Hospital_Name')).filter(Doctor_Appointment_Date=dats)
    return render(request, 'numberofpatients.html', {"g": v})




