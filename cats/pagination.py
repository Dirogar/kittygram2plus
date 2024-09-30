from rest_framework import pagination

class CatsPagination(pagination.BasePagination):
    page_size = 20