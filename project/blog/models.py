from django.db import models

# Create your models here.
class Topic(models.Model):
    "主题"
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '标题'
        #verbose_name_plural = '条目'

    def __str__(self):
        "返回"
        return  self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '内容'
        #verbose_name_plural = '条目'

    def __str__(self):
        if len(str(self.text)) > 50:
            return self.text[:50] + "..."
        else:
            return self.text