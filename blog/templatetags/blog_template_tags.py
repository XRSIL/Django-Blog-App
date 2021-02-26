from django import template
from blog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def extractFirstName(username):
    user = get_object_or_404(User, username=username)
    first_name = user.first_name
    return first_name

def extractLastName(username):
    user = get_object_or_404(User, username=username)
    last_name = user.last_name
    return last_name

def extractProfileImage(username):
    user = get_object_or_404(User, username=username)
    img_url = user.profile.image.url
    return img_url

register = template.Library()
register.filter('extractFirstName', extractFirstName)
register.filter('extractLastName', extractLastName)
register.filter('extractProfileImage', extractProfileImage)