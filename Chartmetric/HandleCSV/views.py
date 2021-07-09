from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Account

import json

from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

#get the account with the username
def getaccount(username):
    #if id
    try:
        idname = int(username)
        account = Account.objects.get(account_id = idname)
        return account

    #if username
    except:
        for account in Account.objects.all():
            accountdecoded = json.loads(account.content)
            foundUsername = accountdecoded['user_profile']['username']
            if foundUsername == username:
                return account
    
    return None

    


# Create your views here.
def index(request):
    contextDict = {}
    accounts = Account.objects.all()
    followersDict = {}
    for account in accounts:
        accountdecoded = json.loads(account.content)
        contextDict[str(account.account_id)] = accountdecoded
        followersDict[str(account.account_id)] = accountdecoded['user_profile']['followers']

    return render(request, 'index.html', {'dict': contextDict, 'followers': followersDict})

def stats(request, username):

    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        return render(request, 'stats.html', {'username': username,'stats': accountdecoded['user_profile']})
    
    raise Http404("User does not exist")

def recentposts(request, username):

    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        return render(request, 'recentposts.html', {'username': username,'recentposts': accountdecoded['user_profile']['recent_posts']})
    
    raise Http404("User does not exist")


def topposts(request, username):

    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        return render(request, 'topposts.html', {'username': username, 'toppost': accountdecoded['user_profile']['top_posts']})
    
    raise Http404("User does not exist")

def commercialposts(request, username):

    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        if 'commercial_posts' in accountdecoded['user_profile']:
            return render(request, 'commercialposts.html', {'username': username, 'commercialposts': accountdecoded['user_profile']['commercial_posts']})
        else:
            return render(request, 'commercialposts.html', {'username': username, 'commercialposts': {}})
    raise Http404("User does not exist")

def loginall(request, username):

    account = getaccount(username)

    if account:
        return HttpResponse(account.content)
    
    raise Http404("User does not exist")

def reportinfo(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        reportinfo = json.dumps (accountdecoded['report_info'])
        return HttpResponse(reportinfo)
    
    raise Http404("User does not exist")

def userprofile(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        userprofile = json.dumps (accountdecoded['user_profile'])
        return HttpResponse(userprofile)
    
    raise Http404("User does not exist")
def audiencelikers(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        audiencelikers = json.dumps (accountdecoded['audience_likers'])
        return HttpResponse(audiencelikers)
    
    raise Http404("User does not exist")

def audiencefollowers(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        audiencefollowers = json.dumps (accountdecoded['audience_followers'])
        return HttpResponse(audiencefollowers)
    
    raise Http404("User does not exist")

def audiencecommenters(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        audiencecommenters = json.dumps (accountdecoded['audience_commenters'])
        return HttpResponse(audiencecommenters)
    
    raise Http404("User does not exist")

def extra(request, username):
    
    account = getaccount(username)

    if account:
        accountdecoded = json.loads(account.content)
        extra = json.dumps (accountdecoded['extra'])
        return HttpResponse(extra)
    
    raise Http404("User does not exist")

