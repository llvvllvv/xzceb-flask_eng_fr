"""
Import module
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('CwA6OfUxZlUzy4RCTby9q-0M3ga1tIgay-LqpUaOo5V-')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/21138319-838a-4440-8c34-8e6c540cba86')

def english_to_french(english_text):
    """
    This function translates english to french
    """
    frenchtranslation = language_translator.translate(
        text=english_text, model_id='en-fr'
    ).get_result()
    return frenchtranslation.get("translations") [0].get("translation")

def french_to_english(french_text):
    """
    This function translates french to english
    """
    englishtranslation = language_translator.translate(
        text=french_text, model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations") [0].get("translation")
