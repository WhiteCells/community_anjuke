import os
import time
import requests
from lxml import etree
import random


res_path = "./wuhan3"


def process_detail_page(url, name, page_num, num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "SECKEY_ABVK=asa7BDAt8wO+usXrMQ868468lvsBTzGU186BFka1PyM%3D; BMAP_SECKEY=wSdnTJ2x3Kh-QsXQvPcnOL8mwH62QEdiYc1NnnNNF12LvleasyyCNjkeoatzDsA__TvTepgB92qI0v9_tekl883HnXcjkDA9v30I3hYe6ZXR1CshiGMl7A6I6zVn7Qs-0kqbwhmRHFGyFU3JM5yaN06vIHSthq0wXpYntHIbyF6YkICDvEz5Nz9c-Q2-UNNF; sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; fzq_h=da53c88bc291080f187eb6807befe088_1729559751289_b9372eb777134921b5e2fa0fea3d9ef8_1899585074; id58=CkwARGcW/Mg62h7ND4F3Ag==; obtain_by=2; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; init_refer=https%253A%252F%252Fwuhan.anjuke.com%252F; new_uv=2; new_session=0; fzq_js_anjuke_xiaoqu_pc=c4f470cc9890c818df807185a24a0a78_1729584261475_24; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729584265061&PBODY=MaCN-d8-1k4xY2QMgKy-im7xsIoKplQUPTtbRz29AQ94PRknf_WG6ATYx84zCKXqy2R02dD1t-P1l3H99nlq8KReY82-GVgdNBYjTjFvgOiFIHQOi8L8VP7Qrpdiv9Vli3qwJp_9T3YgzG35dOxLp_fWau1JquwlS8_FHXFT6bo&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTU4NDI2MzQ5MzEzODA1NnxzSjV0dmRsS2dwUW10WXorRkFBb25hUVE2YnBJMXNoeFFrNFpKSHVmZVlrPXxmYTRmNzdlMTA1OGJjNTFhMjBiOThmMGYwMzZkZWFmY18xNzI5NTg0MjY1MDUxX2Q0MjE5NWU3Yjc4NDQ2ZjJiOTljMGRhZGVjNDg5YjM4XzE4OTk1ODUwNzR8OGU0YjgwMDg2MjM2NDExZjg2M2Q0OTcyODM5ZGIyYjNfMTcyOTU4NDI2MzEwOF8yNTU=",
    }
    response = requests.get(url, headers=headers)

    # print(response.text)

    # 获取链接

    with open(f"{res_path}/{page_num}_{num}_{name}.html", "w", encoding="utf-8") as f:
        f.write(response.text)


