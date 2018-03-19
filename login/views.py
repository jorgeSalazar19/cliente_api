from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests
from social_django.models import UserSocialAuth
import twitter, json
from django.conf import settings

def index(request):

    template = loader.get_template('index.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))

def logOut(request):
    logout(request)
    return redirect('/')


@login_required
def home(request):
    print(request)
    user = request.user
    print('usuario: ' , user )
    template = loader.get_template('home.html')
    ctx={'user': user,}
    return HttpResponse(template.render(ctx,request))

@login_required
def followers(request):
    template = loader.get_template('followers.html')
    CONSUMER_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
    CONSUMER_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
    OAUTH_TOKEN = settings.TWITTER_ACCESS_TOKEN
    OAUTH_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

    auth = twitter.oauth.OAuth( OAUTH_TOKEN , OAUTH_SECRET, CONSUMER_KEY , CONSUMER_SECRET )
    twitter_api = twitter.Twitter(auth=auth)

    q = request.user 
    count = 20

    search_results = twitter_api.friends.list(q=q, count=count , include_user_entities=False , cursor=-1 , skyp_status=True , screen_name=q)

    print(len(search_results['users']))

    list_friends=[]*len(search_results['users'])
    for i in range(0,(len(search_results['users'])-1)):
        friend = search_results['users'][i]['name']
        list_friends.append(friend)
    
    list_tweets = []*len(list_friends)
    for i in list_friends:
        search = twitter_api.search.tweets(q=i,count=1)
        list_tweets.append(search)

    print(list_tweets[10]['statuses'][0]['geo'])

    ctx={}
    return HttpResponse(template.render(ctx,request)) 