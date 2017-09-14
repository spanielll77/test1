import requests
import json

"""
Modify these please
"""
url='http://nxosv/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "int eth1/1 ;desc abc",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print(response)
