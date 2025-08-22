from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model  # ✅ FIXED import
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from notifications.utils import create_notification  # ✅ Ensure this utility exists

User = get_user_model()  # ✅ Always use your AUTH_USER_MODEL


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)  # ✅ ensure token creation
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target)

        # ✅ Create follow notification
        create_notification(
            recipient=target,
            actor=request.user,
            verb="started following you",
            target=None
        )

        return Response({
            "detail": f"You are now following {target.username}.",
            "you_follow_count": request.user.following.count(),
            "their_follower_count": target.followers.count(),
        }, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target)
        return Response({
            "detail": f"You unfollowed {target.username}.",
            "you_follow_count": request.user.following.count(),
            "their_follower_count": target.followers.count(),
        }, status=status.HTTP_200_OK)


class ListFollowingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = request.user.following.all()
        return Response(UserSerializer(users, many=True).data)


class ListFollowersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = request.user.followers.all()
        return Response(UserSerializer(users, many=True).data)
