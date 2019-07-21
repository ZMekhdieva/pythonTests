# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType


def test_9(browser, pdf_file):
    """
        Сценарий 8. Выгрузка отчета "Отчет о суммах площадей ЗУ по типу заявителя"

            Шаг 1. Загрузка главной страницы:
            открыть страницу http://10.5.127.12/web

            Шаг 2. Авторизация:
            Вести логин и пароль - MekhdievZ, QAtest05

            Шаг 3. Переход во вкладку "Отчеты":
            Нажать кнопку "Создать" и заполнить поля тестовыми значениями:
            Тип запроса -  "Отчет о суммах площадей ЗУ по типу заявителя";
            Название отчета - Тестовый отчет 002;
            Дата повестки
            Нажать "Сохранить"

            В поисковой строке ввести наименоввание отчета - Тестовый отчет 002
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
    with allure.step('Шаг 5. Перейти в раздел "Отчеты"'):
        try:
            browser.hover_and_click("html/body/nav/div/div[2]/ul/li[3]/a", "html/body/nav/div/div[2]/ul/li[3]/a")
            # browser.get('http://10.5.127.12/web/jobs')
            browser.xpath("//button[@data-target_modal='#idCardJob']").click()
            time.sleep(2)
            browser.select_option("//select[@id='jobType']", 'Отчет о суммах площадей ЗУ по типу заявителя')
            browser.xpath("//input[@name='reportName-param']").send_keys(u'Тестовый отчет 002')
            browser.xpath("//input[@name='periodBegin-param']").send_keys(u'01012019')
            browser.xpath("//input[@name='periodEnd-param']").send_keys(u'31012019')
            browser.xpath("//button[contains(@class,'btn btn-success btn-sm js-save-card saveJobButton')]").click()
            browser.xpath(".//*[@id='searchInput']").send_keys("Тестовый отчет 002")
            browser.xpath(".//*[@id='searchButton']").click()
            browser.xpath("//td[contains(.,'Тестовый отчет 002')]").click()
            browser.xpath(".//*[@id='outFile-card']/a").click()
            browser.xpath(".//*[@id='idCardJob']").click()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise
