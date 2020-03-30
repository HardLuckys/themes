from django.core.mail import send_mail
from .user_veref import get_code
from django.conf import settings
from .models import CustomUser, MyUserModel
from datetime import datetime, timedelta


def signup_back(request):
    try:
        url = get_code()
        code_user = CustomUser.objects.get(slug=request.user.slug)
        code_create_time = datetime.now().strftime('%Y/-%m/-%d/ %H:%M:%S.%f') #float(datetime.now().strftime("%H.%M"))
        code = MyUserModel(url=url, code_user=code_user, code_create_time=code_create_time)
        code.save()
        response = MyUserModel.objects.get(code_user=code_user).url
        user_email = request.user.email
        user_username = request.user.username
        send_mail(
            'Подтверждение на hardls.com',
            f'Ваш код: {response} , уважаемый {user_username}. Введите его пожалйуста на http://127.0.0.1:8000/code',
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False
        )
        return True
    except:
        return False


def time_code(request):
    try:
        code_time = MyUserModel.objects.get(code_user=request.user).code_create_time
        then = datetime.strptime(code_time, '%Y/-%m/-%d/ %H:%M:%S.%f')
        now = datetime.now()
        degree = datetime.strptime(str(now - then), '%H:%M:%S.%f')
        if degree > datetime.strptime('0:01:00.000000', '%H:%M:%S.%f'):
            MyUserModel.objects.get(code_user=request.user).delete()
            return False
        else:
            return True
    except:
        return False


def get_degree(request):
    code_time = MyUserModel.objects.get(code_user=request.user).code_create_time
    then = datetime.strptime(code_time, '%Y/-%m/-%d/ %H:%M:%S.%f')
    degree = 'Годен до: ' + str(then + timedelta(minutes=1))
    return degree
