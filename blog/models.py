from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogTitle(models.Model):

    """A space to add a title for the overall blog."""

    title_text = models.CharField(max_length = 200)

    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.title_text.title()
    
class BlogText(models.Model):

    """This is where you put the text for the home page."""

    title = models.ForeignKey(BlogTitle, on_delete = models.CASCADE)

    text = models.TextField()

    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        if len(self.text) > 50:

            return f"{self.text[:50]}..."
            
        else:

            return f"{self.text[:50]}"
        
# ---------------------------------------------------------------------------- #
        
class PostTitle(models.Model):

    """A place to make posts in the blog."""

    post_title_text = models.CharField(max_length = 200)

    pub_date = models.DateTimeField(auto_now_add = True)

    holder = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):

        return self.post_title_text.title()
    
class PostText(models.Model):

    """Here we'll have the content."""

    post_title = models.ForeignKey(PostTitle, on_delete = models.CASCADE)

    text = models.TextField()

    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        if len(self.text) > 50:

            return f"{self.text[:50]}..."
            
        else:

            return f"{self.text[:50]}"



