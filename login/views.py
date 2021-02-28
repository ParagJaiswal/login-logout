from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Users,Res

def index(request):
	if request.method =='POST':
		r = Users(username=request.POST['txtusername'],password=request.POST['txtpass'],email=request.POST['txtemail'],mobile=request.POST['txtmobile'])
		chkemail = Users.objects.filter(email = request.POST['txtemail'])
		if chkemail.count()==0:			
			r.save()
			return redirect('login')
		else:
			
			return render(request,'login/form.html',{'key':"Email already exist"})

	return render(request,'login/form.html')


def login(request):
	if request.method=='POST':
		c = Users.objects.filter(username=request.POST['txtusername'])
		p1 = Users.objects.filter(password=request.POST['txtpassword'])
		
		if c.count()>0:
			p = Users.objects.filter(username=request.POST['txtusername'],password=request.POST['txtpassword'])
			if p.count()>0:
				request.session['uid']=request.POST['txtusername']			
				return redirect('dashboard')
			else:
				return render(request,'login/loginpage.html',{'invalid':'Password is not valid'})
		if p1.count()>0:
			c1 = Users.objects.filter(username=request.POST['txtusername'],password=request.POST['txtpassword'])
			if c1.count()>0:
				request.session['uid']=request.POST['txtusername']			
				return redirect('dashboard')
			else:
				return render(request,'login/loginpage.html',{'invalid':'Username is not valid'})
		else:
			return render(request,'login/loginpage.html',{'invalid':'Username and Password is not valid'})
	return render(request,'login/loginpage.html')

def dashboard(request):
	if request.session.has_key('uid'):
		ses = request.session['uid']
		info = Users.objects.filter(username=ses)
		return render(request,'login/dashboard.html',{'sesname':ses,'information':info})
	else:
		return redirect('login')

def logout(request):
	del request.session['uid']
	return redirect('login')

def resume(request):
	if request.method == 'POST':
		resinput = Res(first_name=request.POST['txtfname'],last_name=request.POST['txtlname'],city=request.POST['txtcity'],mobile=request.POST['txtmobile'],education=request.POST['txteducation'],fieldstudy=request.POST['txtstudy'],university=request.POST['txtcollege'],tpstartm=request.POST['startm'],tpstarty=request.POST['startyear'],tpendm=request.POST['endm'],tpendy=request.POST['endyear'],exptitle=request.POST['txtexp'],expcompany=request.POST['txtcompany'],expstartm=request.POST['expstartm'],expstarty=request.POST['expstartyear'],expendm=request.POST['expendm'],expendy=request.POST['expendyear'])
		resinput.save()

	return render(request,'login/resume.html')



