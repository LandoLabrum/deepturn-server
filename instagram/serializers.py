from rest_framework import serializers
from instagram.models import Account, Cookies
 
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class CookiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookies
        fields = '__all__'