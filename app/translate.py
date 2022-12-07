import json

import requests
from flask_babel import _

from app import myapp

MS_TRANSLATOR_KEY = 'MS_TRANSLATOR_KEY'

def translate(text, source_language, dest_language):
    print(text, source_language, dest_language)
    if MS_TRANSLATOR_KEY not in myapp.config or not myapp.config[MS_TRANSLATOR_KEY]:
        return _("Error: the translattion service is not configured.")
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate'
    constructed_url = endpoint + path
    auth = {
        'Ocp-Apim-Subscription-Key': myapp.config[MS_TRANSLATOR_KEY],
        'Ocp-Apim-Subscription-Region': 'eastasia'}

    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': [dest_language]
    }

    r = requests.post(constructed_url, params=params, headers=auth, json=[{'text':text}])
    print(r)
    print(r.json())
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']