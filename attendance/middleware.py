from django.shortcuts import redirect
from django.conf import settings
from django.db import connection
from django.template import Template, Context
from ipware.ip import get_client_ip
from accounts.models import User

class IpCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        
        
        # ip 확인
        ip = get_client_ip(request)
        ip=ip[0]
        print("IP = ", ip)
        try:
            user = User.objects.get(id=request.user.id)
            user.ip = ip
            user.save()
        except Exception as e:
            print("IP ERROR", e)


        return response