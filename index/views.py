from django.shortcuts import render
from django.core.paginator import Paginator
from getpass import getpass
from github import Github
from django.http import HttpResponse
import requests
# Create your views here.

def reps(request):
    g = Github('kotifnat','19960508aB')
    repos = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search = g.search_repositories(q)
        for repo in search:
            last = repo.get_commit(sha='master')
            all = str(repo.name) + ', ' + str(repo.stargazers_count) + ' stars, ' + str(last.commit.author.date) +', ' + str(last.html_url)
            repos.append(all)
    else:
        for repo in g.search_repositories("stars:>=90000"):
            last = repo.get_commit(sha='master')
            all = str(repo.name) + ', ' + str(repo.stargazers_count) + ' stars, ' + str(last.commit.author.date) +', ' + str(last.html_url)
            repos.append(all)
    return render(request, 'index/index.html', locals())

def rep_detail(request, name):
    g = Github('kotifnat','19960508aB')
    repo = g.search_repositories(name)
    return render(request, 'index/repo_detail.html', locals())
