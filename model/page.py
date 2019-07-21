# coding=utf-8

""" Основной Page Object от которого инициализируются все остальные Page Object классы
"""
import calendar
import re
import time
import warnings

from datetime import date, timedelta, datetime
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwrapper import SeleniumWrapper
from selenium.common.exceptions import WebDriverException, InvalidElementStateException, NoSuchElementException


class Page(SeleniumWrapper):
    def _move_to_element(self, xpath):
        """ Переносит фокус на необходимый web элемент
        """
        time.sleep(0.5)
        action = ActionChains(self._wrapped)
        element = self.xpath(xpath)
        action.move_to_element(element).perform()

    def scroll(self, x=0, y=500):
        """ По умочланию скроллит страницу вниз на 500 пикселей """
        self.scroll_by(x, y)

    def scroll_to_element(self, xpath):
        """
        Скролит страницу к элементу
        :param xpath: xpath элемента
        """
        element = self.xpath(xpath).unwrap
        x = int(element.location_once_scrolled_into_view['x'])
        y = int(element.location_once_scrolled_into_view['y'])
        self.scroll_to(x, y)

    def cur_date_sub(self, days, months=0, years=0):
        """
        Вычитает из текущей даты указанное количество дней, месяцев и лет
        :param days: дни
        :param months: месяцы
        :param years: года
        :return:  дата в формате дд.мм.гггг
        """
        curdate = self.__add_months(date.today() - timedelta(days=days), -months)
        curdate = date(curdate.year - years, curdate.month, curdate.day)
        return curdate.strftime("%d.%m.%Y")

    def cur_date_add(self, days=0, months=0, years=0):
        """
        Добавляет к текущей дате указанное количество дней, месяцев и лет
        :param days: дни
        :param months: месяцы
        :param years: года
        :return:  строка в формате дд.мм.гггг
        """
        curdate = self.__add_months(date.today() + timedelta(days=days), months)
        curdate = date(curdate.year + years, curdate.month, curdate.day)
        return curdate.strftime("%d.%m.%Y")

    def __add_months(self, sourcedate, months):
        """
        Добавляет месяц к текущей дате
        :param sourcedate: начальная дата
        :param months: добавляемое количество месяцев
        :return: дата в формате дд.мм.гггг
        """
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return date(year, month, day)

    @staticmethod
    def get_tag_number(element):
        """ Получает номер элемента из тега

            num = get_tag_number('div[3]')
        """
        reg = re.compile(r'(\d+)')
        num = int(re.search(reg, element).group())
        return num

    def clear_xpath(self, xpath):
        """ Пытается очистить форму ввода
        """
        try:
            self.xpath(xpath).clear()
        except InvalidElementStateException:
            pass

    def clear_element(self, element):
        """ Очищает элемент
        """
        try:
            element.clear()
        except InvalidElementStateException:
            pass

    def force_click(self, xpath):
        """ Кликает на первый элемент из всех элементов в списке
        """
        elements = self.xpath(xpath, eager=True)
        for el in elements:
            try:
                if el.is_displayed():
                    el.click(timeout=1)
                    return
            except WebDriverException:
                continue


    def is_element_exists(self, element):
        """ Принимает webdriver element и проверяет что он существует

            Возвращает сам элемент
        """
        try:
            if element.is_enabled() and element.is_displayed():
                return element
            else:
                return False
        except WebDriverException:
            return False

    def is_exists(self, xpath, eager=False):
        try:
            if eager:
                if self.xpath(xpath, eager=eager, timeout=1).size:
                    return True
                else:
                    return False
            else:
                return self.xpath(xpath, timeout=1).is_displayed()
        except WebDriverException:
            return False

    def is_exists_send_keys(self, xpath, text, clear=True):
        """ Проверяет, есть ли такой элемент
            Если есть, то очишает форму и вводит текст
            :param clear - Если True, то попытается перед вводом очистить форму
        """
        if self.is_exists(xpath):
            if clear:
                try:
                    self.xpath(xpath).clear()
                except InvalidElementStateException:
                    pass
            self.xpath(xpath).send_keys(text)

    def is_exists_element_send_keys(self, element, text, clear=True):
        """ Очищает webdriver элемент и вводит текст
        """
        if self.is_element_exists(element):
            if clear:
                self.clear_element(element)
            element.send_keys(text)

    def is_exists_element_send_keys(self, element, text, clear=True):
        """ Очищает webdriver элемент и вводит текст
        """
        if self.is_element_exists(element):
            if clear:
                self.clear_element(element)
            element.send_keys(text)

    def element_is_editable(self, el):
        return (el.get_attribute("readonly") == "false" or bool(el.get_attribute("readonly")) == False) \
               and el.is_enabled() and el.is_displayed()

    def send_keys_to_xpaths(self, xpaths, text, clear=True):
        """ вводит текст в поля указанные в списке
        """
        xpaths = " | ".join(xpaths)

        try:
            elements = self.xpath(xpaths, eager=True, timeout=0.5)
        except NoSuchElementException:
            elements = []
        for el in elements:
            if self.element_is_editable(el):
                if clear:
                    self.clear_element(el)
                el.send_keys(text)

    def set_date_to_xpaths(self, xpaths, date):
        """ вводит дату в поля указанные в списке
        """
        # xpaths = " | ".join(xpaths)

        try:
            elements = self.xpath(xpaths, eager=True, timeout=0.5)
        except NoSuchElementException:
            elements = []
        for el in elements:
            if self.element_is_editable(el):
                el.clear()
                el.send_keys(date)



    def wait_for_main_window(self):
        timeout = 5
        while True:
            try:
                self.xpath("//div[contains(@class,'my-Modal')]", eager=True, timeout=0.5)
            except:
                break
            time.sleep(0.5)
            timeout -= 0.5
            if timeout < 0:
                break

    def get_future_date(self, days):
        result = date.today() + timedelta(days=days)
        return result.strftime("%d.%m.%Y")

    """Вспомогательные  методы"""

    def file_apply(browser, xpath):
        """ Нажимает на кнопку
            Использовать эту версию

            xpath - обычно это xpath на iframe


        """

        browser.switch_to.frame(browser.xpath(xpath).unwrap)
        browser.xpath("//input[@value='Использовать эту версию']").click(timeout=90)
        browser.switch_to.default_content()

    def street_chosen_click(browser, xpath, streen_name):
        """ Заполняет форму выбора улицы
            :param browser
            :param xpath - xpath формы
            :param streen_name - название улицы

        """

        browser.xpath(xpath + '/a/span').click(presleep=2, postsleep=2)
        browser.xpath(xpath + '/div/div/input').send_keys(streen_name)
        browser.xpath(xpath + '/div/ul').click(presleep=1)

    def first_option_click(browser, xpath):
        """ Кликает на первую опцию из списка
        """

        browser.xpath(xpath + '/a/span').click(postsleep=1)
        browser.xpath(xpath + '/div/ul/li[2]').click()

    def current_month():
        months = {
            "January": u'Январь',
            "Febuary": u'Февраль',
            "March": u'Март',
            "April": u'Апрель',
            "May": u'Май',
            "June": u'Июнь',
            "July": u'Июль',
            "August": u'Август',
            "September": u'Сентябрь',
            "October": u'Октябрь',
            "November": u'Ноябрь',
            "December": u'Декабрь'
        }
        mydate = datetime.datetime.now().strftime("%B")
        return months[mydate]

    def switch_to_next_window(browser, close_others=False):
        """ Переключается на следующее окно
            Закрывает все другие окна
            Возвращает главное окно
        """
        current_window = browser.current_window_handle
        windows = browser.window_handles
        for window in windows:
            if window != current_window:
                browser.switch_to.window(window)
                break
            else:
                if close_others:
                    browser.close()
        return current_window

    def switch_to_frame(browser, xpath):
        """ Делает свитч на frame"""
        browser.switch_to.frame(browser.xpath(xpath).unwrap)

    def switch_to_active_element(self):
        """ Deprecated use driver.switch_to.active_element
        """
        warnings.warn("use driver.switch_to.active_element instead",
                      DeprecationWarning, stacklevel=2)
        return self._switch_to.active_element

    def is_element_present(browser, xpath, eager=False):
        try:
            elements = browser.xpath(xpath, eager=eager, timeout=1)
            return elements
        except NoSuchElementException:
            return False

    def send_keys_periodic(browser, xpath, keys):
        for k in keys:
            browser.xpath(xpath).send_keys(k)
            time.sleep(0.2)

class NotFound(Exception):
    pass
