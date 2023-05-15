import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['api_key']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator_instance.set_service_url(url)

def english_to_french(english_text):
    french_text = translator_instance.translate(text=english_text,model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    english_text = translator_instance.translate(text=french_text,model_id="fr-en").get_result()
    return english_text.get("translations")[0].get("translation")
