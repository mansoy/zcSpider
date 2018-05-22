import requests

zwHeaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}

def zwGet(url):
    try:
        rx = requests.get(url, headers = zwHeaders)
    except:
        rx = None
        return rx
    finally:
        return rx


def zwGetText(url,ucod='gb18030',ftg='',fcod='gbk'):
    htm, rx = '', zwGet(url)
    if rx != None:
        xcod = rx.apparent_encoding;#print(xcod,uss)
        rx.encoding = xcod  # gb-18030
        htm = rx.text;  # print(htm)
        if xcod.upper() == 'UTF-8':
            # print('@@u8a');#print(htm)
            htm = htm.replace('&nbsp;', ' ')
            css = htm.encode("UTF-8", 'ignore').decode("UTF-8", 'ignore')
            css = css.replace(u'\xfffd ', u' ')
            css = css.replace(u'\xa0 ', u' ')
            htm = css.encode("GBK", 'ignore').decode("GBK", 'ignore')
        #
        #if ftg != '': zt.f_add(ftg, htm, True, cod=fcod)
        #
    return htm
