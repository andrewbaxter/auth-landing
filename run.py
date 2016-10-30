import json
import os
import crypt
import random

from jinja2 import Environment as je, FileSystemLoader as jfs

servers = json.loads(os.environ['SERVERS'])

with open('/password', 'w') as out:
    out.write(':{}\n'.format(crypt.crypt(
        os.environ['PASSWORD'],
        ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/.'
        ) for x in range(2)))).encode('ascii'))

je = je(loader=jfs('.'))
for pair in (
        ('nginx.conf.source', '/nginx.conf'),
        ('index.html.source', '/index.html')):
    with open(pair[1], 'w') as out:
        out.write(je.get_template(pair[0]).render(
            title=os.environ['TITLE'],
            servers=servers,
        ))

os.execl('nginx', '-g', '-c', '/nginx.conf')
