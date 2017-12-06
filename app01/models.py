from django.db import models

# Create your models here.



class UserInfo(object):
    '''用户信息'''
    nid=models.BigAutoField(primary_key=True)
    telephone=models.CharField(max_length=11,blank=True,verbose_name='手机号码')
    avatar=models.FloatField(verbose_name='头像')

class Blog(models.Model):
    '''博客信息'''
    nid=models.BigAutoField(primary_key=True)
    title=models.CharField(verbose_name='个人博客标题',max_length=64)
    site=models.CharField(verbose_name='个人博客前缀',max_length=32,unique=True)
    theme=models.CharField(verbose_name='博客主题',max_length=32)
    user=models.OneToOneField(verbose_name='用户详细',to='UserInfo')

class Category(models.Model):
    '''博主个人文章分类'''
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='分类标题',max_length=32)
    blong=models.ForeignKey(verbose_name='所属博客',to='Blog')

class Article(models.model):
    '''文章'''
    nid=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=50,verbose_name='文章标题')
    dasc=models.CharField(max_length=255,verbose_name='文章描述')
    comment_num=models.IntegerField(default=0)
    poll_num=models.IntegerField(default=0)
    category = models.ForeignKey(verbose_name='文章类型', to='Category', to_field='nid', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')

class AriticleDetail(models.Model):
    '''文章详细表'''
    countent=models.TextField(verbose_name='文章内容')
    article=models.CharField(verbose_name='所属文章',to='Article')

class Comment(models.Model):
    '''评论表'''
    nid=models.BigAutoField(primary_key=True)
    article=models.ForeignKey(verbose_name='评论文章',to='Ariticle')
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    parent_id = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid')

    poll_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Poll(models.Model):
    """
    点赞表
    """
    user = models.ForeignKey('UserInfo', null=True)
    article = models.ForeignKey("Article", null=True)
    comment = models.ForeignKey("Comment", null=True)
