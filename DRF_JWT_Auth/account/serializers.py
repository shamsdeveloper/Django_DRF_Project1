from rest_framework import serializers
from account.models import User
###############################################################################################
class UserRegistrationSerializer(serializers.ModelSerializer):
  #We are writing this becoz we need confirm password field in our Registratin Request
  password2=serializers.CharField(style={'input_type':'password'},write_only=True)
  class Meta:
    model=User
    fields={}
    # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)