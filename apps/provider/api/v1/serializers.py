from rest_framework import serializers
from ...models import Notification, InternetTariff, CityArea, DistrictArea, CableTech, StreetArea, HomeArea, Request, \
    TypeChannel, Channel, TelephonyTariff


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id', 'title', 'content', 'date_created')


class InternetTariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternetTariff
        fields = ('id', 'title', 'speed', 'tas_ix', 'price', 'price_cash6', 'price_cash12')


class TelephonyTariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelephonyTariff
        fields = ('id', 'title', 'minutes', 'price')


class CityAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityArea
        fields = ('id', 'title')


class DistrictAreaSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.title', read_only=True)

    class Meta:
        model = DistrictArea
        fields = ('id', 'city', 'city_name', 'title')


class CableTechSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableTech
        fields = ('id', 'title')


class HomeAreaSerializer(serializers.ModelSerializer):
    street_name = serializers.CharField(source='street.title', read_only=True)

    class Meta:
        model = HomeArea
        fields = ('id', 'street', 'street_name', 'title')


class StreetAreaSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district.title', read_only=True)
    tech_name = serializers.CharField(source='tech.title', read_only=True)
    flats = serializers.SerializerMethodField()

    def get_flats(self, obj):
        qs = HomeArea.objects.filter(street=obj, is_active=True)
        sz = HomeAreaSerializer(instance=qs, many=True)
        return sz.data

    class Meta:
        model = StreetArea
        fields = ('id', 'district', 'district_name', 'title', 'flats', 'tech', 'tech_name')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('city', 'street', 'district', 'home', 'flat', 'full_name', 'phone')


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('id', 'get_img_url', 'title')


class TypeChannelSerializer(serializers.ModelSerializer):
    # channels = ChannelSerializer(read_only=True, many=True)
    channels = serializers.SerializerMethodField()

    def get_channels(self, obj):
        qs = Channel.objects.filter(type_channel=obj, is_active=True)
        sz = ChannelSerializer(instance=qs, many=True)
        return sz.data

    class Meta:
        model = TypeChannel
        fields = ('id', 'title', 'channels')
