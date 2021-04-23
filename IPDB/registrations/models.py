from django.db import models

class UserAccounts(models.Model):

    fullName= models.CharField(max_length=100)
    userName=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    
class PoliticalParty(models.Model):
    partyName= models.CharField(max_length=100)
    partySlogan= models.CharField(max_length=200)
    partyObjective=models.CharField(max_length=300)
    partyLeader = models.CharField(max_length=100)
    partyRating=models.PositiveIntegerField(default='10')
    
    def __str__(self):
     return f"{self.id}"

class Politicians(models.Model):
    fullName= models.CharField(max_length=100)
    party=models.ForeignKey(PoliticalParty, related_name='members' , on_delete=models.CASCADE)
    postName= models.CharField(max_length=50)
    politicianRating=models.PositiveIntegerField(default='10')

    def __str__(self):
     return f"{self.fullName}"

class PartyRating(models.Model):
    party=models.ForeignKey(PoliticalParty, related_name='ratings' , on_delete=models.CASCADE)
    user=models.ForeignKey(UserAccounts, related_name='user',unique=True, on_delete=models.CASCADE )
    rating=models.PositiveIntegerField(default='0')

    def __str__(self):
      return f"{self.rating,self.party_id}"

    
class PoliticianRating(models.Model):
    politician=models.ForeignKey(Politicians, related_name='Ratings' , on_delete=models.CASCADE)
    user=models.ForeignKey(UserAccounts, related_name='User',unique=True ,on_delete=models.CASCADE )
    rating=models.PositiveIntegerField(default='0')

    def __str__(self):
     return f"{self.rating,self.politician_id}"

class PoliticianWork(models.Model):
    politician=models.ForeignKey(Politicians, related_name='work' , on_delete=models.CASCADE)
    work=models.CharField(max_length=1000)
    Totalrating=models.PositiveIntegerField(default='10')

    def __str__(self):
     return f"{self.work}"

      


class PoliticianWorkRating(models.Model):
    politician=models.ForeignKey(Politicians, related_name='workRatings' , on_delete=models.CASCADE)
    user=models.ForeignKey(UserAccounts, related_name='workUser',unique=True,on_delete=models.CASCADE )
    rating=models.PositiveIntegerField(default='0')

    def __str__(self):
      return f"{self.rating,self.politician_id}"
    
    
    