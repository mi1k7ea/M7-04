# coding=utf-8

from optparse import OptionParser
import sys
from urllib import request, error


# 解析命令行输入参数
def input_parse():
    parser = OptionParser('python m7-04.py -t <Scan Type> [-u <Target URL>] [-f <Target Swf File>]')
    parser.version = "M7-04 v1.0"
    parser.add_option("-v", "--version", dest="version", action="store_true", help="show scanner's version and exit")
    parser.add_option('-t', '--type', dest='type', type='string', help='scan type (xss or csrf), combine with -f or -u')
    parser.add_option('-u', '--url', dest='url', type='string', help='target url for flash csrf scan')
    parser.add_option('-f', '--file', dest='file', type='string', help='target swf file for flash xss scan')
    (options, args) = parser.parse_args()

    if options.version:
        print(parser.version, "  --  By Mi1k7ea")
        sys.exit(1)

    if not options.type:
        parser.print_help()
        sys.exit(1)

    if options.type.lower() == "xss" and options.file:
        return options
    elif options.type.lower() == "csrf" and options.url:
        # url参数是必须的且能正常访问
        try:
            request.urlopen(options.url)
        except error.HTTPError:
            parser.error("URL can not be visited.")
        except error.URLError:
            parser.error("URL can not be visited.")
        return options
    else:
        parser.print_help()
        sys.exit(1)
