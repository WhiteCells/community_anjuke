import requests
import json
import urllib

"""
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D
"""

"""
# 1
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731480834526_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9114UZBqOIyYGsLV71Nk4n4e+jtMtsRfy+/J+4Okhjs728M/Uw7L9M0HK5cFr7aTx
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=j&tt=l19&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1a7sk&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731480834522

# 2
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731480858054_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9fq/tgQqDZuxEtvoDIfOv27VH6jvMTt/M68Hs+y3TOTMsyEjq38yL0td+Y1ENS6+O
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=k&tt=lte&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1alb0&nu=9y8m6cy&cl=1b2mj"; log_last_time=1731480858049

# 3
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731480814770_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9fcfjBAfCm5bkTp123E16SIkBGb1QLWjWpnycv5uRHombj5tfEl6YHuVbUWeHS2AX
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=i&tt=ir5&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=19ih9&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731480814763

"""


def cn_to_url_encode(text: str):
    """
    :param text: 中文
    :return: url encode
    """
    return urllib.parse.quote(text)


def create_url():
    #      https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&f=%7B%22provinceCode%22:[%22420200%22]%7D
    #      https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420800%22]%7D
    # url = "https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420800%22]%7D"
    #      https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420200%22]%7D
    # url = "https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420200%22]%7D"
    #      https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420700%22]%7D

    # url = "https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420200%22]%7D"
    # url = "https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D"
    url = "https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22]%7D"
    return url


def create_headers(city: str):
    """
    :param city: 城市名称（中文名）
    :return: 请求头
    """
    city_url_encode = cn_to_url_encode(city)
    #     headers_str = f"""
    # Host: aiqicha.baidu.com
    # Connection: keep-alive
    # sec-ch-ua-platform: "Windows"
    # ymg_ssr: 1731402407617_1731465402187_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HJsF6GngnhQhzfZ2rMAINDs5bl8qhTQejR346EdoCUaMpirNmTZ0ZlB7p+aTOWpbIjg5hTyxlbZL5sy5c5fhowKTsfW7wi8yL8KgIvfBKufK3DzJvLDhC4qb4IRB9qZUP6eLGjaFaX/wo21920Eq8XsF3AsR7h1UuZzOofYolMLWzm8LcUnT7R34xnfRFjZM+ZRsWB3P2m9An5lCi9+WcBL4kEKtE/lixFxl4uXU3gPd
    # sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
    # sec-ch-ua-mobile: ?0
    # Zx-Open-Url: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
    # X-Requested-With: XMLHttpRequest
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
    # Accept: application/json, text/plain, */*
    # Sec-Fetch-Site: same-origin
    # Sec-Fetch-Mode: cors
    # Sec-Fetch-Dest: empty
    # Referer: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
    # Accept-Encoding: gzip, deflate, br, zstd
    # Accept-Language: zh-CN,zh;q=0.9
    # Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; ab173145960=34e29e498a485add55c941f7867f8f121731461808479; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; log_first_time=1731463522411; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; ab173146320=34e29e498a485add55c941f7867f8f121731465370975; ab_sr=1.0.1_OGQwZWM3ZmQ0Mzg4YjA0MmViZTc5NDFiYzdlM2EwYmQzYTIzOGRlYTJjOGJiNDk1NmFkY2NmYjE0YjhiN2Q3ZGM4MmU1NDlhNTY5OTRmZTMwNmI1YjdlZDAyNDNlYzAyNzBlMGNmMTVhY2FmNzNlODA4OGYzNjI3ZDY3OGYwNGU2ZTQ2YmJjNzBkZjFjM2RhYmE3ZTUxZDUyYjE3ZTAxYg==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d6499c3911f239818c48e769af99d058d3cc18dd39e657d71fc3ba9ff715aab76780e; _y18_s21_=35be41dd; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3f7nayi&sl=16&tt=1gt3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=25am2&nu=9y8m6cy&cl=25bt7"; log_last_time=1731465402182
    #     """.strip()

    #     headers_str = f"""
    # Host: aiqicha.baidu.com
    # Connection: keep-alive
    # sec-ch-ua-platform: "Windows"
    # ymg_ssr: 1731402407617_1731478940904_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9tnJm45bl65mfoEBUf0KyAHrlSuyQQnlFoX9o84a/hYlqCCJ9Xn1rynb70c1+wEw6
    # sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
    # sec-ch-ua-mobile: ?0
    # Zx-Open-Url: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
    # X-Requested-With: XMLHttpRequest
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
    # Accept: application/json, text/plain, */*
    # Sec-Fetch-Site: same-origin
    # Sec-Fetch-Mode: cors
    # Sec-Fetch-Dest: empty
    # Referer: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
    # Accept-Encoding: gzip, deflate, br, zstd
    # Accept-Language: zh-CN,zh;q=0.9
    # Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; ab_sr=1.0.1_MjgyYWZjNzczYWI1NTMzMzU4ZDVmN2U5ZjI1YWFjYzNlMWQ4ZWI2NTI5YWYzNzhkZTRkOTdjZmI4OGI2ZTkzNWM5OWE1ZGVkYjk2Y2NmZDUwY2Y3NjNiNGJmNDM1ODU0NzU5ZGY0MWUzMGQ0YTAyMzE3YjY5ZDc5ZTE2NzFkODg0OTlhNzUwZmZhNTM4YzE5ZDc2NGEwOGNiZGQwNWZjZQ==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=6&tt=74m&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5yjd&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731478940886
    #     """.strip()

    """
    
    """

    headers_str = f"""
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city={city_url_encode}&f={{%22provinceCode%22:[%22420100%22]}}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; ab_sr=1.0.1_MjgyYWZjNzczYWI1NTMzMzU4ZDVmN2U5ZjI1YWFjYzNlMWQ4ZWI2NTI5YWYzNzhkZTRkOTdjZmI4OGI2ZTkzNWM5OWE1ZGVkYjk2Y2NmZDUwY2Y3NjNiNGJmNDM1ODU0NzU5ZGY0MWUzMGQ0YTAyMzE3YjY5ZDc5ZTE2NzFkODg0OTlhNzUwZmZhNTM4YzE5ZDc2NGEwOGNiZGQwNWZjZQ==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=6&tt=74m&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5yjd&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731478940886
    """.strip()

    print(headers_str)
    headers = {}
    for line in headers_str.strip().split("\n"):
        key, value = line.split(": ", 1)
        headers[key] = value
    return headers


