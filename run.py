import json
import os
import re

from jinja2 import Environment as je, FileSystemLoader as jfs

je = je(loader=jfs('.'))
je.filters['quote'] = (
    lambda x: re.sub('["\\\\]', lambda m: '\\{}'.format(m.group(0)), x)
)
servers = json.loads(os.environ['SERVERS'])


def render(source, dest, **kwargs):
    with open(dest, 'w') as out:
        out.write(je.get_template(source).render(**kwargs))

render(
    'nginx.conf.source',
    '/nginx.conf',
    servers=servers,
    password=os.environ['PASSWORD'],
)
for server in servers:
    render(
        'index.html.source',
        '/usr/share/nginx/html/index_s{}.html'.format(server[1]),
        server=server,
    )

os.execlp('nginx', '-g', '-c', '/nginx.conf')
