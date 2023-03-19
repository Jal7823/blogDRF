from rest_framework import serializers
from ..models import Post,Category


class SerializerCategories(serializers.ModelSerializer):
    
    class Meta:
        model =Category
        fields = '__all__'

class SerializerPost(serializers.ModelSerializer):
    categories = SerializerCategories(many=True)
    class Meta:
        model = Post
        fields = '__all__'



