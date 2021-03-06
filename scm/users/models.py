from django.db import models

# Create your models here.
class User(models.Model):
    identityChoices = (('教师','教师'),('学生','学生'),)
    userID = models.CharField('用户编号', max_length=20, primary_key=True)
    userName = models.CharField('用户姓名', max_length=20)
    userPassword = models.CharField('用户密码', max_length=20)
    userIdentity = models.CharField("用户身份", max_length=2, choices=identityChoices, default='学生')
    userAddTime = models.DateField('添加时间', auto_now_add=True)
    
    class Meta:
        ordering = ['-userAddTime']
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.userID