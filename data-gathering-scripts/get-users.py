#!/usr/bin/env python3

import json

city = 'San%20Diego'
users = []
wname = 'users/{}.txt'.format(city)

for i in range(1,51):
    fname = 'queries/{}{}.json'.format(city, i)
    uf = None
    with open(fname, 'r') as f:
        uf = json.loads(f.read())
    for u in uf:
        if u['location'] is not "":
            user_info = {'name': u['name'], 'id': u['id'], 'location': u['location']}
            users.append(json.dumps(user_info))


with open(wname, 'w') as f:
    for user in users:
        f.write("{}\n".format(user))

