from django.contrib.auth import get_user_model
from django.db import models

from utils.models import TimestampModel

User = get_user_model()

class Blog(TimestampModel):
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField('배포 일시', null=True)

    def is_active(self):
        now = timezone.now()

        if not self.published_at:
            return True

        return self.published_at <= now


    class Meta:
        verbose_name ='블로그'
        verbose_name_plural = '블로그 목록'
        ordering = ('-created_at', '-id')

