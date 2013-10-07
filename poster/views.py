# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.context import RequestContext
from logging import warning


def sign_up(request):
    return render_to_response('signup.html',
                              context_instance=RequestContext(request))


def create_user(request):
    def res(*args):
        return render_to_response(*args,
                                  context_instance=RequestContext(request))
    
    warning('called create_user')
    post = request.POST
    username = post['username']
    email = post['email']
    password = post['password']
    password2 = post['password2']
    
    if not (username or email or password or password2):
        warning('KeyError')
        # 入力必須項目が抜けている
        return res('signup.html', {'empty_request': True})
    
    if username in [u.username for u in User.objects.all()]:
        warning('Duplicate User Name')
        # ユーザー名が被っている
        return res('signup.html', {'double_username': True})
    
    if password != password2:
        warning('Invalid Password')
        # パスワードが一致しない
        return res('signup.html', {'miss_password': True})
    
    warning('Pass the checks')
    # チェックを通ったのでアカウント作成
    new_user = User.objects.create_user(username, email, password)
    try:  # 追加情報の設定
        new_user.first_name = post['first_name']
        new_user.last_name = post['family_name']
    except KeyError:
        pass  # No problem.
    new_user.save()
    
    # ログインさせる
    user = authenticate(username=username, password=password)
    login(request, user)
    return render_to_response('headline.html', {'user': user})
