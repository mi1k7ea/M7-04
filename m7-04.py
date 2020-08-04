# coding=utf-8

import os

from lib.banner import show_banner
from lib.input_parser import input_parse
from flash_xss_scanner import FlashXSSScanner
from flash_csrf_scanner import FlashCSRFScanner

def main():
    show_banner()
    params = input_parse()

    # 识别扫描类型，根据输入选择进行Flash XSS或Flash CSRF扫描
    if params.type.lower() == "xss":
        print("[*]Start to scan Flash XSS vulnerability...")
        scanner = FlashXSSScanner(os.getcwd() + "/tmp", params.file)
        scanner.scan()
    elif params.type.lower() == "csrf":
        print("[*]Start to scan Flash CSRF vulnerability...")
        scanner = FlashCSRFScanner(params.url)
        scanner.scan()

    print("[*]Finished.")

if __name__ == '__main__':
    main()
