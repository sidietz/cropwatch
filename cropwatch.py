#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import copy
import concurrent.futures
import requests as rq
import pandas as pd
from time import sleep, time
from lxml import html
import csv

from constants import H, RQ_DATA_0, RQ_DATA_1, RQ_DATA_2, RQ_DATA_3, COOKIES

PLZS = []

with open('plz.csv', newline='') as f:
    reader = csv.reader(f)
    PLZS = [i[0] for i in list(reader)]


def save_grants_to_csv(grant_dict, jahr):
    grants_df = pd.DataFrame.from_dict(grant_dict, orient='index')
    grants_df.reset_index(drop=True, inplace=True)
    grants_df.fillna(value=0, inplace=True)
    grants_df[grants_df.columns[5:]] = grants_df[grants_df.columns[5:]].astype(int)
    grants_df.to_csv(str(jahr) + "_grants" + ".csv")
    return True


def extract_grants(jahrtype, jahr):
    dataframe = pd.read_csv(str(str(jahr) + "_ids" + ".csv"))
    dataframe_2 = dataframe.loc[:, "pid"]
    pid_list = dataframe_2.values.tolist()
    result_dict = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=8*16) as executor:
        future_to_grantlist = {executor.submit(adv_parser_by_pid, pid, jahrtype): pid for pid in pid_list}
        for future in concurrent.futures.as_completed(future_to_grantlist):
            pid = future_to_grantlist[future]
            error, grant = future.result()
            if error:
                with open("error.log", "a") as error_log:
                    error_log.write(str(pid) + "\n")
            else:
                result_dict[pid] = grant

    save_grants_to_csv(result_dict, jahr)
    # print(list(map(list, dataframe_2.values)))
    # https://stackoverflow.com/questions/33157522/create-pandas-dataframe-from-dictionary-of-dictionaries

    return 0


def save_ids_to_csv(array_list, jahr):
    columns = ["pid"]
    dataframe_3 = pd.DataFrame(array_list, columns=columns)
    dataframe_3.drop_duplicates(["pid"], inplace=True)
    dataframe_3.reset_index(drop=True, inplace=True)
    dataframe_3.to_csv(str(str(jahr) + "_ids" + ".csv"))
    return True


def get_meta_data(response):
    count_start = response.find('<span>')
    raw_count = response[count_start + 22:count_start + 27]
    try:
        count = int(raw_count.strip())
    except ValueError:
        return 0, 0
    view_count_start = response.find('<input id="hCount" name="viewCount" type="hidden" value="', 0)
    view_count_end = response.find('/>', view_count_start)
    raw_v_count = response[view_count_start + 57:view_count_end - 1]
    view_count = int(raw_v_count)
    return view_count, count


def extract_ids(jahrtype, jahr):
    name_list = list()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8*16) as executor:
        future_to_idlist = {executor.submit(adv_from_plz, plz, jahrtype): plz for plz in PLZS}
        for future in concurrent.futures.as_completed(future_to_idlist):
            plz = future_to_idlist[future]
            tmp_list = future.result()
            name_list.extend(tmp_list)

    save_ids_to_csv(name_list, jahr)
    return 0


def handle_request2(cookie, data):
    successful = False

    while (not successful):
        try:
            request = rq.post('https://www.agrar-fischerei-zahlungen.de/Suche', headers=H, cookies=cookie, data=data)
            successful = True
        except rq.exceptions.ConnectionError:
            print("Server to many connections error detected, sleeping!")
            sleep(3)

    return request

def handle_request(cookie, data):
    return handle_request2(cookie, data)


def adv_parser_ids(response):
    tree = html.document_fromstring(response)
    pid_list = list(map(str, tree.xpath('/html/body/div[5]/div[3]/div/form[2]/table/tbody/tr[*]/th/button/@value')))
    return pid_list


def amount_to_cent(amount):
    amount = amount[:-2]
    euro = amount[:-3]
    euro = int(euro.replace('.', ''))
    cent = int(amount[-2::])
    return euro*100 + cent


def adv_parser_by_pid(pid, yeartype):
    RQ_DATA_2[0] = ('jahr', yeartype)
    RQ_DATA_2[23] = ('showBeg', pid)

    grant = {"pid": pid, "Gesamt": ""}

    tree = html.document_fromstring(handle_request(COOKIES, RQ_DATA_2).text)
    try:
        metadata = str(tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/h2/text()')[0])  # name + ...
    except IndexError:
        print("fault pid detected!")
        print(pid)
        return True, grant
    raw_measures = list(map(str, tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/h3[*]/text()')))  # name of grant
    raw_amounts = list(map(str, tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/p[*]/span/text()')))  # amount of money
    raw_amounts = raw_amounts[:-2]  # drop unrelevant rows

    measure_list = list(map(lambda x: x[2:], raw_measures))
    measure_list.append('Gesamt')

    name, location = metadata.split('–')
    location = location[1:-2]
    plz, place = location.split(' ', 1)

    grant["name"] = name[:-1]
    grant["plz"] = int(plz)
    grant["place"] = place

    amounts = list(map(amount_to_cent, raw_amounts))

    for measure, amount in zip(measure_list, amounts):
        grant[measure] = amount

    return False, grant


def adv_from_plz(plz, jahr):
    try:
        q = int(plz[1:])
    except ValueError:
        return ["FATAL ERROR!"]

    RQ_DATA_0[2] = ('plz', str(plz))
    i = 1
    request_0 = handle_request(COOKIES, RQ_DATA_0)
    text = request_0.text
    view_count, count = get_meta_data(text)

    if count == 0:
        return []

    RQ_DATA_1[0] = ('jahr', jahr)
    RQ_DATA_1[3] = ('plz', str(plz))
    RQ_DATA_1[12] = ('viewCount', view_count)
    RQ_DATA_1[13] = ('viewCountBeg', count)
    RQ_DATA_1[18] = ('count', view_count)
    RQ_DATA_1[19] = ('countBeg', count)

    rq_data2 = copy.deepcopy(RQ_DATA_1)

    request_1 = handle_request(COOKIES, rq_data2)
    name_list = adv_parser_ids(request_1.text)

    while i < math.ceil(view_count/50):
        rq_data2[22] = ('seite', str(i))

        request_1 = handle_request(COOKIES, rq_data2)
        text = request_1.text
        tmp_list = adv_parser_ids(text)

        if not tmp_list:
            break
        name_list.extend(tmp_list)
        i += 1

    return name_list


s1 = time()
testyear = 2018
extract_ids("vorjahr", testyear)
s2 = time()
print(f'e ids for {testyear} took {s2 - s1}')
extract_grants("vorjahr", testyear)
s3 = time()
print(f'grants for {testyear} took {s3 - s2}')

testyear = 2019
extract_ids("jahr", testyear)
s4 = time()
print(f'e ids for {testyear} took {s4 - s3}')
extract_grants("jahr", testyear)
s5 = time()
print(f'grants for {testyear} took {s5 - s4}')

print(f'total {s5 - s1}')
