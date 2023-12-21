from rest_framework import serializers
from .models import *

class studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields  = ['name','age']
        # exclude = ['id']
        fields ='__all__'


    def validata(self,data):
        if data['age']<18:
            raise serializers.ValidationError({'error':"age cannot be less than 18"})
        return data
    
class Categoryserializer(serializers.ModelSerializer):
        
    class Meta:
        models = Category
        fields ='__all__'

class Bookserializer(serializers.ModelSerializer):
    category = Categoryserializer()
    class Meta:
        models = Book
        fileds = '__all__'

    


