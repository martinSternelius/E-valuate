from django.http import HttpResponseRedirect

class UrlAccessRestrictions:
    def process_request(self, request):
        if not request.user.is_authenticated() and request.path != "/login/":
            return HttpResponseRedirect("/login/")
