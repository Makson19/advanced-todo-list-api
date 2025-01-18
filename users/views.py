from rest_framework import status, generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import UserProfile
from users.serializers import UserProfileSerializer, PasswordResetSerializer, ChangePasswordSerializer


# Register user
class RegisterUserView(generics.CreateAPIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        if UserProfile.objects.filter(email=request.data['email']).exists():
            return Response({ 'error': 'Email already resgistered' }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# GET and UPDATE user
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        user = UserProfile.objects.get(id=request.user.pk)
        user.name = request.data['name']
        user.birthday = request.data['birthday']
        user.gender = request.data['gender']
        user.save()
        return Response({ 'message': 'User updated successfuly' }, status=status.HTTP_200_OK)
    

# GET all users
class AllUsersView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


# Reset password
class PasswordResetView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer
    model = UserProfile

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']
            user = UserProfile.objects.filter(email=email).first()

            if user:
                user.set_password(new_password)
                user.save()
                return Response({ 'message': 'Password reset successfuly' }, status=status.HTTP_200_OK)
            return Response({ 'message': 'User with this email does not exist.' }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update password
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserProfile
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not self.user.check_password(serializer.validated_data['old_password']):
                return Response({ "old_password": "Wrong password." }, status=400) 

            self.user.set_password(serializer.validated_data['new_password']) 
            self.user.save()
            return Response({ 'message': 'Password updated successfully' }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
