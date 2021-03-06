from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.ProtectedError)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def comment_count(self):
        return self.comments.filter(created_date__lte=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.ProtectedError)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)




    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post,related_name='Likes' ,on_delete=models.CASCADE)


