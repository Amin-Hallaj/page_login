from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import login , authenticate , logout 
from django.contrib import messages


def master_index(request):

    return render(request , 'master/index.html', {})


def master_login(request):

    return render(request , 'master/login.html', {})


def master_login_submit(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username , password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f"{username} خوش اومدین.")
            return redirect('master_index')

        else:
            messages.error(request,'نام کاربری یا رمز عبور اشتباه میباشد.')
    
    return redirect("master_login")


def master_logout(request):

    logout(request)
    return redirect("master_login")


def operator_login(request ):
            
    return render(request , 'operator/login.html', {})


def operator_login_submit(request):

    if request.method == "POST":
        username=request.POST.get('national_id')
        member_pass=request.POST.get('member_pass')
        user=authenticate(username=username, password=member_pass)

        if user is not None:
            login(request , user)
            messages.success(request, f"{request.user.user_members} خوش اومدین.")
            return redirect("operator_panel")

        else:
            messages.error(request,"نام کاربری یا رمز عبور نامعتبر است.")
            return redirect("operator_login")
        
    return redirect("operator_login" )


def operator_logout(request):

    logout(request)
    return redirect("operator_login")