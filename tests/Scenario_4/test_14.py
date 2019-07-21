# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType


def test_14(browser, pdf_file):
    """
    Сценарий 13. Выгрузка отчета "Итоговая повестка"
        Шаг 1. Загрузка главной страницы:
        открыть страницу http://10.5.127.12/web

        Шаг 2. Авторизация:
        Вести логин и пароль - FilippovYM, FilippovYM

        Шаг 3. Перейти во вкладку "МИО.Итоговая повестка"
        В поле "Дата ближайшей повестки" указать дату
        Нажать кнопку "Отчет Итоговая повестка"
        Нажать кнопку "Закрыть"

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
            browser.login_test_mvk('FilippovYM', 'FilippovYM')
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. МИО. Итоговая повестка'):
        try:
            browser.hover_and_click(".//*[@id='executantsPage']/a", ".//*[@id='executantsPage']/ul/li[5]/a")
            # browser.get('http://10.5.127.12/web/mio_final_notice')
            time.sleep(3)
            browser. set_date(".//*[@id='noticeDate']")
            time.sleep(5)
            browser.xpath(".//*[@id='finalNoticeLandsReportXls']").click()

            xp = ".//*[@id='close']"
            browser.xpath(xp, eager=True)[14].click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Переход в раздел "Отчеты"'):
        try:
            #TODO тест упал тут
            #TODO пример плохого локатора
            browser.hover_and_click("/html/body/nav/div/div[2]/ul/li[2]/a", "/html/body/nav/div/div[2]/ul/li[2]/a")
            # browser.get('http://10.5.127.12/web/jobs')
            time.sleep(3)
            browser.xpath(".//*[@id='startTimestamp']/div[1]").click()
            time.sleep(2)
            browser.xpath(".//*[@id='startTimestamp']/div[1]").click()
            time.sleep(2)
            browser.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[3]").click()
            browser.xpath(".//*[@id='outFile-card']/a").click()
            browser.xpath('//*[@id="formCardJob"]/div[3]/button[5]').click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise


