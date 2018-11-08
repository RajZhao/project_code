from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class ValidPermission(MiddlewareMixin):
    def process_request(self,request):
        current_path = request.path_info

        valid_url_list = ["/login/","/reg/","/admin/.*"]
        for valid_url in valid_url_list:
            pass
