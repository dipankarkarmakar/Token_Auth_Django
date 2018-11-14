# from django.db import models
# # from core.validations import image_extension, mobile_regex, username_validator
#
# # Create your models here.
# class GoUser(models.Model):
#
#     email = models.EmailField(verbose_name=('email address'),
#                               max_length=255,
#                               unique=True
#                               )
#     username = models.CharField(('Username'),
#                                 max_length=50,
#                                 blank=False,
#                                 null=True,
#                                 )
#     full_name = models.CharField(('Full name'),
#                                  max_length=150,
#                                  blank=True,
#                                  null=False
#                                  )
#     phone = models.CharField(('Contact no'),
#                              max_length=18,
#                              blank=True,
#                              null=False,
#                              )
#     country_code = models.CharField(max_length=4, blank=True, null=False)
#     password = models.CharField(('password'), max_length=128)
#
#     def __str__(self):
#         return self.email
