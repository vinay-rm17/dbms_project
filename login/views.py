from django.shortcuts import render
import mysql.connector as sql

em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd

    if request.method=="POST":
        n=sql.connect(host="localhost",user="root",password="W7301@jqir#",database="bus")
        cursor=n.cursor()
        d=request.POST
        for key,value in d.items():
            
            if key=="email":
                em=value
            if key=="password":
                pwd=value

        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'dbms1.html')
    return render(request,"login_page.html")