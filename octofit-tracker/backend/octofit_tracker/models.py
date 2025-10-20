from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField(help_text='Duration in minutes')
    calories_burned = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    suggested_for = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_calories = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Leaderboard for {self.team.name}"
