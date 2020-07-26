class PageNumberPagination(pagination.PageNumberPagination):
  """查第n页，每页显示n条数据
    可在试图内通过pagination_class类属性指定私有分页器
  """
  page_size = 1 # 指定每页显示多少条数据
  page_size_query_param = 'size' # URL参数中每页显示条数的参数
  page_query_param = 'page' # URL中页码的参数
  max_page_size = None # 每页最多显示多少条数据