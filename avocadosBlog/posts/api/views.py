import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permitions import IsAdminOrReadOnly


## Clase ModelViewSet
""" Permite crear todos los metodos en un modelo de forma automatica """

class PostModelViewSet(ModelViewSet):
    # permisos de la API
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()





## Clase ViewSet
""" Permite controlar los post, get, updtate, delete de forma general """


# class PostViewSet(ViewSet):
#     def list(self, request):
#         postsSerlizer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=postsSerlizer.data) 

#     def retrieve(self, request, pk : int):
#         post = PostSerializer(Post.objects.get(id=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)

#     def create(self, request):
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         postsSerlizer=PostSerializer(data=body)
#         postsSerlizer.is_valid(raise_exception=True)
#         postsSerlizer.save()

#         return self.get(request)

    



## Clase Tradicional APIView
""" forma clasica se generar APIs con el tipo del metodo """


# class PostApiView(APIView):
    # def get(self, request):
        ## forma tradicional
        # posts = Post.objects.all()
        # posts = [post.title for post in Post.objects.all()]
        # return Response(status=status.HTTP_200_OK, data=posts) 

        ## con serializadores
        # postsSerlizer = PostSerializer(Post.objects.all(), many=True)
        # return Response(status=status.HTTP_200_OK, data=postsSerlizer.data) 


    # def post(self, request):
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        ## forma tradicional
        # print(body)
        # Post.objects.create(title=body['title'], description=body['description'])

        ## con serializadores
        # postsSerlizer=PostSerializer(data=body)
        # postsSerlizer.is_valid(raise_exception=True)
        # postsSerlizer.save()

        # return self.get(request)