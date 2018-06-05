from rest_framework import serializers
from.models import Post, Category

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'created_date')
        