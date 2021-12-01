import requests
from requests.utils import dict_from_cookiejar

import requests

url = 'https://my.4399.com/forums/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    "Cookie": "home4399=yes; UM_distinctid=17d4112b95d7a2-09faf0599e54b4-b7a1438-144000-17d4112b95ed06; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1637474286; _gprp_c=""; USESSIONID=ad9d40cf-a0db-43de-80de-f129f5ecc7c8; Puser=2397544674; Qnick=; zone_guide_date=1637510400; _4399tongji_vid=163747516397941; _4399tongji_st=1637475163; _4399stats_vid=16374751642859260; ptusertype=my.4399_login; guide_share=0; guide_new_user_list=3663289649; phlogact=l124183; Uauth=4399|1|20211121|my.|1637477127604|6e8314a87a381c24e5e9a6e994d6c359; Pauth=3663289649|2397544674|t3ce7n1519274f877d712c56e1526220|1637477127|10002|ac2925b08d87d87c0be71882a8b6a688|0; ck_accname=2397544674; Xauth=da226b50fe28e9c93a338a4aae804e13; Sauth=3663289649%7C2397544674%7C1637477127%7C1638341286%7Ccbd57fa5660a3b63d9fb%7C%7C2397544674%7C02a48a06c130aef95331145aa85d8d63; zone_guide_limit=-1; zone_guide_time=0; zone_guide=-1; smidV2=202111211449374675849dc53350f1d2bb5f989340671e00f2aecd321e31220; myweb_auth=3663289649||nick||2397544674||3a03adaa74945e510a99e1c37bbae831; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1637475164,1637477390,1637477450; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1637475164,1637477390,1637477450; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1637481928; gdc_userMark=w41Be56Te93No-17DX14ZL48Fu6-1yg79Fo22Fg78-PH82yP56LD62Z; gdc_webRecordId=27ea5362-b9fa15-f8dbde; gdc_newStatCid=3001; gdc_newStatOid1=19204; channel_cid=3001; channel_uid=3001; WEB_PAGE_OID=18685; WEB_REFERER=http://web.4399.com/4399landing/cqbz.html?cid=3001&oid=19204&r=0.8195834794997923&__ref=1&__p__=http%253A%252F%252Fweb.4399.com%252F4399landing%252Fcqbz.html%253Fcid%253D3001%2526oid%253D19204%2526r%253D0.8195834794997923%2526baseoid%253D18685&; webRecordId=2383g23r-1avxtqm-rpdra; webRecordIdP=2383g23r-1avxtqm-mwomi; ol=1; Pnickset=1; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1637486555; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1637486555; Pmtime=66bd256d38dec143d8dc%7C1637486553"
}

response = requests.get(url=url, headers=headers)

response.encoding = 'utf-8'

print(response.text)