
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .serializers import userAuthSerializers

class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userAuthSerializers

    def create(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        cpassword = request.data.get('cpassword')

        if password != cpassword:
            return Response({"error": "password mismatch"})

        existing_email = User.objects.filter(email=email).exists()
        existing_username = User.objects.filter(username=username).exists()

        # Check duplicate values
        if existing_username:
            return Response({"username_error": "User with this username already exists"})
        if existing_email:
            return Response({"email_error": "User with this email already exists"})

        user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)

        # Generate a token for the user and associate it with their account
        token, created = Token.objects.get_or_create(user=user)

        serializer = self.get_serializer(user)
        return Response({
            "success": "User created successfully",
            "token": token.key,
            "user_data": serializer.data,
        })



class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        # Perform user authentication
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        # print(user)

        if user is not None:
            # Log the user in
            login(request, user)

            # Generate a new token for the user
            # token, created = Token.objects.get_or_create(user=user)

            # Return the user data and token in the response
            serializer = userAuthSerializers(user)

            return Response({
                # 'token': token.key,
                'user_data': serializer.data,
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
