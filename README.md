# pagination
自定义django分页组件

# 核心用法

```python
def publisher_list(request):
    # 从URL中取当前访问的页码数
    current_page = int(request.GET.get('page'))
    # 比len(models.Publisher.objects.all())更高效
    total_count = models.Publisher.objects.count()
    
    # 获取分页对象
    # =========================================================================
    # Pagination(current_page, total_count, base_url, per_page=10, max_show=11)
    # current_page: 当前请求的页码
    # total_count: 总数据量
    # base_url: 请求的URL
    # per_page: 每页显示的数据量，默认值为10
    # max_show: 页面上最多显示多少个页码，默认值为11
    # =========================================================================
    page_obj = Pagination(current_page, total_count, request.path_info)
    
    # =============================================
    # page_obj.start 和 page_obj.end 确定记录数据范围
    # =============================================
    data = models.Publisher.objects.all()[page_obj.start:page_obj.end]
    
    # =============================================
    # page_obj.page_html() 生成html代码
    # =============================================
    page_html = page_obj.page_html()
    
    return render(request, "publisher_list.html", {"publisher_list": data, "page_html": page_html})
```
