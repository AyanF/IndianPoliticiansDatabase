from rest_framework import serializers
from .models import UserAccounts, PoliticalParty, Politicians, PartyRating, PoliticianRating, PoliticianWork , PoliticianWorkRating

class UserAccountSerializer(serializers.ModelSerializer):
    workUser = serializers.StringRelatedField(many=True)
    class Meta:
        model =UserAccounts
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):

    members = serializers.StringRelatedField(many=True)
    # ratings = serializers.StringRelatedField(many=True)

    class Meta:
        model = PoliticalParty
        fields = '__all__'

class PoliticianSerializer(serializers.ModelSerializer):

    # Ratings = serializers.StringRelatedField(many=True)
    work = serializers.StringRelatedField(many=True)
    # workRatings = serializers.StringRelatedField(many=True)

    class Meta:
        model =Politicians
        fields = '__all__'

class PartyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model =PartyRating
        fields = '__all__'

class PoliticianRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model =PoliticianRating
        fields = '__all__'

class PoliticianWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PoliticianWork
        fields = '__all__'

class PoliticianWorkRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model =PoliticianWorkRating
        fields = '__all__'