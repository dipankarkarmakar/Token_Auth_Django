# # from rest_framework.views import APIView
# # from rest_framework.parsers import MultiPartParser, FormParser
# # from rest_framework.response import Response
# # from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.decorators import api_view
# # from rest_framework.decorators import parser_classes
# #
#
# # @csrf_exempt
# # @api_view(['POST'])
# # @parser_classes((FormParser, MultiPartParser,))
# # def upload_image(request):
# #     file_obj = request.FILES['image']
# #     remark = request.data['remark']
# #     profile = File()
# #     profile.file = file_obj
# #     profile.remark=remark
# #     profile.save()
# #     imageurl = profile.profile_pic.url
# #     profile.file   = imageurl
# #     profile.save()
# #
# #     return Response(imageurl, status=status.HTTP_200_OK)
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from .models import Profile
#
# @csrf_exempt
# class UserCreate(APIView):
#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#
#                 profile =  Profile()
#                 user_object=User.objects.get(id=serializer.data["id"])
#                 profile.user = user_object
#                 profile.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 # return render(request, 'login.html', {})
#             else:
#                 return Response("Record already exists")
#         else:
#             return Response("Please submit the details correctly")
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

@csrf_exempt
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)