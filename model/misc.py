# coding=utf-8

"""Вспомогательные  методы"""
import datetime
import json

import requests
from selenium.common.exceptions import NoSuchElementException
import time


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

def claim_compare(etalon_claim, new_claim):
    #Данный метод отправляет запрос в РЛДД после чего конвертирует заявку в справочник содержащий ключи и значения из
    # заявки
    print(new_claim)
    print(etalon_claim)
    json_data = requests.get(etalon_claim)
    data = {"": "", "": ""}  # python словарь
    parsed_json = json.loads(json_data.content)
    if 'required' in parsed_json[u'fields']:
        del parsed_json[u'fields'][u'required']
    # распаковываем
    try:
        search(parsed_json[u'fields'][u'sequenceValue'])
    except:
        print ('no key value')

    json_data2 = requests.get(new_claim)
    data = {"": "", "": ""}  # python словарь
    parsed_json2 = json.loads(json_data2.content)  # распаковываем
    if 'required' in parsed_json2[u'fields']:
        del parsed_json2[u'fields'][u'required']
    try:
        search(parsed_json2[u'fields'][u'sequenceValue'])
    except KeyError:
        print ('no key value')
    result = dict_compare(parsed_json, parsed_json2)

    print (result)

    #Если кол-во неравных элементов больше нуля тест считается провалившимся
    if len(result) == 0:
        pass
    else:
        print(len(result))
        print(result)
        raise Exception('Error, stopping')

def dict_compare(parsed_json, parsed_json2):
    #Данный метод сравнивает ключи и значения заявки
    d1_keys = set(parsed_json.keys())
    d2_keys = set(parsed_json2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : [parsed_json[o], parsed_json2[o]] for o in intersect_keys if parsed_json[o] != parsed_json2[o]}
    same = set(o for o in intersect_keys if parsed_json[o] == parsed_json2[o])
    error_list = list()
    try:
        del modified ['_links']
    except KeyError:
        pass
    try:
        del modified ['claimCreate']
    except KeyError:
        pass
    try:
        del modified ['createDate']
    except KeyError:
        pass
    try:
        del modified ['creationDate']
    except KeyError:
        pass
    try:
        del modified ['activationDate']
    except KeyError:
        pass
    try:
        del modified ['currStatus']
    except KeyError:
        pass
    try:
        del modified ['customClaimNumber']
    except KeyError:
        pass
    try:
        del modified ['id']
    except KeyError:
        pass
    try:
        del modified ['lastModified']
    except KeyError:
        pass
    try:
        del modified ['personsInfo']
    except KeyError:
        pass
    try:
        del modified ['persons']
    except KeyError:
        pass
    try:
        del modified ['daysToDeadline']
    except KeyError:
        pass
    try:
        del modified['deadlineDate']
    except KeyError:
        pass
    try:
        del modified['required']
    except KeyError:
        pass
    try:
        del modified['claimId']
    except KeyError:
        pass
    try:
        del modified['registrationAddressId']
    except KeyError:
        pass
    try:
        del modified['currIdentityDocId']
    except KeyError:
        pass
    try:
        del modified['href']
    except KeyError:
        pass
    try:
        del modified['statusDate']
    except KeyError:
        pass
    try:
        del modified['closed']
    except KeyError:
        pass
    try:
        del modified['sentToDepartmentDate']
    except KeyError:
        pass
    try:
        del modified['href']
    except KeyError:
        pass
    try:
        del modified['existingID']
    except KeyError:
        pass

    # return modified, same, added, removed
    return modified

def search(myDict):
    #Данный метод удаляет все референсы из заявок, т.к. они всегда будут уникальными для каждоый новой заявки
    # пример - адрес
    i=0
    for row in myDict:
        try:
            if row[u'required'] == False:
                del myDict[i][u'required']

            if row[u'type'] == 'REF' or row[u'type'] == 'URL':
                del myDict[i][u'type']

            if 'sequenceValue' in  myDict[i]:
                search(row['sequenceValue'])

            if 'value' in myDict[i]:
                if 'url' in myDict[i]['value']:
                    del myDict[i]['value']['url']
            else:
                continue
        except Exception as e:
            print('no stringId in dictionary')
        finally:
            i+=1
