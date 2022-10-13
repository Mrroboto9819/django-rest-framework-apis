from rest_framework.serializers import ModelSerializer
from posts.models import Post

## serializadores | Gestionan datos de salida

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at']
        # fields = '__all__'