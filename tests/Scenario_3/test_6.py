# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_6 (browser, pdf_file):
    """
     Сценарий 7. Выгрузка отчета "Сводное заключение":

        Шаг 1. Загрузка главной страницы:
        открыть страницу http://10.5.127.12/web

        Шаг 2. Авторизация:
        Вести логин и пароль - MekhdievZ, QAtest05

        Шаг 3. Переход во вкладку "МИО.Сводное заключение":
        Нажать кнопку "Сводное заключение" и заполнить поля тестовыми значениями:
        Номер отчета - отчет тестовый 123;
        Тип повестки - Очная;
        Дата повестки
        Нажать "Заказать", "Закрыть"

        Шаг 4. Переход в раздел "Отчеты":
        В поисковой строке ввести наименоввание отчета - отчет тестовый 123
        Кнопка "Поиск" - отчет найден.
        Детализировать строку с найденным отчетом - нажать кнопку "Скачать"
        Отчет скачен.
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
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. МИО. Сводное заключение'):
        try:
            browser.hover_and_click("/html/body/nav/div/div[2]/ul/li[2]/a", "/html/body/nav/div/div[2]/ul/li[2]/ul/li[6]/a")
            # browser.get('http://10.5.127.12/web/mio_protocol')
            time.sleep(12)
            browser.xpath("//button[@id='protocolLandsReportXls']").click()
            time.sleep(9)
            browser.xpath("//input[@name='protocolNumber']").send_keys("отчет тестовый 123")
            time.sleep(5)
            browser.xpath(".//*[@id='noticeDate']/select").click(presleep=5)
            browser.find_element_by_xpath('//*[@id="noticeDate"]/select/option[15]').click()
            xp = ".//*[@id='confirm']"
            browser.xpath(xp, eager=True)[9].click()
            time.sleep(3)
            xp = ".//*[@id='close']"
            browser.xpath(xp, eager=True)[15].click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Переход в раздел "Отчеты"'):
        try:
            browser.hover_and_click("html/body/nav/div/div[2]/ul/li[3]/a", "html/body/nav/div/div[2]/ul/li[3]/a")
            # browser.get('http://10.5.127.12/web/jobs')
            time.sleep(5)
            browser.xpath(".//*[@id='searchInput']").send_keys("отчет тестовый 123")
            browser.xpath(".//*[@id='searchButton']").click()
            time.sleep(3)
            browser.css(".td_jobTitle.resizable.ui-resizable").click()
            time.sleep(3)
            browser.xpath('//*[@id="outFile-card"]/a').click()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise



