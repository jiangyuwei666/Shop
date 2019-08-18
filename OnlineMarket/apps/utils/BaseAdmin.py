from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    list_display_links = ["id"]
    list_per_page = 5  # 分页，每页数据
    search_fields = ["name"]  # 设置可以搜索的字段
