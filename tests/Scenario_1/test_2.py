# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_2(browser, pdf_file):
    """
Сценарий 1. Сценарий движения карточки Основного отдела, снятие с учета/Итоговая повестка/Протокол сформирован
        """


    with allure.step('Шаг 1. Загрузка главной страницы'):
        try:
            # Открыть тестовый стенд МВК
            browser.open_test_mvk()

            # Залогиниться на тестовый стенд МВК
            browser.login_test_mvk('MekhdievZ', 'QAtest05')

            # Начать заполнение новой карточки
            browser.new_card()
            browser.find_element_by_xpath("html/body/div[2]/div[2]/div[4]/div/div/div[1]/button[1]").click(presleep=10)
            browser.xpath('html/body/div[4]/div/div/form').click()

            # Заполнить адрес в новой карточке
            browser.select_adress()

            # Заполнить карточку физического лица в новой карточке
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
            browser.xpath('//textarea[@name="explanationsMioLC"]').send_keys(u'Тест пояснения МИО')
            # Загрузить документ
            browser.doc_upload('//input[@name="attachments"]', pdf_file)
            # Далее
            browser.go_next()

            # Модальное окно "Похожие объекты"
            browser.modal_ok()
            # Сохранить текущее состояние карты для презентации
            browser.save_map()
            # Получить номер карточки
            browser.get_claim_number()
            # Создает карточку и сохраняет ее номер
            new_card = browser.save_card()
            # Найти новую созданную карточку и открыть ее
            browser.select_new_card(new_card)

            # Отправить на открытую карточку МВК
            browser.send_to_mvk()

            #Перейти в раздел "Голосование", Найти новую карточку и снять с голосования
            browser.get('http://10.5.127.12/web/voting')
            browser.open_new_card(new_card)
            browser.remove_from_voting()

            #Перейти во вкладку "МИО.Основной отдел", найти карточку и назначить ответственного
            browser.get('http://10.5.127.12/web/mio_main_dept')
            # browser.open_new_card(new_card)
            browser.open_new_card(new_card)
            browser.set_executant()

            #Отправить на доработку
            browser.open_new_card(new_card)
            browser.send_to_rework()

            #Редактировать карточку
            browser.open_new_card(new_card)
            browser.edit_card()
            browser.xpath('//textarea[@name="draftDecisionLC"]').send_keys(u'Тест')
            browser.save_after_edit()

            #Отправить на МВК
            browser.get('http://10.5.127.12/web/oms_rework')
            browser.open_new_card(new_card)
            browser.send_to_mvk()

            #Перейти во вкладку МИО Основной отдел и отправить на согласование
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.open_new_card(new_card)
            browser.send_to_consideration()

            #Включить в повестку
            browser.open_new_card(new_card)
            browser.send_to_formed_notice()

            #Перейти во вкладку МИО.Формируемая повестка
            browser.get('http://10.5.127.12/web/mio_formed_notice')
            browser.set_date('//input[@id="noticeDate"]')
            #TODO тест упал тут
            browser.open_new_card(new_card)
            browser.send_to_commission()

            # Выйтит из учетной записи
            browser.end_session()

            # Войти в УЗ для формирования итоговой повестки
            browser.login_test_mvk('LebedAA', 'LebedAA')

            # Перейти в раздел "МИО итоговая повестка и Сформировать протоколом
            browser.get('http://10.5.127.12/web/mio_final_notice')
            browser.set_date('//input[@id="noticeDate"]')
            browser.open_new_card(new_card)
            browser.formed_protocol()

            # Перейти во вкладку "МИО. Сводное заключение"
            browser.get('http://10.5.127.12/web/mio_protocol')
            time.sleep(7)
            browser.open_new_card(new_card)

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise





