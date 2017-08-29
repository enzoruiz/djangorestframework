from rest_framework.pagination import (
    LimitOffsetPagination, PageNumberPagination
)


class PeliculaLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class PeliculaPageNumberPagination(PageNumberPagination):
    page_size = 2
