from bs4 import BeautifulSoup
import requests
import re
import os
import json

s = requests.Session()


def login():

    login = s.get("https://binusmaya.binus.ac.id/login/")

    soup = BeautifulSoup(login.text, 'html.parser')

    username = soup.find_all('input')[0]['name']
    password = soup.find_all('input')[1]['name']
    button = soup.find_all('input')[2]['name']

    serial = soup.select('script')[-2]['src'].split('/')[2]
    script_randomer = s.get(
        "https://binusmaya.binus.ac.id/login/" + serial)

    name1 = re.findall(r'name="[A-Za-z0-9%_]*"',
                       script_randomer.text)[0].split('name=')[1][1:-1]

    name2 = re.findall(r'name="[A-Za-z0-9%_]*"',
                       script_randomer.text)[1].split('name=')[1][1:-1]

    value1 = re.findall(r'value="[A-Za-z0-9%_]*"',
                        script_randomer.text)[0].split('value=')[1][1:-1]

    value2 = re.findall(r'value="[A-Za-z0-9%_]*"',
                        script_randomer.text)[1].split('value=')[1][1:-1]

    # Put your credentials
    f = open("creds.txt", "r").read().split("\n")

    data = {
        username: f[0],
        password: f[1],
        button: "Login",
        name2: value2
    }
    login = s.post("https://binusmaya.binus.ac.id/login/sys_login.php",
                   data=data)


def get_assignment():

    header = {
        "Referer": "https://binusmaya.binus.ac.id/newStudent/"
    }

    api_course = s.get("https://binusmaya.binus.ac.id/services/ci/index.php/student/init/getCourses",
                       headers=header)
    print(api_course.text)


login()
get_assignment()
