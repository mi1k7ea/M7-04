# coding=utf-8

import os
import hashlib

from lib.swf_decompiler import decompile_swf
from lib.conf import FLASH_XSS_SINK, FLASH_XSS_SOURCE, FLASH_XSS_MD5, FLASH_XSS_EXP

class FlashXSSScanner:
    def __init__(self, as_dir, swf_file):
        self.as_dir = as_dir
        self.swf_file = swf_file

    # 使用已知存在漏洞的三方swf文件的MD5进行对比检测
    def md5_check(self):
        md5_value = hashlib.md5(open(self.swf_file, 'rb').read()).hexdigest()
        for index in FLASH_XSS_MD5:
            for swf_name in index:
                swf_md5 = index[swf_name]
                if swf_md5 == md5_value:
                    print("[+]Found Flash XSS vulnerability by MD5:", swf_name)
                    print("[+]Exp:", end=" ")
                    for exp in FLASH_XSS_EXP:
                        for name in exp:
                            if name == swf_name:
                                print(exp[name])
                                break
                    return True
        return False

    # 基于source和sink的源码扫描检测，辅助人工排查
    def code_check(self, content, path):
        sources = ""
        sinks = ""
        found = False
        for source in FLASH_XSS_SOURCE:
            if source in content:
                sources += source + "  "
                for sink in FLASH_XSS_SINK:
                    if sink in content:
                        sinks += sink + "  "
                        found = True
        if found:
            print("[+]A Flash XSS vulnerability may exists here, please check it manually.")
            print("[+]File path:", path)
            print("[+]Source:", sources)
            print("[+]Sink:", sinks)
            print("**" * 40)

    def scan(self):
        print("[*]Use MD5 list to check if the swf file is vulnerable...")
        if not self.md5_check():
            print("[*]Start to decompile swf file...")
            decompile_swf(self.swf_file)

            print("[*]Start to scan AS files...")
            if os.path.isdir(self.as_dir):
                for root, dirs, files in os.walk(self.as_dir):
                    for as_file in files:
                        if ".as" in as_file:
                            file_path = root + "/" + as_file
                            with open(file_path, "r") as f:
                                self.code_check(f.read(), file_path)
                        else:
                            continue
            else:
                print("[-]Decompile dir not found.")
