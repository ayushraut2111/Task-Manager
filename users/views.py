from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserAuthSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout

class AuthViewset(GenericViewSet):
    serializer_class = UserAuthSerializer
    @action(detail=False,url_path='register',methods=['post'],permission_classes=[AllowAny])
    def register_user_api(self,request):
        data=request.data

        username=data.get("username",None)
        password=data.get("password",None)

        if not (username and password):
            return Response({"message":"Username and password both are required"},status=400)
        
        serializer=UserAuthSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message":"User is registered"},status=200)
    
    @action(detail=False, url_path='login',methods=['post'],permission_classes=[AllowAny])
    def login_user_api(self,request):
        data = request.data

        username = data.get("username", None)
        password = data.get("password", None)


        if not (username and password):
            return Response({"message": "Username and password both are required"},status=400)

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"message": "Invalid credentials"}, status=400)

        login(request, user)

        return Response({"message": "Login successful"}, status=200)
    
    @action(detail=False,url_path='logout',methods=['post'])
    def logout_user_api(self,request):
        logout(request)
        return Response({"message":"User logged out successfully"},status=200)
