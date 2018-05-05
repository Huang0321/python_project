
import django_filters
from rest_framework import filters

from stu.models import Student


class StuFilter(filters.FilterSet):

    name = django_filters.CharFilter('s_name', lookup_expr='icontains') # contains 模糊搜索 i 忽略大小写
    tel = django_filters.CharFilter('s_tel')
    yuwen = django_filters.CharFilter('s_yuwen')
    # 过滤操作时间大于某些时间的学生
    l_operate = django_filters.DateTimeFilter('S_operate_time', lookup_expr='lte')
    # 过滤操作时间小于某些时间的学生
    g_operate = django_filters.DateTimeFilter('S_operate_time', lookup_expr='gte')
    # 过滤学生的状态
    status = django_filters.CharFilter('s_status')
    # 过滤语文成绩小于某些分数的学生
    yu = django_filters.CharFilter('s_yuwen', lookup_expr='lt')
    # 过滤语文成绩大于某些分数的学生
    wen = django_filters.CharFilter('s_yuwen', lookup_expr='gt')

    class Meta:
        model = Student
        # 现在这个版本 括号里可写可不写,低版本就必须写
        # fileds = [] 也是可以的
        fields = ['s_yuwen', 's_status', 'S_operate_time', 's_tel', 's_name']