import requests

def bookappointments():
    auth = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIwMThlMTNlYS1hMjViLTQ2ZWQtYjIwMi0xNDdjYmJlNWM3NmQiLCJ1c2VyX3R5cGUiOiJCRU5FRklDSUFSWSIsInVzZXJfaWQiOiIwMThlMTNlYS1hMjViLTQ2ZWQtYjIwMi0xNDdjYmJlNWM3NmQiLCJtb2JpbGVfbnVtYmVyIjo4MDA4MjY2MzMwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjg0NzUzNDMwODU2MTcwLCJ0eG5JZCI6ImM5ZTQyODM5LTg3N2ItNGFjMy1hODVhLWIwMDhlZjNmYTQ0NyIsImlhdCI6MTYyMDk4NDg2MywiZXhwIjoxNjIwOTg1NzYzfQ.pB_eXo2CZBK40El50F9VLzY3BiVi_gdQGGt0Y7HZoOk'
    auth = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIwMThlMTNlYS1hMjViLTQ2ZWQtYjIwMi0xNDdjYmJlNWM3NmQiLCJ1c2VyX3R5cGUiOiJCRU5FRklDSUFSWSIsInVzZXJfaWQiOiIwMThlMTNlYS1hMjViLTQ2ZWQtYjIwMi0xNDdjYmJlNWM3NmQiLCJtb2JpbGVfbnVtYmVyIjo4MDA4MjY2MzMwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjg0NzUzNDMwODU2MTcwLCJ0eG5JZCI6IjJiNmJlMmMxLTg2YTUtNDUyZC1iMzdiLTNhMjdjMWQ2ZWQyZCIsImlhdCI6MTYyMTAxMjcwMCwiZXhwIjoxNjIxMDEzNjAwfQ.x1VeH8BxyDb7huACIN3yE53lJOYYT1oN_Mj_Ak0jIAE'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'Authorization': "Bearer {}".format(auth),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    print(headers)
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries'
    # url = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/findByPin'
    paramas = 'pincode=110001&date=15-05-2021&vaccine=COVAXIN'
    r = requests.get(url, params=paramas, headers=headers, verify=False)
    print(r)