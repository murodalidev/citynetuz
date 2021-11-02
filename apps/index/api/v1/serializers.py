from rest_framework import serializers
from ...models import News, Partner, Object


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'get_img_url', 'title', 'content', 'date_created')


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('id', 'get_img_url', 'title', 'link', 'date_created')


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = ('id', 'get_img_url', 'title', 'date_created')