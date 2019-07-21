# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType



def test_4(browser, pdf_file):
    """
Сценарий 1. Сценарий движения карточки Основного отдела, снятие с учета/Итоговая повестка/Протокол сформирован
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

    with allure.step('Шаг 3. Заполнить карточку физического лица в новой карточке'):
        try:
            # Начать заполнение новой карточки
            browser.new_card()
            # Заполнить адрес в новой карточке
            browser.select_adress()
            # ФИО
            browser.xpath('//input[@name="applicantsLC"]').send_keys(u'Тестов тест тестович')
            # Физическое лицо
            browser.xpath('//input[@id="individual"]').click()
            # Кадастровый номер
            browser.xpath("//input[@name='cadastralNumberLC']").send_keys("50:00:000000:00")
            # Предмет рассмотрения
            browser.select_value("//*[@id='subjectOfConsiderationLC']", 3)
            # Площадь квадратных метров
            browser.xpath('//input[@name="areaLC"]').send_keys(u"60")
            # Номер обращения в МФЦ
            browser.xpath('//input[@name="mfcNumberLC"]').send_keys(u"B501-0000000000-10914509")
            # Дата обращения в МФЦ
            browser.set_date_to_xpaths('//input[@name="mfcDateLC"]', u'08022019')
            # Вид решения
            browser.select_value('//*[@id="decisionTypeLC"]', 3)
            # Категория вопроса
            browser.select_text(".//*[@id='questionCategoryLC']", u"Проект ЦИОГВ о проведении торгов (аренда)")
            # Категория земельного участка
            browser.select_value('//*[@id="categoryLC"]', 3)
            # Вид разрешенного использования
            browser.select_value('//*[@id="containerForEditPattern"]', 2)
            # Пояснение ОМС
            browser.xpath('//textarea[@name="explanationsLC"]').send_keys(u'Тест пояснения ОМС')
            # Пояснение МИО
            # browser.xpath('//textarea[@name="explanationsMioLC"]').send_keys(u'Тест пояснения МИО')
            # Загрузить документ
            browser.doc_upload('//input[@name="attachments"]', pdf_file)
            # Далее
            browser.go_next()
            # Модальное окно "Похожие объекты"
            # browser.modal_ok()
            # Сохранить текущее состояние карты для презентации
            #TODO тест упал тут
            browser.save_map()
            # Получить номер карточки
            browser.get_claim_number()
            # Создает карточку и сохраняет ее номер
            new_card = browser.save_card()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Найти новую созданную карточку и открыть ее, отправить на открытую карточку МВК'):
        try:
            browser.open_new_card(new_card)
            browser.send_to_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 5. Перейти вд ругую УЗ и согласовать по умолчанию'):
        try:
            browser.end_session()
            time.sleep(5)
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            #TODO Сверьясо со сценарием, тут что-то не так. Карточку неудается найти вразделе.
            browser.open_new_card(new_card)
            browser.xpath('//a[@href="#tabVoting_land"]').click()
            browser.xpath('.//*[@id="accepted_conditionally"]').click()
            browser.modal_confirm()

            time.sleep(3)
            browser.xpath('//textarea[@name="modalTextArea"]').send_keys('Тест')
            time.sleep(3)
            browser.xpath('html/body/div[8]/div/div/div[3]/button[1]').click()
            time.sleep(3)
            browser.xpath('html/body/div[4]/div/div/form/div[1]/button[1]').click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 6. Перейти в другую УЗ и снять с голосования'):
        try:
            browser.end_session()
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            browser.get('http://10.5.127.12/web/voting')
            browser.open_new_card(new_card)
            browser.remove_from_voting()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 7. Назначить исполнителя'):
        try:
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.open_new_card(new_card)
            browser.set_executant()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 8. Отправить на доработку'):
        try:
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.open_new_card(new_card)
            browser.send_to_rework()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 9. Редактировать карточку ио тправить на МВК'):
        try:
            browser.get('http://10.5.127.12/web/oms_rework')
            browser.open_new_card(new_card)
            browser.edit_card()
            browser.xpath('//textarea[@name="draftDecisionLC"]').send_keys(u'Тест')
            browser.save_after_edit()
            browser.send_to_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 10. Отправить на согласование и включить в поветку'):
        try:
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.open_new_card(new_card)
            browser.send_to_consideration()
            browser.open_new_card(new_card)
            browser.send_to_formed_notice()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 11. Вынести на комиссию'):
        try:
            browser.get('http://10.5.127.12/web/mio_formed_notice')
            browser.set_date('//input[@id="noticeDate"]')
            browser.open_new_card(new_card)
            browser.send_to_commission()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 12. Сформировать протокол'):
        try:
            browser.get('http://10.5.127.12/web/mio_final_notice')
            browser.set_date('//input[@id="noticeDate"]')
            browser.open_new_card(new_card)
            browser.formed_protocol()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 13. Сводное заключение'):
        try:
            browser.get('http://10.5.127.12/web/mio_protocol')
            browser.open_new_card(new_card)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise
