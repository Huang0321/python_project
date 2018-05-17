from uauth.models import Users
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 统一验证登录
            # 符合条件的 return none 或 不写return
        if request.path == '/uauth/dj_login/':
            return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/uauth/dj_login/')
        users = Users.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/uauth/dj_login/')

        给request中的user赋值
        request.user = users[0]


