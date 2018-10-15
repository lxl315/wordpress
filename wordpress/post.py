# coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import requests,time
wp = Client('http://booksduo.com/xmlrpc.php', xxx,xxx) #改成自己的wordpress 后台密码
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }

# post.thumbnail = attachment_id #缩略图的id

# post.custom_fields = []  # 自定义字段列表
# post.custom_fields.append({  # 添加一个自定义字段 #是否下载
#     'key': 'start_down',
#     'value': 1
# })
# post.custom_fields.append({  # 添加第二个自定义字段
#     'key': 'erphpdown',
#     'value': 1
# })
# post.custom_fields.append({  # 添加第三个自定义字段 下载价格
#     'key': 'down_price',
#     'value': 0.1
# })
#
# post.custom_fields.append({  # 添加第三个自定义字段 硬擦的下载地址的url
#     'key': 'down_url',
#     'value': 'https://pan.baidu.com/s/18euvTbBYGhMy_2S4yglDZQ'
# })
# post.custom_fields.append({  # 添加第三个自定义字段 必须开启 1为会员原价
#     'key': 'member_down',
#     'value': 1
# })
# post.custom_fields.append({  # 添加第三个自定义字段 隐藏内容
#     'key': 'hidden_content',
#     'value': '百度网盘密码：by1f'
# })



def autoPost(image,title,tags,content,download,**kw):
    """
    文章发布方法
    :param image: 文章内要上传的图片
    :param title:文章标题
    :param tags:文章标签
    :param content:文章内容
    :param **kw:自定义的字段
    :return:
    """
    html =requests.get(image)
    imgFile = str(int(time.time()))+'.jpg'
    with open(imgFile,'wb') as file:
        file.write(html.content)

    filename = './'+imgFile  # 上传的图片文件路径
    data = {
        'name': imgFile,
        'type': 'image/jpeg',  # mimetype
    }
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
    response = wp.call(media.UploadFile(data))
    #attachment_id = response['id']
    header= ''
    if 'header' in kw:
        header = kw['header']
    post = WordPressPost()
    post.title = title
    url = response['url']
    post.content = '<img class="size-medium wp-image-203 alignleft" src='+url+' width="240" height="300" />'+header+'</br>'+content+download

    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.terms_names = {
        'post_tag': tags  # 文章所属标签，没有则自动创建
        # 文章所属分类，没有则自动创建
    }
    post.id = wp.call(posts.NewPost(post))
    print('发布成功，文章ID:'+post.id)
