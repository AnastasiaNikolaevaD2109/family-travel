from rest_framework import serializers
from .models import Trail, TrailImage, IncludedService, AvailableDate, Comment

class TrailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailImage
        fields = ['id', 'image', 'order']

class IncludedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncludedService
        fields = ['service']

class AvailableDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableDate
        fields = ['date']

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'text', 'created_at']

class TrailListSerializer(serializers.ModelSerializer):
    images = TrailImageSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Trail
        fields = ['id', 'name', 'location', 'price', 'difficulty', 'description',
                  'keywords', 'duration', 'accommodation', 'coordinates',
                  'images', 'likes_count', 'comments_count']

class TrailDetailSerializer(TrailListSerializer):
    included_services = IncludedServiceSerializer(many=True, read_only=True)
    available_dates = AvailableDateSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
