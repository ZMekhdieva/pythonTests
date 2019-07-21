# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_11 (browser, pdf_file):
    """
    Сценарий 10. Выгрузка отчета "Протокол отказов"
        Шаг 1. Загрузка главной страницы:
        открыть страницу http://10.5.127.12/web

        Шаг 2. Авторизация:
        Вести логин и пароль - MekhdievZ, QAtest05

        Шаг 3. Перейти во вкладку "МИО.Протокол.Отдел отказа"
        Нажать кнопку "Протокол отказов"
        В поле "Номер отчета" ввести текст
        В поле "Дата повестки" выбрать значение из выпадающего списка
        Нажать кнопку "Заказать"

        Шаг 4. Переход в раздел "Отчеты"
        Найти и Кликнуть по наименованию отчета
        Нажать кнопку-ссылку "Скачать"
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
            # Осуществить вход в систему под учетной записью
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. МИО. Протокол отказа'):
        try:
            # Перейти во вкладку "МИО.Протокол.Отдел отказа"
            browser.get("http://10.5.127.12/web/mio_decline_protocol")
            time.sleep(6)
            # Нажать кнопку "Протокол отказов"
            browser.xpath(".//*[@id='protocolLandsReportXls']").click()
            time.sleep(6)
            # В поле "Номер отчета" ввести текст
            browser.xpath("//input[@name='protocolNumber']").send_keys(u'000000Тест')
            time.sleep(3)
            # В поле "Дата повестки" выбрать значениe из выпадающего списка
            browser.select_option(".//*[@id='noticeDate']/select",'10.07.2019')
            # Нажать кнопку "Заказать"
            xp = ".//*[@id='confirm']"
            browser.xpath(xp, eager=True)[9].click()
            # browser.xpath("html/body/div[17]/div/div/div[3]/button[1]").click()
            # Нажать кнопку "Закрыть"
            browser.xpath("html/body/div[20]/div/div/div[3]/button").click()
            # browser.modal_close()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Отчеты'):
        try:
            # Перейти в раздел "Отчеты"
            browser.hover_and_click("html/body/nav/div/div[2]/ul/li[3]/a", "html/body/nav/div/div[2]/ul/li[3]/a")
            # browser.get("http://10.5.127.12/web/jobs")
            time.sleep(3)
            # В поисковом поле ввести название отчета и нажать кнопку "Поиск"
            browser.xpath(".//*[@id='searchInput']").send_keys(u'000000Тест')
            browser.xpath(".//*[@id='searchButton']").click()
            time.sleep(4)
            # Выбрать найденный отчет и скачать его
            browser.xpath("html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]").click()
            time.sleep(5)
            browser.xpath(".//*[@id='outFile-card']/a").click()
            time.sleep(3)
            browser.xpath(".//*[@id='formCardJob']/div[3]/button[5]").click()
            browser.xpath("//a[@title='Выйти']").click()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

