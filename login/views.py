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
    
    user = request.user
    print('usuario: ' , user )
    template = loader.get_template('home.html')
    ctx={'user': user,}
    return HttpResponse(template.render(ctx,request))

@login_required
def followers(request):
    followers_screen_name = []
    template = loader.get_template('followers.html')
    CONSUMER_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
    CONSUMER_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
    OAUTH_TOKEN = settings.TWITTER_ACCESS_TOKEN
    OAUTH_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

    auth = twitter.oauth.OAuth( OAUTH_TOKEN , OAUTH_SECRET, CONSUMER_KEY , CONSUMER_SECRET )
    twitter_api = twitter.Twitter(auth=auth)

    q = request.user 
    count = 20

    search_results = twitter_api.friends.list(q=q, count=3)

    #NOMBRES DE SEGUIDORES
    followers_screen_name = getScreenName(search_results)

    contexto = makeContext(twitter_api,followers_screen_name)

    print(contexto)
    
    ctx={
        'context': contexto
    }   

    return HttpResponse(template.render(ctx,request)) 


def getScreenName(followers):
    quest = []
    i = 0
    while i < len(followers['users']):
        quest.append(followers['users'][i]['screen_name'])
        i += 1
    return quest

def makeContext(twitter_api, followers):
    quest = {}
    followers_last_tweet = []
    aux = []
    coordinates = []

    for name in followers:
        followers_last_tweet = twitter_api.statuses.user_timeline(screen_name="JhonE_Sanz", count=1)
        try:
            coordinates = followers_last_tweet[0]['geo']['coordinates']
        except:
            coordinates = []
        aux = [ followers_last_tweet[0]['text'], coordinates ]
        quest[name] = aux

    return quest
