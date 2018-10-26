from django.http import HttpResponse
from django.shortcuts import render

from rbac.models import *


def users(request):
    user_list = user.objects.all()

    return render(request, "users.html", locals())


def add_user(request):
    permission_list = request.session["perlist"]
    current_path = request.path_info
    if current_path in permission_list:
        pass
    else:
        return HttpResponse("You have no permission")
    return HttpResponse("add user")


def roles(request):
    user_list = user.objects.all()

    return render(request, "users.html", locals())


def login(request):
    if request.method == "POST":

        username = request.POST.get("user")
        pwd = request.POST.get("pwd")
        use = user.objects.filter(name=username, pwd=pwd).first()
        print use
        if use:
            ret = use.roles.all().values("permissions__url").distinct()
            print ret

            permission_list = []

            for item in ret:
                permission_list.append(item["permissions__url"])
            print permission_list
            request.session["perlist"] = permission_list
            return HttpResponse("Login suceffuly")
    return render(request, "login.html")
