from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)     # 由少量字符组成的数据
    date_added = models.DateTimeField(auto_now_add=True)    # 记录日期和时间的数据

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的关于某个主题的具体知识"""
    # 将该条目关联到另一条目中，这里是Topic；on_delete让其删除该条目时同时也删除相关联条目，即级联删除
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()   # 相比Char字段，该Text字段长度不受限制
    data_added = models.DateTimeField(auto_now_add=True)    # 记录时间戳

    class Meta:
        """用于管理模型的额外信息"""
        verbose_name_plural = 'entries'

        def __str__(self):
            """返回一个表示条目的简单字符串"""
            return f"{self.text[:50]}..."
