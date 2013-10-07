# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '"%s": %s' % (self.title, self.body)

    def to_dict(self):
        return dict(title=self.title,
                    body=self.body,
                    date=self.date)

    def post_str(self):
        return '%d/%d, %d %d:%d:%d' % (
            self.date.month, self.date.day, self.date.year,
            self.date.hour, self.date.minute, self.date.second)
