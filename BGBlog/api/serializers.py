from rest_framework import serializers
from blog.models import Article

class ArticleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        #exclude = ('thumbnail', 'created', 'updated')
