# coding=utf-8

import urllib3
urllib3.disable_warnings()

import re
import requests

from lib.header_generator import get_headers
from lib.conf import FLASH_CSRF_RULE, GET_DOMAIN_VALUE

class FlashCSRFScanner:
    def __init__(self, url):
        self.url = url

    def scan(self):
        # 尝试访问目标域名下的/crossdomain.xml文件
        crossdomain_url = self.url.rstrip("/") + "/crossdomain.xml"
        response = requests.get(url=crossdomain_url, headers=get_headers(), verify=False, timeout=5)

        # 如果目标域名未设置该文件则不存在Flash CSRF
        if response.status_code == 404:
            print("[-]There is no Flash CSRF vulnerability, because the domain doesn't have crossdomain.xml.")
        elif response.status_code == 200:
            content = response.text
            if re.search(FLASH_CSRF_RULE, content):
                print("[+]Found Flash CSRF vulnerability:", crossdomain_url)
            else:
                # 正则匹配响应内容是否为crossdomain.xml相关内容
                domains = re.findall(GET_DOMAIN_VALUE, content)
                if len(domains) > 0:
                    print("[-]The domain value is not equal '*', "
                          "please check if the whitelist domains allow user to upload a Flash file.")
                    print("[*]WhiteList domains:", end=" ")
                    for domain in domains:
                        print(domain, end="  ")
                    print()
                else:
                    print("[-]Can't access crossdomain.xml.")
        else:
            print("[-]Response status code wrong.")
