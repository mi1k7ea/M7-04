# M7-04
个人使用的一款Flash XSS与Flash CSRF扫描器。

Flash XSS扫描原理及步骤：

1. 使用已知的存在Flash XSS漏洞的第三方swf文件的MD5列表和目标swf文件的MD5进行对比检测，若检测到则给出对应的exp，若检测不到则进行下一步
2. 使用asdec.jar反编译目标swf文件得到AS代码，然后进行基于source和sink的源码扫描检测，如果单文件中同时存在source和sink则判断为疑似Flash XSS漏洞、待进一步人工审计**（目前不支持AS语义分析和扩文件检测）**

Flash CSRF扫描原理：

1. 尝试访问目标域名下是否存在`crossdomain.xml`，若不存在该文件则不存在Flash CSRF风险，若存在则进行下一步
2. 使用正则匹配对应响应报文body中是否存在domain值为`*`，若匹配则判定为存在Flash CSRF漏洞，否则输出domain的值、用于个人审计这些domain是否支持上传Flash文件

使用方法：

```powershell
Usage: python m7-04.py -t <Scan Type> [-u <Target URL>] [-f <Target Swf File>]

Options:
  -h, --help            show this help message and exit
  -v, --version         show scanner's version and exit
  -t TYPE, --type=TYPE  scan type (xss or csrf), combine with -f or -u
  -u URL, --url=URL     target url for flash csrf scan
  -f FILE, --file=FILE  target swf file for flash xss scan
```

- -t参数指定扫描类型，值为`xss`或`csrf`，分别指定进行Flash XSS扫描和Flash CSRF扫描，且必须同时结合-f或-u参数；
- -f参数指定对目标swf文件进行Flash XSS扫描，必须结合`-t xss`参数进行使用；
- -u参数指定对目标URL进行Flash CSRF扫描，必须结合`-t csrf`参数进行使用；

example：

```bash
python m7-04.py -t xss -f sample/xss.swf
python m7-04.py -t csrf -u https://www.mi1k7ea.com
```

扫描效果：

```powershell
PS M:\M7-04> python m7-04.py -t xss -f sample/swfupload.swf                                              

        _|      _|  _|_|_|_|_|                _|    _|  _|
        _|_|  _|_|          _|              _|  _|  _|  _|
        _|  _|  _|        _|    _|_|_|_|_|  _|  _|  _|_|_|_|
        _|      _|      _|                  _|  _|      _|
        _|      _|    _|                      _|        _|  v1.0


[*]Start to scan Flash XSS vulnerability...
[*]Use MD5 list to check if the swf file is vulnerable...
[+]Found Flash XSS vulnerability by MD5: swfupload.swf
[+]Exp: ?movieName="])}catch(e){alert('mi1k7ea')};//
[*]Finished.
PS M:\M7-04> python m7-04.py -t csrf -u https://www.imooc.com                                            

        _|      _|  _|_|_|_|_|                _|    _|  _|
        _|_|  _|_|          _|              _|  _|  _|  _|
        _|  _|  _|        _|    _|_|_|_|_|  _|  _|  _|_|_|_|
        _|      _|      _|                  _|  _|      _|
        _|      _|    _|                      _|        _|  v1.0


[*]Start to scan Flash CSRF vulnerability...
[+]Found Flash CSRF vulnerability: https://www.imooc.com/crossdomain.xml
[*]Finished.
PS M:\M7-04>          
```

