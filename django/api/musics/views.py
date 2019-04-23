from django.shortcuts import render,redirect,get_object_or_404
from .models import Music,Artist,Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer,ArtistSerializer,ArtistDetailSerializer,CommentSerializer
from rest_framework.response import Response




@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()    
    
    # Serializer
    serializer = MusicSerializer(musics, many = True)
    return Response(serializer.data)
   
@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music,id = music_id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()   
    
    # Serializer
    serializer = ArtistSerializer(artists, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist,id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)
    
@api_view(['POST'])
def comment_create(request, music_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_id)
        return Response(serializer.data)
        
@api_view(['PUT','DELETE'])
def comment_update_and_delete(request, music_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance = comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'Comment has been updated!'})
    else:
        comment.delete()
        return Response({'message':'Comment has been deleted!'})

        