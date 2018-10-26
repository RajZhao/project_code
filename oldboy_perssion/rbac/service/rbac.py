from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class ValidPermission(MiddlewareMixin):
    def process_request(self,request):
        pass
