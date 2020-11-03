from rest_framework import serializers
from place.serializers import PlaceSerializer
from .models import Funding, MainFunding, FundingComment
from accounts.models import User
from django.utils import timezone

class FundingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingComment
        fields = ('id', 'user', 'funding', 'content', 'created_at', 'updated_at')


class FundingCommentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingComment
        fields = ('id', 'content')


class FundingSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner_user.nickname')
    backed_list = serializers.StringRelatedField(many=True)
    comment_list = FundingCommentSerializer(many=True, read_only=True)
    place = PlaceSerializer(read_only=True)
    class Meta:
        model = Funding
        fields = ('id','thumbnail_image', 'place','title', 'description', 'owner_username',
                  'backed_list', 'content_image', 'content_text', 'funding_goal_amount',
                  'funding_amount', 'created_at', 'ended_at', 'total_likes' ,'user_likes', 'comment_list')


class FundingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ('image', 'place','title','content', 'funding_price', 'created_at', 'ended_at','total_likes')


class FundingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = '__all__'


class MainFundingSerializer(serializers.ModelSerializer):
    main_funding = FundingSerializer(many=True, read_only=True)
    class Meta:
        model = MainFunding
        fields = ('id', 'main_funding')


class MainFundingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFunding
        fields = ('id', 'main_funding')





