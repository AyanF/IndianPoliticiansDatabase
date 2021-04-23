from rest_framework import viewsets
import json
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from . import models
from . import serializers

class UserViewset(viewsets.ViewSet):

    def list(self, request):
        UserAccountList= models.UserAccounts.objects.all()
        serializer_class = serializers.UserAccountSerializer(UserAccountList, many=True)
        return Response (serializer_class.data)

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            UserData = models.UserAccounts.objects.get(id=id)
            serializer_class = serializers.UserAccountSerializer(UserData)
            return Response (serializer_class.data)

    def create(self, request):
        serializer_class = serializers.UserAccountSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg': 'Data Entered' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)


    def update(self, request, pk=None):
        id=pk
        if id is not None:
            UserData = models.UserAccounts.objects.get(id=id)
            serializer_class =serializers.UserAccountSerializer(UserData, data=request.data)
            if serializer_class.is_valid():
             serializer_class.save()
             serializer_class = serializers.UserAccountSerializer(UserData)
             return Response({'msg': 'Data Updated' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        UserData = models.UserAccounts.objects.get(id=id)
        UserData.delete()
        return Response({'msg': 'Data Deleted' })

class PartyRatingViewSet(viewsets.ViewSet):
    
    def list(self, request):
        PartyRatingList= models.PartyRating.objects.all()
        serializer_class = serializers.PartyRatingSerializer(PartyRatingList, many=True)
        return Response (serializer_class.data)

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            PartyRatingData = models.PartyRating.objects.get(id=id)
            serializer_class = serializers.PartyRatingSerializer(PartyRatingData)
            return Response (serializer_class.data)

    def create(self, request):
        serializer_class = serializers.PartyRatingSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()

            latestRecord = models.PartyRating.objects.latest('id')
            latestRatingId = latestRecord.pk
            partyId = latestRecord.party_id
            latestRating = latestRecord.rating
            print(latestRatingId)
            print(partyId)
            print(latestRating)
            

            updatePartyRating= models.PoliticalParty.objects.get(id=partyId)
            oldRating =updatePartyRating.partyRating
            print(oldRating)
            newRating=(oldRating+latestRating)/2
            print(newRating)
            updatePartyRating.partyRating=newRating
            updatePartyRating.save()

            return Response({'msg': 'Data Entered' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)


    def update(self, request, pk=None):
        id=pk
        if id is not None:
            PartyRatingData = models.PartyRatings.objects.get(id=id)
            serializer_class =serializers.PartyRatingSerializer(PartyRatingData, data=request.data)
            if serializer_class.is_valid():
             serializer_class.save()
             serializer_class = serializers.PartyRatingSerializer(PartyRatingData)
             return Response({'msg': 'Data Updated' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        PartyRatingData = models.PartyRating.objects.get(id=id)
        PartyRatingData.delete()
        return Response({'msg': 'Data Deleted' })


class PoliticianRatingViewSet(viewsets.ViewSet):

      def list(self, request):
        PoliticianRatingList= models.PoliticianRating.objects.all()
        serializer_class = serializers.PoliticianRatingSerializer(PoliticianRatingList, many=True)
        return Response (serializer_class.data)

      def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            PoliticianRatingData = models.PoliticianRating.objects.get(id=id)
            serializer_class = serializers.PoliticianRatingSerializer(PoliticianRatingData)
            return Response (serializer_class.data)

      def create(self, request):
        serializer_class = serializers.PoliticianRatingSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()

            latestRecord = models.PoliticianRating.objects.latest('id')
            latestRatingId = latestRecord.pk
            politicianId = latestRecord.politician_id
            latestRating = latestRecord.rating
            print(latestRatingId)
            print(politicianId)
            print(latestRating)
            

            updatePoliticianRating= models.Politicians.objects.get(id=politicianId)
            oldRating =updatePoliticianRating.politicianRating
            print(oldRating)
            newRating=(oldRating+latestRating)/2
            print(newRating)
            updatePoliticianRating.politicianRating=newRating
            updatePoliticianRating.save()

            return Response({'msg': 'Data Entered' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)


      def update(self, request, pk=None):
        id=pk
        if id is not None:
            PoliticianRatingData = models.PoliticianRating.objects.get(id=id)
            serializer_class =serializers.PoliticianRatingSerializer(PoliticianRatingData, data=request.data)
            if serializer_class.is_valid():
             serializer_class.save()
             serializer_class = serializers.PoliticianRatingSerializer(PoliticianRatingData)
             return Response({'msg': 'Data Updated' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)

      def destroy(self, request, pk):
        id=pk
        PoliticianRatingData = models.PoliticianRating.objects.get(id=id)
        PoliticianRatingData.delete()
        return Response({'msg': 'Data Deleted' })
        
    

class PoliticianWorkRatingViewSet(viewsets.ViewSet):

      def list(self, request):
        PoliticianWorkRatingList= models.PoliticianWorkRating.objects.all()
        serializer_class = serializers.PoliticianWorkRatingSerializer(PoliticianWorkRatingList, many=True)
        return Response (serializer_class.data)

      def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            PoliticianWorkRatingData = models.PoliticianWorkRating.objects.get(id=id)
            serializer_class = serializers.PoliticianWorkRatingSerializer(PoliticianWorkRatingData)
            return Response (serializer_class.data)

      def create(self, request):
        serializer_class = serializers.PoliticianWorkRatingSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()

            latestRecord = models.PoliticianWorkRating.objects.latest('id')
            latestRatingId = latestRecord.pk
            politicianId = latestRecord.politician_id
            latestRating = latestRecord.rating
            # print(latestRatingId)
            # print(politicianId)
            # print(latestRating)
            
            updatePoliticianWorkRating= models.PoliticianWork.objects.get(id=politicianId)
            # print(updatePoliticianWorkRating)
            oldRating =updatePoliticianWorkRating.Totalrating
            print(oldRating)
            newRating=(oldRating+latestRating)/2
            print(newRating)
            updatePoliticianWorkRating.Totalrating=newRating
            updatePoliticianWorkRating.save()

            return Response({'msg': 'Data Entered' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors)


      def update(self, request, pk=None):
        id=pk
        if id is not None:
            PoliticianWorkRatingData = models.PoliticianWorkRating.objects.get(id=id)
            serializer_class =serializers.PoliticianWorkRatingSerializer(PoliticianWorkRatingData, data=request.data)
            if serializer_class.is_valid():
             serializer_class.save()
             serializer_class = serializers.PoliticianWorkRatingSerializer(PoliticianWorkRatingData)
             return Response({'msg': 'Data Updated' }, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)

      def destroy(self, request, pk):
        id=pk
        PoliticianWorkRatingData = models.PoliticianWorkRating.objects.get(id=id)
        PoliticianWorkRatingData.delete()
        return Response({'msg': 'Data Deleted' })



class PartyViewset(viewsets.ModelViewSet):

     queryset=models.PoliticalParty.objects.all()
     serializer_class=serializers.PartySerializer

class PoliticiansViewset(viewsets.ModelViewSet):
    queryset=models.Politicians.objects.all()
    serializer_class=serializers.PoliticianSerializer

class PoliticianWorkViewset(viewsets.ModelViewSet):
    queryset=models.PoliticianWork.objects.all()
    serializer_class=serializers.PoliticianWorkSerializer



