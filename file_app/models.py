# # # from django.db import models
# # #
# # # class File(models.Model):
# # #     file = models.FileField(blank=False, null=False)
# # #     remark = models.CharField(max_length=20)
# # #     timestamp = models.DateTimeField(auto_now_add=True)
# #
# # from django.db import models
# # from probably.users.models import User
# #
# #
# # class FileUpload(models.Model):
# #     created = models.DateTimeField(auto_now_add=True)
# #     owner = models.ForeignKey(User, to_field='id')
# #     datafile = models.FileField()
#
# from django.db import models
# from django.contrib.auth.models import User
# def upload_location(instance, filename):
#     return "%s/%s" % (instance.user, filename)
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     profile_pic =  models.FileField(('photo'), upload_to=upload_location,
#                                    storage=FileSystemStorage(location=settings.MEDIA_ROOT), null=True, blank=True)

from django.db import models
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)