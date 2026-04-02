from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken  # Import RefreshToken directly
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer

class LoginSerializer(serializers.Serializer):
    """
    Custom serializer for login with username or email
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        username_value = attrs.get('username')
        password_value = attrs.get('password')
        
        if username_value and password_value:
            # Try to find user by username first
            try:
                user_obj = User.objects.get(username=username_value)
                email_value = user_obj.email
            except User.DoesNotExist:
                # Try email directly
                try:
                    user_obj = User.objects.get(email=username_value)
                    email_value = user_obj.email
                except User.DoesNotExist:
                    raise serializers.ValidationError('Invalid credentials')
            
            # Authenticate with email
            user = authenticate(self.context['request'], email=email_value, password=password_value)
            
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        
        raise serializers.ValidationError('Must include "username" and "password".')

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
