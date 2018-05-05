from django.utils.deprecation import MiddlewareMixin
from stu.models import Visit

import logging


logger = logging.getLogger('auth')


class VisitTimes(MiddlewareMixin):

    def process_request(self, request):

        path = request.path

        # get 如果得到的是空或者多个对象，将会报错
        # 所以此处用try 进行错误处理
        try:
            visit = Visit.objects.get(v_url=path)
            if visit:
                visit.v_times += 1
                visit.save()
        except Exception as e:
            logger.error(e)
            print(e)
            Visit.objects.create(v_url=path, v_times=1)
