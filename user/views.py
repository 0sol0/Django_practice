from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model 
from django.http import HttpResponse
from .models import UserModel

# user/views.py

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html') # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in') # 회원가입이 완료되었으므로 로그인 페이지로 이동       return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)
        if me.password == password: 
            request.session['user'] = me.username
            return HttpResponse("로그인 성공!")
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')