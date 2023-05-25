from rest_framework.pagination import PageNumberPagination


class LimitPageNumberPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'limit'


class LimitPageFollowNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'recipes_limit'
