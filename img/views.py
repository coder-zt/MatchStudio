from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def res(request):
    # 获取图片文件的路径
    image_path = os.path.join('static/images', '1.jpg')

    # 读取图片文件
    with open("D:\Coding\Python\dianxuan\dianxuan\data\secDataset/1/segment_S_0.jpg", 'rb') as f:
        image_data = f.read()

    # 返回HttpResponse对象，设置content_type为'image/jpeg'
    return HttpResponse(image_data, content_type='image/jpeg')
# Create your views here.

def img(request, index, name):
    print(index)
    print(name)
    # 获取图片文件的路径
    image_path = os.path.join('static/images', '1.jpg')

    # 读取图片文件
    with open(f"D:\Coding\Python\dianxuan\dianxuan\data\secDataset/{index}/{name}", 'rb') as f:
        image_data = f.read()

    # 返回HttpResponse对象，设置content_type为'image/jpeg'
    return HttpResponse(image_data, content_type='image/jpeg')