import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d95479f2-27fe-41ba-805f-4889d26afa4b")

def englishToFrench(englishText):
    """
    This function translates english to french
    """
    frenchtranslation = language_translator.translate(
        text=englishText, model_id='en-fr'
    ).get_result()
    return frenchtranslation.get("translations") [0].get("translation")

def frenchToEnglish(frenchText):
    """
    This function translates french to english
    """
    englishtranslation = language_translator.translate(
        text=frenchText, model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations") [0].get("translation")