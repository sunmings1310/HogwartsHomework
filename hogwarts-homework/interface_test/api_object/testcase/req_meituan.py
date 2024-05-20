import requests


url = 'https://h5.waimai.meituan.com/waimai/mindex/home'

cookies = {
    '_lxsdk_cuid': '1742417b8e9c8-0e44d47d19ff95-5a472316-1fa400-1742417b8e9c8',
    'iuuid': 'F14A52FEE04B2F09156651A779EAA43CDE22FBB83482FF71907A7523CEF4024F',
    'ci': '55',
    'cityname': '%E5%8D%97%E4%BA%AC',
    'WEBDFPID': '021011x92461506z042yvx13zx9w5w7781w262zw7zz9795886403yw2-2022399444899-1707039444490OSAOWGIfd79fef3d01d5e9aadc18ccd4d0c95078234',
    'uuid': '1f97f665638c4434a295.1709627595.1.0.0',
    'mtcdn': 'K',
    'wm_order_channel': 'default',
    'utm_source': '',
    'igateApp': 'igate',
    '_lx_utm': 'utm_source%3Dgoogle%26utm_medium%3Dorganic',
    '_lxsdk': 'F14A52FEE04B2F09156651A779EAA43CDE22FBB83482FF71907A7523CEF4024F',
    'au_trace_key_net': 'default',
    'openh5_uuid': 'F14A52FEE04B2F09156651A779EAA43CDE22FBB83482FF71907A7523CEF4024F',
    'isIframe': 'false',
    'showTopHeader': 'show',
    'isTcMpa': 'false',
    'token': 'AgHAH7uYACikY0W96jvDBSxrSMO4NlywV1mW7hg3MFzGhglmqia6ae_QPHewb44MInhCcawcPvUfKAAAAAB1HgAADJy3_-uPCxNlm9AsVFIIzQNRL3Y4O6487-pmwFCYZ-sMjcNh4MGAtRduBZhWyngG',
    'mt_c_token': 'AgHAH7uYACikY0W96jvDBSxrSMO4NlywV1mW7hg3MFzGhglmqia6ae_QPHewb44MInhCcawcPvUfKAAAAAB1HgAADJy3_-uPCxNlm9AsVFIIzQNRL3Y4O6487-pmwFCYZ-sMjcNh4MGAtRduBZhWyngG',
    'oops': 'AgHAH7uYACikY0W96jvDBSxrSMO4NlywV1mW7hg3MFzGhglmqia6ae_QPHewb44MInhCcawcPvUfKAAAAAB1HgAADJy3_-uPCxNlm9AsVFIIzQNRL3Y4O6487-pmwFCYZ-sMjcNh4MGAtRduBZhWyngG',
    'userId': '285437242',
    'userIdCanceled': '0',
    'uuidCanceled': '0',
    'logan_session_token': 'ewt9k4qcowdbvfu79upw',
    'userName': '%E4%B9%85%E4%BC%B4%E4%B8%80%E4%B8%AAGirl',
    'userFace': 'https://img.meituan.net/avatar/31178d7b9069dc6c9e54dd7334a3d09f1717.jpg',
    '_lxsdk_s': '18e12648762-1d7-e65-62a%7C%7C92'
}

response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    # Print the entire content of the response
    print(response.content)
else:
    # Print status code and reason for failure if the request was not successful
    print(f"Failed to retrieve the content. Status Code: {response.status_code}. Reason: {response.reason}")