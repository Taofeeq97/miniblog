from django.db import models


class blogentry(models.Model):
    blog_title=models.CharField(max_length=30)
    blog_header=models.CharField(max_length=100)
    blog_content=models.CharField(max_length=300)


    def __str__(self):
        return "{} {} {}".format(self.blog_title, self.blog_header, self.blog_content)