def process_request(url, headers):
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)

    with open("./aiqicha.json", "w", encoding="utf-8") as f:
        f.write(rsp.text.encode("utf-8").decode("utf-8"))

    with open("./aiqicha.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    with open("./aiqicha_utf-8.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("end")


def parse_json(json_str: str):
    pass


if __name__ == "__main__":
    url = create_url()
    # headers = create_headers("荆州市")
    # headers = create_headers("武汉市")
    # headers = create_headers("黄石市")
    headers = create_headers("鄂州市")
    process_request(url, headers)


"""
# 省 + 地区（地区没有参数）
https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420111%22]%7D
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=6&s=10&o=0&f=%7B%22provinceCode%22:[%22420107%22]%7D
f={"provinceCode":["420111"]}

# 省 + 行业
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%22A%22]%7D
f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%22A%22]%7D
f={"provinceCode":["420100"],"industryCode1":["A"]}

https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%22D%22]%7D
f={"provinceCode":["420100"],"industryCode1":["D"]}

# 省 + 行业
# 农林牧渔
## 农业
## 林业
## 畜牧业
## 渔业
## 农、林、牧、渔服务业
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420102%22],%22industryCode1%22:[%22A%22]%7D
f=%7B%22provinceCode%22:[%22420102%22],%22industryCode1%22:[%22A%22]%7D
f={"provinceCode":["420102"],"industryCode1":["A"]}

# 农、林、牧、渔服务业 + 农业
f={"provinceCode":["420100"],"industryCode1":["01"]}

# 农、林、牧、渔服务业 + 林业
https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2202%22]%7D
f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2202%22]%7D
f={"provinceCode":["420100"],"industryCode1":["02"]}

https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420000%22],%22industryCode1%22:[%22T%22]%7D

https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2244%22]%7D
f={"provinceCode":["420100"],"industryCode1":["44"]} # 

https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2250%22]%7D
f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2250%22]%7D

https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2244%22]%7D
f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2244%22]%7D

# 电力、热力生产和供应业
https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2244%22]%7D

# 燃气生产和供应业
https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420100%22],%22industryCode1%22:[%2245%22]%7D

# 省 + 地区 + 行业 + 年限
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&f=%7B%22provinceCode%22:[%22420102%22],%22industryCode1%22:[%22A%22],%22startYear%22:[%7B%22start%22:%222023%22,%22end%22:%222024%22%7D]%7D
f=%7B%22provinceCode%22:[%22420102%22],%22industryCode1%22:[%22A%22],%22startYear%22:[%7B%22start%22:%222023%22,%22end%22:%222024%22%7D]%7D
f={"provinceCode":["420102"],"industryCode1":["A"],"startYear":[{"start":"2023","end":"2024"}]}

# 
f=%7B%22industryCode1%22:[%2203%22]%7D
f=%7B%22industryCode1%22:[%2203%22]%7D
# 01-04

# 
f=%7B%22industryCode1%22:[%2206%22]%7D
# 06
f=%7B%22industryCode1%22:[%2212%22]%7D
# 12

# 成立年限
## 一年内
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420000%22],%22startYear%22:[%7B%22start%22:%222023%22,%22end%22:%222024%22%7D]%7D
f={"startYear":[{"start":"2023","end":"2024"}]}

## 1-2 年
https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&
f={"startYear":[{"start":"2022","end":"2023"}]}

## 2-3 年
f={"startYear":[{"start":"2021","end":"2022"}]}

## 3-5 年
f={"startYear":[{"start":"2019","end":"2021"}]}

## 5-10 年（可能超出范围）
f={"startYear":[{"start":"2014","end":"2019"}]}

## 10 年以上（可能超出范围）
f={"startYear":[{"start":"0","end":"2014"}]

# 注册资本


# 企业类型 (1-10)
https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&
f={
    "provinceCode":["420000"],
    "industryCode1":["01"],
    "startYear":[
        {"start":"2023","end":"2024"}
    ],
    "entType":["1"]
}

"entType":["10"]

参数:
p=页数
s=返回公司数量最多 20


Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731316049516_1731394382051_ApSBHrxk6aM1wiiVCRm5l9RLuVpQN7ZDE+o20dsOY4DAUci7Ls28zmEEpl0QN8Atv6jzAzFnIHqx0OobjO+RgG5OsaHj8aP7Zrxu82viGRzUGXssozrZdLuolnrRBQvQRtcl2ioYQBYM09/AnVn7K6b3RPxLClzfDr7/MaW7CYJZuaPg+3A+GyKj9OLFbgl7p8vQNbS8aVXEPjGIugvnziODtpUNaI6OhJxg4iRZz/bIDZLEVCcL5NjtS42w4YlaOG8fHhnDUC4PNPsbziD5fAgilaTDLVnuMoARks2ocThl1LEPmG7xVisBB56QH35Yh7KyooWPdrmaQzZA0mmv246VV+r9d9X79jBAEYhzuvCfKyv6jHUC61syfX9VHhhWV4XQV7rxBURaKt9roe7d8USBoiOgstxqb3cCV5rFC61vyWqTXR2er2Cp/3xZzHaI
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; log_guid=4c48687f47800e9cc05aa81601e6ba8f; in_source=; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGkHJI5+HejCI+YBMRTRlDLcGEimjy3MrXEpSuItnI4KD6gPH6jkea9LsrC89k7QK9sPnGsRKrgm+c8AFVUIodNr7FEIRtRAOgwicUK5GoOqmhJsVwXkGdF24AsEQ3K5XBbh9EHAWDOg2T1ejpq0s2eFy9ar/j566XqWDobGoNNfmfpaEhZpob9le2b5QIEdiQcpT+G70XAL2dDZrKJZsyBEFCMUN0p4SXVVUMsKNJv2T2Q0Rs14gDuqHJ3rxHJuOGO4LkPV+7TROLMG0V6r0A++zkWOdjFiy1eD/0R8HcRWYo64YZQejZKa7nFsdjKdPqCp+HBavJhpxl858h16cMtKQmxzisHOxsE/KMoDNYYE7ucLE22Bi0Ojbor7y6SXfVj7+B4iuZO+f7FUDWABtt/WWQqHKVfXMaw5WUmKnfSR5wwQa+N01amx6X+p+x97kkGmoNOSwxWgGvuezNFuiJQdt51yrWaL9Re9fZveXFsIu/gzGjL50VLcWv2NICayyI8BE9m62pdBPySuv4pVqQ9Sl1uTC//wIcO7QL9nm+0N6JgtCkSAWOZCh7Lr0XP6QztjlyD3bkwYJ4FTiNanaDaDbqdzIXFsBZWqSyyvBl18qZhILHGnWDyfzQZbh1XZEKeAdUiln9jkMKniXrc3ZJKGSGk66HDxtjKMU4HPNa0dthF7UsHf7NW9eE+gwuTQSa7GLWfOy9+ap4iFBQsmjpefgOF89jAHLbnVUejtrqqvdWuZ4/HEMMnbDCD5VPlPijyQv5hRFZsF+eQboEydZL8+vlcABgxzYamRzhKuGyzS/8Hl9kvBNQ2Jdc2vnWtW/hY4qGtGAcdWyIH3UpW6DdxqyYN1zEUp6ggVCZWoCgBT7dhxdC3bEpOFlnJXW/ewK+fOJ1Rm0oz1xFFR9FYG1BJvnQA8z6Cz/jTzGDsocIHwA4qlml8ik+FDREmF7DwZHRpOpiwmjUhELAzdRtuu+0nt6o8w3MlwZxJhxBabUW5sicyie973hz6nxWLbBzvYx9F54WJPMynUbqkO3Z7jSA8MZt1Aj6NtrhSNGXID70JtNbPvI2IjBBSQ1a2vY1slk3TKTLoU96dsmC3+9Ar1MCJM; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272; HMACCOUNT=F0698D153D5B731D; log_first_time=1731392852847; entry=1101; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ5oi0P9g8qzzmd; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731394217; ab173139120=31e29e498a485add55c941f7867f8f121731394217370; ab_sr=1.0.1_OGY4MTg3OWNkMDc4MDFkMTE3MzdkNzI2NGE3NjQyODY2ZTMxNTI5MmU4MGE0NzI1YmJjY2ViNThmZTczNWQ3MGNkYTNhOWEwOTZhYzIyNmU3ZDM0YTdmZjUxNDJiZDcwNWYxYmI5ZjEzNWQ5ZjViZTNjNmFhZjI2MDNlYTdhZGQ5OTM2NTI1MjhkZjJiY2RlMmUwYmFmM2IyMzQ5NTQxMg==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d6499591e2b0e5531d8731179844f81bf4447d9f0f73bd68659ab9ed7d8c60e2d2ece; _y18_s21_=b10311b5; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3e30f10&sl=t&tt=psn&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=hdiv&nu=9y8m6cy&cl=hlnn"; log_last_time=1731394382046


GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=3&s=10&o=0&
f=%7B%22provinceCode%22:[%22420111%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731463915072_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HJsF6GngnhQhzfZ2rMAINDs5bl8qhTQejR346EdoCUaMpirNmTZ0ZlB7p+aTOWpbIjg5hTyxlbZL5sy5c5fhowKTsfW7wi8yL8KgIvfBKufK3DzJvLDhC4qb4IRB9qZUP6eLGjaFaX/wo21920Eq8XsF3AsR7h1UuZzOofYolMLWqYN513T1AJdsPEmQomsJ4fZROD3nrAwgnON3072sUcboZO1GkSWV53vxonRWh6q9
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQyPKeJy5upZtmd; ab173145960=34e29e498a485add55c941f7867f8f121731461808479; ab_sr=1.0.1_MjE3Njk2NGU1YjU0YjJkYzU2MDkzYmY0YWViZDE4N2I3N2E0OTlkZTJlNWRlYTBiOGU3Mzc1Nzk4M2UyYTlkZDZmYTUyYTIxMmM3MDIxY2VkNTI3NmRjZGY2Yjk2YzQ2YjU5OTM0NGNjNWY3Y2IzZWEyMmU0NTNiYTk0NTE2MzZjZjZkYzIzMGQ1ZmQ5YjU5MzM1Y2I2OWI0NzE3MDllYw==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64995a005c0de4b758acef93e5264cff5ffbdf3ea2a86929c50ce2835d8fd8f360a6; _y18_s21_=2021ae92; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; log_first_time=1731463522411; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3f7nayi&sl=b&tt=hrw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1945a"; log_last_time=1731463915067


GET https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420000%22],%22industryCode1%22:[%2201%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731464413610_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HJsF6GngnhQhzfZ2rMAINDs5bl8qhTQejR346EdoCUaMpirNmTZ0ZlB7p+aTOWpbIjg5hTyxlbZL5sy5c5fhowKTsfW7wi8yL8KgIvfBKufK3DzJvLDhC4qb4IRB9qZUP6eLGjaFaX/wo21920Eq8XsF3AsR7h1UuZzOofYolMLWkTfhcN2xLtaLMB5lcU+BL44WMI1dE/C0ihmyr6SyC8YquXNGkW7+vgKIiZbo+dBY
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?
    city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; ab173145960=34e29e498a485add55c941f7867f8f121731461808479; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; log_first_time=1731463522411; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731464213; ab173146320=32e29e498a485add55c941f7867f8f121731464213477; ab_sr=1.0.1_ZDQyMWRkZTc1MGMwNzA4MTVkOWRlZWVjMTE3YjI4YmViMWJhODg5ODcxNWIxZTNiODg5NzE1NDQ4NmM5Y2U2ZWMwYjhlM2ZiMWFhOTIxMzhhYzdmYWE5NGE5MTVlM2MyZjFkMjFhYjFiYzhiOTJmZDQ3MWNlMTU0OWZkNDhhMTA5MGNjNGQzNDcxYzEyOGFlMDRmYThmYmVlOTJjODFmYQ==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d6499c059f190588ea72b05af556acc660e15ea1079c4b54c56f72ebaeadb99d0db4f; _y18_s21_=07780c57; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3f7nayi&sl=g&tt=nji&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1jxvf"; log_last_time=1731464413591

GET https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420102%22],%22industryCode1%22:[%2201%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731464759263_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HJsF6GngnhQhzfZ2rMAINDs5bl8qhTQejR346EdoCUaMpirNmTZ0ZlB7p+aTOWpbIjg5hTyxlbZL5sy5c5fhowKTsfW7wi8yL8KgIvfBKufK3DzJvLDhC4qb4IRB9qZUP6eLGjaFaX/wo21920Eq8XsF3AsR7h1UuZzOofYolMLWkdltDIOrEr07T7SICbIcmwtoncotsRhIU1jEEAtkC8QZycjrH9x48AiwMlGZ5xie
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; ab173145960=34e29e498a485add55c941f7867f8f121731461808479; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; log_first_time=1731463522411; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; ab173146320=34e29e498a485add55c941f7867f8f121731464426975; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731464427; in_source=; ab_sr=1.0.1_MzU4Njc1YjJhMDMxYzhiMmNlMDk0ZDA5Y2ZjYWZhNmY0ZDg4ZTc0ODA0NGFkNGI4YmE0NDJjYjcyZDZiNjQxMDA2ZjY0NjUyMjM4NGExMTRjOWZjOGI3YzZjMThmOTI1ZDk5ZTRlN2YyZWZhOTQwNTYyNDRjYzNhNzkxZTI5YTI1NjBjNTQ4OWYzNmIwM2Q0ZGY0MTdhNjk4ZGYwMTQyNQ==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d649920558ca3e8212d8c35753614f8aa1d036e2e74d2d88f9686f539e51f4de80529; _y18_s21_=524e1be3; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3f7nayi&sl=m&tt=s7g&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1rjjz"; log_last_time=1731464759244


# 宜昌
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420500%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731465402187_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HJsF6GngnhQhzfZ2rMAINDs5bl8qhTQejR346EdoCUaMpirNmTZ0ZlB7p+aTOWpbIjg5hTyxlbZL5sy5c5fhowKTsfW7wi8yL8KgIvfBKufK3DzJvLDhC4qb4IRB9qZUP6eLGjaFaX/wo21920Eq8XsF3AsR7h1UuZzOofYolMLWzm8LcUnT7R34xnfRFjZM+ZRsWB3P2m9An5lCi9+WcBL4kEKtE/lixFxl4uXU3gPd
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E6%AD%A6%E6%B1%89%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_UNIQ_UID=307f7f2a2410ecd3e088fa87b3e55fb8; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; ab173145960=34e29e498a485add55c941f7867f8f121731461808479; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; log_first_time=1731463522411; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; ab173146320=34e29e498a485add55c941f7867f8f121731465370975; ab_sr=1.0.1_OGQwZWM3ZmQ0Mzg4YjA0MmViZTc5NDFiYzdlM2EwYmQzYTIzOGRlYTJjOGJiNDk1NmFkY2NmYjE0YjhiN2Q3ZGM4MmU1NDlhNTY5OTRmZTMwNmI1YjdlZDAyNDNlYzAyNzBlMGNmMTVhY2FmNzNlODA4OGYzNjI3ZDY3OGYwNGU2ZTQ2YmJjNzBkZjFjM2RhYmE3ZTUxZDUyYjE3ZTAxYg==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d6499c3911f239818c48e769af99d058d3cc18dd39e657d71fc3ba9ff715aab76780e; _y18_s21_=35be41dd; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3f7nayi&sl=16&tt=1gt3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=25am2&nu=9y8m6cy&cl=25bt7"; log_last_time=1731465402182

# 荆门市
GET https://aiqicha.baidu.com/s/advanceFilterAjax?q=&t=&p=1&s=10&o=0&f=%7B%22provinceCode%22:[%22420800%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731478940904_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9tnJm45bl65mfoEBUf0KyAHrlSuyQQnlFoX9o84a/hYlqCCJ9Xn1rynb70c1+wEw6
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; ab_sr=1.0.1_MjgyYWZjNzczYWI1NTMzMzU4ZDVmN2U5ZjI1YWFjYzNlMWQ4ZWI2NTI5YWYzNzhkZTRkOTdjZmI4OGI2ZTkzNWM5OWE1ZGVkYjk2Y2NmZDUwY2Y3NjNiNGJmNDM1ODU0NzU5ZGY0MWUzMGQ0YTAyMzE3YjY5ZDc5ZTE2NzFkODg0OTlhNzUwZmZhNTM4YzE5ZDc2NGEwOGNiZGQwNWZjZQ==; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=6&tt=74m&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5yjd&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731478940886

# 黄石市
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420200%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731480210069_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/94WDrRE03ekpFUN2Q4YYw1aIfF5NTJyB/uQ6Es2oNgARXMiTD5g1HwDYJDInlH4C4
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=b&tt=c2j&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=x3gh&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731480210059

# 鄂州市
GET https://aiqicha.baidu.com/s/advanceFilterAjax?t=&p=2&s=10&o=0&f=%7B%22provinceCode%22:[%22420700%22]%7D HTTP/1.1
Host: aiqicha.baidu.com
Connection: keep-alive
sec-ch-ua-platform: "Windows"
ymg_ssr: 1731402407617_1731480429466_iUHh0ZrgXkUYlNrfoy34BDQ7+LHaY/ll2eV0XZGBdQf3f7kH4FMaJVROd7UL2zwrthCXom/UC9fE+m8FsB+zzJKucSEgeW69uQFKo3piZzmGs9h5RNwnPl4wQCBxi8AhuVK5m3n5A/lgo7C9E6iAtbfn9z7nHTTC8H4JVrzdi9beFvgCwPoX7gXRK9Lv0uZyHhadJYNku4y/YwUbnV8+HCLYF6PZ7tufEU5U9JRf968ZmDgN55b6lfYQj0EAb5kpPIoO4wvsNAJlINTlRwi0RouLT/jgW4LmeA90oQAhwSlmT+lWFjmiCcRsYl2UnCQ9gZ8tRAsLV155Zt8IogMNMf7pAb/2OWypiR3lVjE3md2vlEj3zkOsEsYAr0cDp2/9hNCPW4p8UFrv7A1JyBxy11orO6oAamsizZiCX9HOJGwLoxRJWy6AsNrIsS32ci3Z
sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
sec-ch-ua-mobile: ?0
Zx-Open-Url: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://aiqicha.baidu.com/s?city=%E9%BB%84%E7%9F%B3%E5%B8%82&f={%22provinceCode%22:[%22420100%22]}&province=%E6%B9%96%E5%8C%97%E7%9C%81
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; BIDUPSID=203E9D49E5D58FEEB97B23EA36E6E9CD; PSTM=1730702564; H_PS_PSSID=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; H_WISE_SIDS_BFESS=60276_60941_61027_61036_61053_60851_61099_61129_61128_61113_61140_61115; log_guid=4c48687f47800e9cc05aa81601e6ba8f; _j47_ka8_=57; ZX_HISTORY=%5B%7B%22visittime%22%3A%222024-11-12+11%3A41%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTwzFOPThWpgx3c22Kd0E6dOAmd%22%7D%5D; BDUSS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDUSS_BFESS=pjYVRZaE9mRTlIZGI4VmlGRDF1WVpMRUtlT2E3U3dFeGlTandRaHlnYmdYRnBuSVFBQUFBJCQAAAAAAQAAAAEAAAAjLviHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODPMmfgzzJnQW; BDPPN=62d4143d2d7fc2487321e3d790c904bf; login_type=passport; _t4z_qc8_=xlTM-TogKuTw2CFO4jVGEG8PDRqEdY4TzQmd; BAIDUID_BFESS=203E9D49E5D58FEEB97B23EA36E6E9CD:FG=1; delPer=0; BA_HECTOR=850584050g810lah058424ah19d09g1jj81v11u; ZFY=0najx6y8GkgOt51qgoXdujRrswl77KuANdPeV6ACdf0:C; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; _fb537_=xlTM-TogKuTwZ4BwZAaDAuReN%2A4IrFUgQ3C7gumJtEoXmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731383272,1731464212; HMACCOUNT=F0698D153D5B731D; in_source=; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1731465371; _s53_d91_=7d24ad4bc7e8c351c1b137239049018960c5d20396e6a3cc2b323aafaf99603be1617c4dd5df0404bb01c99f0f1aa854d31428323d332872c300b408fc0321673cc42afbd63ff820a88521a9402df9fced5df7aa10f2e8b509aec2a891b752b31e0c3c66a9ca1dd11d6166c9df8f5e5a84a3492d53cfd3bc6e395f089d71248daa55612a218144d7304cfcbb2a40f5ed7a0c4ed9632d658d97cebf0d23f5e4c54382d657420a0c43d629c1eda51d64999c632ec8b84821aee60aad4fce98f0a81385e1ce11ee76cd71f95b3a4fadff0f; _y18_s21_=49eb906c; log_first_time=1731478661780; RT="z=1&dm=baidu.com&si=fbc2d4c4-4611-48ee-a2bd-56a873428bd4&ss=m3fhotyt&sl=e&tt=exy&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=11plo&nu=9y8m6cy&cl=6n7yy"; log_last_time=1731480429462

"""
