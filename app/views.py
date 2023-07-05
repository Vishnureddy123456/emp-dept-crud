from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def dep(request):
    if request.method=='POST':
        dn=request.POST['dn']
        dname=request.POST['dname']
        lo=request.POST['loc']
        DN=Dept.objects.get_or_create(deptno=dn,dname=dname,loc=lo)[0]
        DN.save()
        return HttpResponse('data is submitted')
    return render(request,'dep.html')
def employ(request):
    LDO=Dept.objects.all()
    d={'LDO':LDO}
    if request.method=='POST':
        dn=request.POST['dn']
        en=request.POST['name']
        job=request.POST['job']
        mgr=request.POST['mgr']
        hiredate=request.POST['hiredate']
        sal=request.POST['sal']
        comm=request.POST['comm']
        DN=Dept.objects.get(deptno=dn)
        EMP=Emp.objects.get_or_create(deptno=dn,ename=en,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm)[0]
        EMP.save()
        return HttpResponse('data is submitted')
    return render(request,'employ.html',d)
