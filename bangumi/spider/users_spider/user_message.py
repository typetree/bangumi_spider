# *_*coding:utf-8 *_*
# author: hoicai
from bs4 import BeautifulSoup
import requests

from bangumi.constants import url_constants

user_code = 'zisudaki'
user_url = url_constants.get_user_url(user_code)
user_hearders = url_constants.get_user_headers(user_code)

response = requests.get(user_url, headers=user_hearders)
response.encoding='utf-8'
soup = BeautifulSoup(response.text, 'lxml')

