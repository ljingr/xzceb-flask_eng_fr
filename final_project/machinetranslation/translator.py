"""
Translating English to French and Frech to English
Created by ljingr
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translating English to French
    Created by ljingr
    """
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    french_textf = french_text['translations'][0]['translation']
    return french_textf

def french_to_english(french_text):
    """
    Translating French to English
    Created by ljingr
    """
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    english_textf = english_text['translations'][0]['translation']
    return english_textf
