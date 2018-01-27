# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Tag
from forms import PostForm
import boto
from boto.s3.key import Key
import os
import shutil

# Create your views here.
def tags_home(request):
    query_data = Tag.objects.all()
    context = {"title":"All TAGS","Tag_name":query_data,}
    return render(request, "index.html",context)

def tags_detail(request, id=None):
    instance = get_object_or_404(Tag,id=id)
    file_url = get_file_url_from_s3_location(str(instance.job_title)+'/output.mp3')
    context = {"tag_name":instance.tag_name,
    "download_url":file_url,
    }

    return render(request, 'post_detail.html', context)

def post_tags(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        file_name = Tag.objects.get(job_title=instance.job_title)
        upload_files_to_s3('/home/prateekeshwar/my_assign/media_cdn/'+str(file_name.audio_file),
        str(instance.job_title)+'/output.mp3')
        shutil.rmtree('/home/prateekeshwar/my_assign/media_cdn/audio')
    context = {
        "form":form,
    }
    return render(request, "post_form.html",context)

def get_bucket_name():
    AWS_CONNECTION = boto.connect_s3(os.environ['AWS_ACCESS_KEY_ID_VAT'],
                                 os.environ['AWS_SECRET_ACCESS_KEY_VAT'])
    bucket_name = AWS_CONNECTION.get_bucket(os.environ['AWS_BUCKET_NAME_VAT'])
    return bucket_name

def upload_files_to_s3(sys_file_path,s3_file_path):
    bucket_name = get_bucket_name()
    k = Key(bucket_name)
    k.key = s3_file_path
    k.set_contents_from_filename(sys_file_path)

def get_file_url_from_s3_location(s3_file_location):
    bucket = get_bucket_name()
    key = bucket.new_key(s3_file_location)
    file_url = key.generate_url(expires_in=600)
    return file_url


