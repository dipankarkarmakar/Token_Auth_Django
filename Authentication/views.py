from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
# from rest_framework import status, viewsets, permissions, views
# from .models import GoUser
# from .serializers import RegisterSerializer

# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
# from .forms import SignUpForm
#
# @csrf_exempt
# @api_view(["POST"])
# def signup(request):
#     form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                     'user_id': user.pk,
                     'email': user.email},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)



# class Register(viewsets.ModelViewSet):
#     queryset = GoUser.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     def registration_step1(self, request):
#         """
#         If individual user company='GoalEzy', role='admin', link='get_site(self.request)', type='S'
#         If Organization user company=request.data['company_name'], role=request.data['role'],
#          link=request.data['company_link'], type=request.data['type']
#         :param request: email, password, full_name, company_name, role, company_link, type
#         :return: token, user
#         """
#         email = request.data['email'].lower()
#         username = request.data['username']
#         phone = request.data['phone']
#         password = request.data['password']
#         country_code = request.data['country_code']
#         full_name = str.title(request.data['full_name'])
#         check = GoUser.objects.filter(email__iexact=email).exists()
#         if check:
#             content = {
#                 'message': 'Already Exist'
#             }
#             return Response(content, status=status.HTTP_409_CONFLICT)
#
#
#
