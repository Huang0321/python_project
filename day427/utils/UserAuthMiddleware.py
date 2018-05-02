from uauth.models import Users
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 统一验证登录
            # 符合条件的 return none 或 不写return
        if request.path == '/uauth/login/':
            return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/uauth/login/')
        users = Users.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/uauth/login/')

        request.user = users[0]