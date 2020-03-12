class Pagination(object):
    """自定义分页（Bootstrap版）"""

    def __init__(self, current_page, total_count, base_url, per_page=10, max_show=11):
        """
        :param current_page: 当前请求的页码
        :param total_count: 总数据量
        :param base_url: 请求的URL
        :param per_page: 每页显示的数据量，默认值为10
        :param max_show: 页面上最多显示多少个页码，默认值为11
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            # 取不到或者页码数不是数字都默认展示第1页
            self.current_page = 1
        # 定义每页显示多少条数据
        self.per_page = per_page
        # 计算出总页码数
        total_page, more = divmod(total_count, per_page)
        if more:
            total_page += 1
        self.total_page = total_page
        # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
        self.max_show = max_show
        self.half_show = max_show // 2
        self.base_url = base_url

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    def page_html(self):
        # 计算一下页面显示的页码范围
        if self.total_page <= self.max_show:  # 总页码数小于最大显示页码数
            page_start = 1
            page_end = self.total_page
        elif self.current_page + self.half_show >= self.total_page:  # 右边越界
            page_end = self.total_page
            page_start = self.total_page - self.max_show
        elif self.current_page - self.half_show <= 1:  # 左边越界
            page_start = 1
            page_end = self.max_show
        else:  # 正常页码区间
            page_start = self.current_page - self.half_show
            page_end = self.current_page + self.half_show
        # 生成页面上显示的页码
        page_html_list = []
        page_html_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
        # 加首页
        first_li = '<li><a href="{}?page=1">首页</a></li>'.format(self.base_url)
        page_html_list.append(first_li)
        # 加上一页
        if self.current_page == 1:
            prev_li = '<li><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'
        else:
            prev_li = '<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                self.base_url, self.current_page - 1)
        page_html_list.append(prev_li)
        for i in range(page_start, page_end + 1):
            if i == self.current_page:
                li_tag = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
            else:
                li_tag = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
            page_html_list.append(li_tag)
        # 加下一页
        if self.current_page == self.total_page:
            next_li = '<li><a href="#"><span aria-hidden="true">&raquo;</span></a></li>'
        else:
            next_li = '<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.base_url, self.current_page + 1)
        page_html_list.append(next_li)
        # 加尾页
        page_end_li = '<li><a href="{}?page={}">尾页</a></li>'.format(self.base_url, self.total_page)
        page_html_list.append(page_end_li)
        page_html_list.append('</ul></nav>')
        return "".join(page_html_list)
