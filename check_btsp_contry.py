import json
import re
import urllib

import requests


user_list = ["test489@yopmail.com",
"knoxportal.qa.1456963466760@vandevlab.com",
"testoffline1243@yopmail.com",
"seap.qa.1457473143542@vandevlab.com",
"seap.qa.1456960749497@vandevlab.com",
"seap.qa.1456959065832@vandevlab.com",
"seap.qa.1456944751754@vandevlab.com",
"seap.qa.1456954037915@vandevlab.com"]

def main_code():
    # file = "country.txt"
    #
    # with open(file, "r") as cfile:
    #     cstring = cfile.readline()
    #
    # regex = '[A-Z]{2}'
    # country_list = re.findall(regex, cstring)
    #
    # for country in country_list:
    #     send_data_to_btsp(country)
    for user in user_list:
        send_data_to_btsp(user)

def send_data_to_btsp(user):
    btsp_url = 'http://btsp.samsunggsbn.com/b2t/rs/common/kamif/create'

    btsp_data = {
        "countryCd": "US",
        "accountNm": "Company Name Inc.",
        "zipcd": "",
        "stateNm": "BC",
        "cityNm": "Vancouver",
        "streetNm": "123 Fake St.",
        "telNo": "",
        "telNo2": "",
        "telNo3": "",
        "firstnm": "Jack",
        "midnm": "",
        "lastnm": "Black",
        "emailAddr": user,
        "userTelNo": "",
        "userTelNo2": "",
        "userTelNo3": "",
        "cellphoneNo": "",
        "knoxLicense": "",
        "seapTier": "",
        "tenantUid": "8e125a2c-3fbe-11e5-9cea-069706ce84ed",
        "userUid": "8f106fa9-3fbe-11e5-9cea-069706ce84ed",
        "tncAccepted": "yes",
        "privacyPolicyAccepted": "yes"
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    jdata = json.dumps(btsp_data)

    btsp_resp = requests.post(btsp_url, data=jdata, headers=headers)

    print("request response code is %s" % btsp_resp.status_code)
    # print("Get response from BTSP, country is %s, status code is %s" % (
    # user, json.loads(urllib.unquote(btsp_resp.text).decode('utf8'))["statusCode"]))
    print("Get response from BTSP, user is %s, status code is %s" % (
    user, json.loads(urllib.unquote(btsp_resp.text).decode('utf8'))))

# send_data_to_btsp("DZ")
main_code()