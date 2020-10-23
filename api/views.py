import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET', ))
def get_languages(request, date):
    url = "https://api.github.com/search/repositories?q=created: >{0}&sort=stars&order=desc".format(
        date)
    repositories = requests.get(url).json()
    languages = {}
    for repo in repositories['items']:
        language = repo['language']
        if language not in languages:  # initaite language dictionary
            languages[language] = {}
            languages[language].setdefault('repos', [])
            languages[language].setdefault('num_repos', 0)
        languages[language]['repos'].append(repo)
        languages[language]['num_repos'] += 1
    return Response(languages)