def process_list_page(page_num):
    """
    获取小区列表页
    """
    # https://wuhan.anjuke.com/community/o6-p1/
    url = f"https://wuhan.anjuke.com/community/o6-p{page_num}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; new_uv=3; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=e6c5e1891192c1a6d022b3918a076205_1729735795331_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729735798410&PBODY=Rjam1iShdKNqo5x5mxfTWrtZJ_27yd_2QKl9uRbGlYl_B-M4qNyz3Vh5hxbanHHia3U9KAS3076BMX_0m3AOXWHwfYZJRdR-Kd-aAT5Ppr1LIs9UWp1OLDiUTVfUf16MCQPgKnV1gX1HOC_gRfFJnqWA9_AOhEdZV_Wpjh-lQ0M&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTczNTc5NjczMTMxNTY2MnwybVpMY0NYWDFtVWE5eHpRbFRKSUVrajVvWEx2dENYR3VFWGdCY1lwd2FnPXxiYzNjYTBjZGY2NGVkZTBmOGEyZDJmYWIzNWRhMDg4YV8xNzI5NzM1Nzk4MjY5XzJmZmJlM2EyNDhjMTQxNDg5ZmUzNjE0YmVmNzlkZTRjXzE4OTk1ODUwNzR8YTlkYjgyNjMzMjU4OGViNGUwMWJjYmFkYThkZGJkOWRfMTcyOTczNTc5NTkzOF8yNTY=",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=4; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=2e6ce0ee73078fcf36f32453639cf053_1729739911737_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729739912277&PBODY=aYiKx7AFFHwTdBstgzcJFXpd_rXBs71Jm4rPM1VsQgPM7A7C4dpo-Cx5zXnUN0Qq5Gz47A4Vsn3R01mWy33mVuvXN5iJb_H4oefVdEgqW9e7t0jHTYOCIa7HL__X7LTMKGjJyfRaQqRU_7fW-s7c_llvFVi0ufnbiSGgnKvQdmY&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTczOTkxMjc4MTA5NzkxOHxBa2NybzdhTEJoUE4vdnl4MDhielZkb1U1UDR3dGJTaXh4bTRPbC9wMGxJPXxjZDAxOTJkOWMxM2E1MTE3NDg2NjYzMGE1MjA3YmRjN18xNzI5NzM5OTEyMjk3X2Y1MjYwYzc4NDk3ODQwYmE5MzUwYzRjYzk1M2EyNDQwXzE4OTk1ODUwNzR8ZmRkMTZjMjU4YjNmY2Y0OWFjMWU1Nzk5YTRkMjYwNTFfMTcyOTczOTkxMjI3Ml8yNTY=",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=4; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=82a918aaf7c5791ec42c9763e7cca5b6_1729741083552_24; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729741084364&PBODY=Is9RstesjQ5LvFyWtirfihuYk8bYjbHwMI_hHl4uAGLrecXF1iQyBFju3djgJr2Fk9ev_qrBio_yWE0zXNpPc6KzNfOCFhlo4ZTKKQUCc2YKb-xDnEg1W5z0qisjkdAmAhvehvFo43Xcq_MumJ9Np1xgr6C14OLdJsge8a-Rki0&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTc0MTA4NDkxMzMxODQ1MXw1TGhRS1IyZ0xBRUM4aG81b1Y4WHQzdkpiUGc5QjY0b25NQVBHd1pabENvPXw2ZmYwYjAxMGQ5M2FjMjQzYmU2NTVjMTMwMzVjYmI4NF8xNzI5NzQxMDg0Mzg0XzVkMzJlMDJhMDE5NDQ3MWVhYWY2Y2Y4MzQzZGJmNWYzXzE4OTk1ODUwNzR8N2M5MTkxNDcyYWNmMjhiZDgxMGM2NDJlNDczZjE1ZWRfMTcyOTc0MTA4NDM5OV8yNTQ=",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=4; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=8e27da886a2a0693a5566a062c9614b3_1729741091263_24; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729741091752&PBODY=PQyULnp4wgt0yKI-9nc5_DDgp34IXv69CTXrsV-l1fIzMgGekBgN1wtsptNc_MzQNLrPf9dxcXQ76vm9o0zwYhY_tu7jJdorXyJ6ZPckcJwEuxBHT1D4sNStqoN6B8LUIzObT61eXTyUDcOwU4aGvZf9atN_Td4w1ZeC6gyVwfw&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh;            xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTc0MTA5MjI0NDQ3NjgxMnxCTU1WYW8yR0JCTVk5ME1oTHlUWW5OMHRscGFjV1doSVNMTE8yM2RsUTBBPXxhYTY3ZDlhMTMxZDgyZjJiNmJjNDI0OWNjYmFiZTZhN18xNzI5NzQxMDkxNjQ0XzkyYmU0ZjkxMTk4NTQ5OTg4OTQ1MDMxN2JjODVkZDQ0XzE4OTk1ODUwNzR8Y2MwZDk1ZjdmYWI5NGZlYzQwZjdiNjAyYmU0MDRkNGNfMTcyOTc0MTA5MTg0OV8yNTQ=",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=4;              fzq_js_anjuke_xiaoqu_pc=9dc0083773dee71a4404159939f55c74_1729741175754_24; obtain_by=2; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729741176157&PBODY=QlM809D6obDcqpK21kABaeEAxQjONv-y5A9jyiPXYW5nM99MtuyqJUV_jnwYIZ7dBtO06Dr1Kdn6wJpYe7nK3RcmPZGWmgR96kkPNCwxvKFW0GDSwIMyT8f2IIMQRT1S9oMcQrCLkoQuf3ijfDO5Q55JLmXbJXiBP_9YEkB6N10&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTc0MTE3NjkxNDg4MTgxMXwzdmFPMk9WNzRMOHRhSVpjcFhCWU5LclczdURrcjFoUng0eFdNY2d2ZWxZPXwxNTYzZTYwZTA2YTUxYjljNzQ3YzcxMDE2YTExN2YwMF8xNzI5NzQxMTc2MDIyX2FhMjI3ZDU5MGQxYTQ0N2M4N2RmZGFhOWMxMzE0NTZjXzE4OTk1ODUwNzR8YjBkOTNlMTk3ZmNhNWU1MmM0NjU3NGI2YzRjZjk3NmVfMTcyOTc0MTE3NjE3MF8yNTQ=",
        # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=4; obtain_by=2; fzq_js_anjuke_xiaoqu_pc=ef497b488298d7da0b45ecd6138ae1fd_1729742785382_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729742785845&PBODY=ocDaMx7O2afFYafnukPLl6ZTpGSEsuMQxVMjjsFrzX0HmABVY9fjP1UW9EbQRsCgKmZxv6YP1czyaTPiLJkT9FysjGnsJEXq8punW0Or9YO6d5s3FVZ6TAhCa_4WkAx8YqAn8GRnvxHXWcWpdXGzfhQm7Rx6kG9oZIYvovg8aAM&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTc0Mjc4NzEzMzcyMTk0N3xaK3BIVDc1VGFzUCtlQXRMcE9WZElSUFgrQXJNaGRFOVJzNUJlbm5DUEZzPXwxZjc4YmM1NGE2NmY0Y2I3ZWFjMzUxMTIzOTEyZDBiZF8xNzI5NzQyNzg1Nzk2X2RlMmNhYTRmZGJlMTRiY2E5YzA2MWY4NWM5MWY4MTBmXzE4OTk1ODUwNzR8OTNmYzczMDNkMGE3Y2M4ZDc1NjBlZjkwN2Y3NzZiYWNfMTcyOTc0Mjc4NTk4Ml8yNTY=",
        "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; twe=2; ajk-appVersion=; id58=CkwARGcW/Mg62h7ND4F3Ag==; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_h=dff59bdf0e571eac870107de44dd8df5_1729732062486_1c9b564d8baf41f38c8316b50d0d75b6_1899585074; new_uv=5; obtain_by=2; ctid=22; fzq_js_anjuke_xiaoqu_pc=1ac4aa9e117501f0493749a03e06086b_1729748877370_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729748877635&PBODY=I7qP2Esg7l4PiXrapm7_ytiM3uSsagD3xXAfzpqeKZZp2y_4VyVqOjaTtDjjTCg4D4ULU12MHe-j2_Y-7GXDClpUQIejlWrWl3rNrYyEtqG4H04zRDVCfYRdEEt67bqhTNSkK1Yp_FcJh52HwF0ZfvxTKts9v2Ur3dVQw8gOw-A&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTc0ODg3NzkyMzE1NTM2M3xZYlJPY2NHZnU5dmJGaHV2V1oyOFd2U1hQQW12WENxNWlIRmtncmdtMHVBPXwzMjJlNmYxM2VlNzhjMjk2YmFjZGI5ZTViZDA2YTc5OV8xNzI5NzQ4ODc3NDg5XzllYjM2NGM3MDdkYjRhNWFiY2I4OThmY2E3MGYwNDkwXzE4OTk1ODUwNzR8OGIzNGUyM2UxMGU1MDM4ODAwMjU2OGFhYTBlZjEzNTZfMTcyOTc0ODg3NzYxNl8yNTY=",
    }

    response = requests.get(url, headers=headers)
    print(response.text)

    xml = etree.HTML(response.text)

    # 获取小区名
    communities_name_list = xml.xpath(
        '//div[@class="nowrap-min li-community-title"]/text()'
    )

    # 获取小区名
    communities_urls = xml.xpath('//div[@class="list-cell"]//a[@class="li-row"]/@href')

    num = 1
    for url, name in zip(communities_urls, communities_name_list):
        time.sleep(random.randint(1, 3))
        process_detail_page(url, name, page_num, num)
        num += 1

    with open(f"{res_path}/{page_num}.html", "w", encoding="utf-8") as f:
        f.write(response.text)


