from django.contrib import admin

# Register your models here.
from stu.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    def set_sex(self):
        if self.sex:
            return '男'
        else:
            return '女'

    # 修改性别字段的描述

    set_sex.short_description = "性别"

    # 展示字段
    list_display = ["id", 'name', set_sex]

    # 过滤
    list_filter = ['name']

    # 搜索
    search_fields = ['name']

    # 分页
    list_per_page = 4


# admin.site.register(Student, StudentAdmin)

# 1.注册启动 第一种方式
# admin.site.register(Student, StudentAdmin)
# 2. 装饰器方式
# @admin.register(Student)
