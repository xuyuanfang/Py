import requests
import json

#
#
# data = {}
# a = 0
# Token = []
# for i in range(100,165):
#
#     url = 'http://192.168.83.200:8088/api/users/{}/token'.format(i)
#     re = requests.request(method='get',
#                           url=url,
#                           headers={"token":"Z3F5d3ZyLDE4ODQ1ODQ3ODk2NTIsMTY0Y2RmNTVhOWE3NmRjZDdjMmQ4NzQ0MWZlZDdlYzU="})
#     if a <= 30:
#         if re.status_code == 200:
#             # print(re.text)
#             # print(re.json())
#             Token.append(re.json())
#     else:
#         break
#     a += 1
#
# print(Token)
#
# for i in Token:
#     headers= i
#     url = 'http://192.168.83.200:8088/api/orders'
#     data = {"mission":[{"type":"move","destination":38,"map_id":11,"action_id":0,"action_param1":0,"action_param2":0},{"type":"move","destination":44,"map_id":11,"action_id":0,"action_param1":0,"action_param2":0}],"priority":0,"handle_type":"single"}
#     re = requests.request(method='post',url=url,headers=headers,json=data)
#     print(re.text)
###########################################################################################
# header = {'token':'YWRtaW4sMTU3MjIzMTM3MDE1OSwyMTFhOWI0ZWZkMzlmYjA3OTQxM2ZiZTNjZDRkZDY3OQ=='}
# for i in range(0,200):
#     url = 'http://192.168.83.200:8088/api/users/{}'.format(i)
#     re = requests.request(method='DELETE',headers=header,url=url)
#     print(i)


###########################################################################################
# url1 = 'http://192.168.83.200:8088/api/orders/template/84'
# url2 = 'http://192.168.83.200:8088/api/orders/template/83'
# url3 = 'http://192.168.83.200:8088/api/orders/template/82'


# header = {'token':'YWRtaW4sMTg4NjIxMjA0MTA5OSxkODQ5ZjE5ZDE1OTIwNDUzYmQyNWE5M2E2NTA1OGNjMQ=='}
# for _ in range(100):
#     for i in range(95,100):
#         url = 'http://192.168.83.200:8088/api/orders/template/{}'.format(i)
#         re = requests.request(method='POST',url=url,headers = header)
#         # re2 = requests.request(method='POST',url=url2,headers = header)
#         # re3 = requests.request(method='POST',url=url3,headers = header)
#         print('range {}'.format(i))
#         print(re.status_code)
################################################################
#
# import numpy as np
#
# point = [i for i in range(109,134)]
# print(point)
# header = {'token':'YWRtaW4sMTg4NjIxMjA0MTA5OSxkODQ5ZjE5ZDE1OTIwNDUzYmQyNWE5M2E2NTA1OGNjMQ=='}
# mession = {"mission":[
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0},
#             {"type":"move","destination":{},"map_id":28,"action_id":0,"action_param1":0,"action_param2":0}],
#             "priority":0,"handle_type":"single"}
#
# for i in range(1):
#     get_point = np.random.choice(point,size=10,replace=False)
#     for p in range(10):
#         mession["mission"][p]['destination'] = int(get_point[p])
#     print(mession,type(mession))
#     re = requests.request(method='post',url='http://192.168.83.200:8088/api/orders',headers=header,json=mession)
#     print(re.status_code)

######################################################################
######################################################################

import numpy as np


Range = 10000000
map_id = 11


point1 = [73,74,75,76,85]
point2 = [86,77]
point3 = [88]

header = {'token':'YWRtaW4sMTg4NjIxMjA0MTA5OSxkODQ5ZjE5ZDE1OTIwNDUzYmQyNWE5M2E2NTA1OGNjMQ=='}

for i in range(Range):
    p1 = int(np.random.choice(point1,size=1,replace=False))
    p2 = int(np.random.choice(point2,size=1,replace=False))
    p3 = int(np.random.choice(point3,size=1,replace=False))
    p = [p1,p2,p3]
    # print(p)
    vehicle_id = int(np.random.choice([1,2,3],size=1))
    mession = {"mission": [
        {"type": "move", "destination": 67, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0},
        {"type": "move", "destination": 66, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0}],
        "priority": 0, "handle_type": "single"}

    mession2 = {"mission": [
        {"type": "move", "destination": 70, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0},
        {"type": "move", "destination": 71, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0}],
        "priority": 0, "handle_type": "single"}
# ,'appoint_vehicle_id':vehicle_id

    # mession1 = {"mission":[
    #     {"type":"move","destination":82,"map_id":6},
    #     {"type":"act","dst":"0","action_name":"","is_preinstall":0,"action_template_id":0,"action_id":78,"action_param1":1,"action_param2":0}],
    #     "appoint_vehicle_id":2,"priority":0,"handle_type":"single"}

    re = requests.request(method='post',url='http://192.168.83.200:8088/api/orders',headers=header,json=mession)
    re = requests.request(method='post',url='http://192.168.83.200:8088/api/orders',headers=header,json=mession2)

    if re.status_code != 200:
        print(re.text)
    else:
        print(re.status_code)

#######################################################################
#######################################################################

# import numpy as np


# Range = 100
# map_idA = 3
# A_point = 88
# map_idB = 2
# B_point1 = int(np.random.choice([73,74,75,76,85],size=1,replace=False))
# B_point2 = int(np.random.choice([77,86],size=1,replace=False))

# map_idC = 4
# C_point1 = int(np.random.choice([63,37],size=1))
# C_point2 = int(np.random.choice([35,36],size=1))


# print(B_point1,B_point2) 

# header = {'token':'YWRtaW4sMTg4NjIxMjA0MTA5OSxkODQ5ZjE5ZDE1OTIwNDUzYmQyNWE5M2E2NTA1OGNjMQ=='}

# mession1 = {"mission": [
#     {"type": "move", "destination": B_point1, "map_id": map_idB, "action_id": 0, "action_param1": 0, "action_param2": 0},
#     {"type": "move", "destination": A_point, "map_id": map_idA, "action_id": 0, "action_param1": 0, "action_param2": 0}
#     ],
#     "priority": 0, "handle_type": "single"}

# print(mession1)

# # mession2 = {"mission": [
# #     {"type": "move", "destination": 95, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0},
# #     {"type": "move", "destination": 93, "map_id": map_id, "action_id": 0, "action_param1": 0, "action_param2": 0}],
# #     "priority": 0, "handle_type": "single"}

# for i in range(int(Range)):
#     re1 = requests.request(method='post',url='http://192.168.83.200:8088/api/orders',headers=header,json=mession1)
#     # re2 = requests.request(method='post',url='http://192.168.83.200:8088/api/orders',headers=header,json=mession2)

#     if re1.status_code != 200 and re2.status_code != 200:
#         print(re1.text,'round:{}'.format(i))
#     else:
#         print(re1.status_code)