if __name__ == "__main__":
    if not os.path.exists(res_path):
        os.mkdir(res_path)

    for i in range(1, 24):
        process_list_page(i)


# def process_list_page():
#     url = "https://wuhan.anjuke.com/community/o6/"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         # "Cookie": "sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; fzq_h=da53c88bc291080f187eb6807befe088_1729559751289_b9372eb777134921b5e2fa0fea3d9ef8_1899585074; id58=CkwARGcW/Mg62h7ND4F3Ag==; obtain_by=2; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; init_refer=https%253A%252F%252Fwuhan.anjuke.com%252F; new_uv=1; als=0; new_session=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; fzq_js_anjuke_xiaoqu_pc=c33896636290cd2b3c10361a0fb0caf7_1729578233281_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729578235474&PBODY=fMMxbh8mJ9mpPim1apiQAfUar0hgsAre58N2ahJbqSY9-8XTQltLsGdElfdH9p1WiKIpYNpFNBxCSqbRnhJiFAqVec4DmC9c13fl09D-6jDZolw39veb15ZGTMnYNkeDxp3gZzbyTKyW3HE2UPQy10Jnfq_XKkujJyL3ohgkvVs&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTU3ODIzNDIwNDk5MDgzMXxvdkJXc0NCcFJZRWJXRjdSUXBXOU1ZWHVkY1dkOTBuZUoycURjUUpzLzlBPXxiYTU0M2NmZDZjNDE5MjE5YzJiMGU4YjhjYThkYWM3M18xNzI5NTc4MjM1MzA3XzRiNDFjM2UwYjYyNjQwNjlhOTdkMmUwZGM5ZjU0N2FlXzE4OTk1ODUwNzR8N2E1ZmFkYTk4NDA0Zjc0OTZhYWMzOWUyMTNlZTE1M2JfMTcyOTU3ODIzMzYwOF8yNTY=",
#         "Cookie": "SECKEY_ABVK=asa7BDAt8wO+usXrMQ868w1zRcEhDBR1cTsMBjdeXD4%3D; BMAP_SECKEY=wSdnTJ2x3Kh-QsXQvPcnOIPcSDJzNwaFim7ZlgRsCxVnLah6vzgAXOS2SMrKi385sZZC5r65fGlJd36n2XfVVQUSHFolaFe5R-ILw0JxyJPYizvXWT4nR5h-tlYWoCaixEm51u5My3GFzrb1tISUcMPcfwax7arXS782xEL3_w4JqhdXeceyqb4oWHnOG6cb; sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; fzq_h=da53c88bc291080f187eb6807befe088_1729559751289_b9372eb777134921b5e2fa0fea3d9ef8_1899585074; id58=CkwARGcW/Mg62h7ND4F3Ag==; obtain_by=2; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; new_session=1; init_refer=https%253A%252F%252Fwuhan.anjuke.com%252F; new_uv=2; fzq_js_anjuke_xiaoqu_pc=13fd7bdc1f9045dc6dc1971a0037fe5b_1729583085884_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729583089672&PBODY=SY29y3YuakEIKgM1KrVmX6nRNFbJyUwvo4eY9QoAmKz-NlUsCTtDvS26pnVSuT8HcPpCQDcLsbaxew42TkIF_0cIUK0udGKRxOdYo9UnQWHfjy4_S5xABNhfsNZr1jx8JVMAn9xn-VyDteEQ14Kziv6lFOpmpA4MXvD_BPNAdME&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTcyOTU4MzA4ODE2NDMwMjA2OXxXbGdHS1E0dlZuc3JFZWh5SUkvVlI1NUp5TUVYQ1FrN3V1TWJzVUNibVdrPXwxYTY3MmI1MzFlMzkzY2E1ZGU1MGQ1NGE3MjdiMjczNV8xNzI5NTgzMDg5NjU4XzY3NWRkOWQ5YzUzNTRlZjI4YTY1MjFjYjRkZGI5NTEzXzE4OTk1ODUwNzR8NTM0ZmI0MzU0NDYyMGRiMTM4MDkzN2JiMjY3ZjhiMWJfMTcyOTU4MzA4Nzc0MV8yNTQ=",
#         # 2        sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; fzq_h=da53c88bc291080f187eb6807befe088_1729559751289_b9372eb777134921b5e2fa0fea3d9ef8_1899585074; id58=CkwARGcW/Mg62h7ND4F3Ag==; obtain_by=2; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; new_uv=2; fzq_js_anjuke_xiaoqu_pc=5de136d68b2f5e30c8dfcea3ec135c62_1729585162273_25; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729585168433&PBODY=jgEJgq8LxpqmZufEism76Q9ImvLvnMgxJYhvhbR1HGpjxv6ipwLeNc96fSg-KqANUVX1zDdR-MBm87DLda-UnFNQtlHx7oZcr96ILSai0syPNWx7zQ7ZyRUik8yVtEPvBsokdHbKPSXscSbdFTfuPikNdd7exgT0nAncJvyRcMo&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTU4NTE2NjgzMzMxMjI3N3xTOXJ6bnNBc0cwZTBhSFVRYi9qakRYd2l4U1hGbWMwVmFCcWt2dGs4VWhVPXw1ZTE2ZDlkYjk4NWQ3YjM1YTc1NGQxNWNmOWI1NjU4ZF8xNzI5NTg1MTY4NDY0X2RkOGZiYTEzNTNjOTQ3M2M5MWJkZGI0NWVhMTZkMTQ4XzE4OTk1ODUwNzR8NDM4OTFhNGY4NGYxNmQ4ZDVlZWM4MDk0MWM2NzZkYmJfMTcyOTU4NTE2NjUxOV8yNTY=
#         # 3        sessid=3BE8975B-A211-742F-746D-CA00BED38DF5; aQQ_ajkguid=C1804C4D-C339-DBB5-65D3-0A0D83425D92; ctid=22; twe=2; ajk-appVersion=; fzq_h=da53c88bc291080f187eb6807befe088_1729559751289_b9372eb777134921b5e2fa0fea3d9ef8_1899585074; id58=CkwARGcW/Mg62h7ND4F3Ag==; obtain_by=2; xxzlclientid=88c7292a-56f3-4b49-86a7-1729559751151; xxzlxxid=pfmxbU0YdPJbDTr0IFDR4ht2MqwLk3SDBw51L1XYH3F0wOyjT6Gw0YI6utmR2kydsIuN; isp=true; 58tj_uuid=dc36640e-4dc9-4cd2-99fe-8dc3e5f1293d; als=0; ajk_member_verify=Y%2BAzCx%2BeCb%2BI%2BgWH3Yvu7XydTGljnIj%2BKU9uBVdABDQ%3D; ajk_member_verify2=Mjk4MDc5Mjg1fExoaVQzclh8MQ%3D%3D; ajk_member_id=298079285; new_uv=2; fzq_js_anjuke_xiaoqu_pc=bf871f52d82652f228f54174424f1bd6_1729585744122_23; ajkAuthTicket=TT=cd7a063b27f88edac722ebbe67742dfd&TS=1729585746702&PBODY=PlvfTBSlnhkwkd54wYG4aavtvA6YEtw7boDvh7uYPqVCtIgy_iyMu5sXbbjA-ixt19LS9gKCI_nbtYeOs9tBf55uuDEkDlbUCvr0dZSlHM-pyKQ2huk287_PKcENQDq7wrHIprv0lS6QnxxX_yS_zBi2-u-C0WwJkF7ndKCHxrM&VER=2&CUID=t3j2DJQnjG5gLGMStevX5Qj5svAO2gEh; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTcyOTU4NTc0NTUwMjUxMDc5N3xJREdIQ09JS21GdXpQQWVjbmVUNlZla2dhTnFqMDh2cVQxaHZ2bUIrMTI0PXwwMDkyNTFjZGI1OGJjMDUyMGJlMTA5YTk5ZGQ3ZTVlZF8xNzI5NTg1NzQ2NDc1X2MzMmM3NzNmZTkyMTRlMjJiMDJjODdiMmZhYjZmZTZmXzE4OTk1ODUwNzR8ZGMwYzcyMmQ5YmQzNDBmNzE5YTQzMjNhNWViYjM0ZWJfMTcyOTU4NTc0NDczN18yNTU=
#     }
#     response = requests.get(url, headers=headers)
#     # print(response.text)
#     xml = etree.HTML(response.text)

#     # 获取小区名
#     communities_name = xml.xpath('//div[@class="nowrap-min li-community-title"]/text()')
#     # print(communities_name)

#     # 获取小区的链接
#     communities_urls = xml.xpath('//div[@class="list-cell"]//a[@class="li-row"]/@href')
#     with open("community_link.txt", "a", encoding="utf-8") as f:
#         for url, name in zip(communities_urls, communities_name):
#             # 生成随机数
#             # time.sleep(random.randint(1, 3))
#             process_detail_page(url, name)
#             f.write(url + "\n")

#     with open("page1.html", "w", encoding="utf-8") as f:
#         f.write(response.text)

#     with open("community_name.txt", "a", encoding="utf-8") as f:
#         for cn in communities_name:
#             f.write(cn + "\n")
