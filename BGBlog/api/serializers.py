from rest_framework import serializers
from blog.models import Article
from account.models import User

class ArticleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        #exclude = ('thumbnail', 'created', 'updated')


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        