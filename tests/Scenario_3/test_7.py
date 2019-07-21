# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_7(browser, pdf_file):
    """
    Сценарий 5 "Создание пользователя"
        Шаг 1. Загрузка главной страницы:
        открыть страницу http://10.5.127.12/web

        Шаг 2. Авторизация:
        Вести логин и пароль - MekhdievZ, QAtest05

        Шаг 3. Переход во вкладку "Админка. Пользователи"
        Нажать кнопку "Создать"
        Логин - user_test001
        Группа - users
        ФИО - Тест Тест Тест
        Муниципальное образование. Район - Московская область
        Поселение - Московская область
        Пароль - 12345
        Подтверждение пароля - 12345
        В подразделе "Роли" в выпадающем списке выбрать значение "oms_employee"
        Нажать кнопку "Добавить"
        В подразделе "Группы для просмотра" в выпадающем списке выбрать значение "root"
        Нажать кнопку "Добавить"  "Сохранить" "Закрыть"

        Шаг 4. Выйти из системы путем нажатия кнопки "Выход"
        Осуществить вход в систему под учетной записью testtesttest, пароль - 12345
    """

    with allure.step('Шаг 1. Открыть тестовый стенд МВК'):
        try:
            browser.open_test_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 2. Залогиниться на тестовый стенд МВК'):
        try:
            browser.login_test_mvk('MekhdievZ', 'QAtest05')

            browser.hover_and_click("html/body/nav/div/div[2]/ul/li[6]/a", "//a[@href='/web/users']")
            # browser.get('http://10.5.127.12/web/users')
            browser.xpath("//button[@id='newAuthObjectButton']").click()
            time.sleep(3)
            browser.xpath("//input[@autocomplete='off']").send_keys(u'user_test001')
            # time.sleep(3)
            browser.select_option("//select[@name='authGroupUS']", 'users')
            # ФИО
            browser.xpath(".//*[@id='fullNameUS']/input[1]").send_keys(u'Тест Тест Тест')
            time.sleep(3)
            # Муниципальное образование
            browser.select_option('//*[@id="municipalityUS"]/select[1]', "Московская область")
            time.sleep(3)
            browser.select_option(".//*[@id='municipalityUS']/select[2]", 'Московская область')
            # Пароль
            browser.xpath(".//*[@id='passwordUS']/input[1]").send_keys(u'123456')
            browser.xpath(".//*[@id='assertPasswordUS']/input[1]").send_keys(u'123456')
            # Роли
            browser.select_option(".//*[@id='rolesMultilineTable']/div[2]/div/div/div[1]/select", 'oms_employee')
            browser.xpath('//*[@id="rolesMultilineTable"]/div[2]/div/div/div[2]/button').click()
            browser.select_option(".//*[@id='groupSeesMultilineTable']/div[2]/div/div/div[1]/select", 'root')
            browser.xpath('//*[@id="groupSeesMultilineTable"]/div[2]/div/div/div[2]/button').click()
            time.sleep(3)
            browser.xpath(".//*[@id='js-save-card_user']").click()
            browser.xpath(".//*[@id='js-close-card_user']").click()
            time.sleep(3)
            browser.xpath("//a[@title='Выйти']").click()
            # Вход в систему под учетной записью
            browser.login_test_mvk('user_test001','123456')
            time.sleep(3)
            browser.xpath("//a[@title='Выйти']").click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

