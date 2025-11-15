from rest_framework.authentication import SessionAuthentication

# for session authentication we are exempting csrf verification by creating a custom authentication and bypassing the csrf verification
class NoCSRFSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return