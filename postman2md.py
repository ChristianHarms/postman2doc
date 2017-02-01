#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, os, codecs, xml.dom.minidom

from StringIO import StringIO

HEADER_VISIBLE = ("Cache-Control", "Content-Type")

def export(data, of, depth=1):
    '''Going thought the dict and print out every item with markdown
    @param data {dict} the postman structure
    @param of {file descriptor} for writing out the data
    @param depth {number} when recursing into "item"
    '''
    temp = { 'name': depth*"#" + ('info' in data and data['info'].get('name', '') or data.get('name', '')),
             'desc': 'info' in data and data['info'].get('description', '') or '',
             }
    if temp['name']:
        of.write('''{name}\n{desc}\n'''.format(**temp))

    if 'request' in data:
        temp = {'request': (depth+1)*"#" + data['request'].get('name', 'request'),
                'method': data['request'].get('method', 'GET'),
                'url': data['request'].get('url', '/api'),
                'requestbody': ''}
        #parse and prettyprint body as md-quote on javascript
        if data['request'].get('body', {}).get('raw', ''):
            try:
                bodydata = json.loads(data['request']['body'].get('raw'))
                temp['requestbody'] = '```javascript\n%s\n```\n' % json.dumps(bodydata, indent=4)
            except:
                temp['requestbody'] = '```\n%s\n```' % data['request']['body']
        of.write('{request}\n```\n{method} {url}\n```\n{requestbody}\n'.format(**temp))

    if 'response' in data:
        for resp in data['response'][:1]:
            #parse and prettyprint body as md-quote (json/xml/plain)
            if resp.get('_postman_previewlanguage','') == "json":
                body = '```javascript\n%s\n```\n' % json.dumps(json.loads(resp['body']), indent=4)
            elif resp.get('_postman_previewlanguage','') == 'xml':
                node = xml.dom.minidom.parseString(resp['body'].strip('"'))
                body = '```xml\n%s\n```\n' % node.toprettyxml()
            else:
                body = '```\n%s\n```\n' % body
            temp = {'response': (depth+1)*"#" + resp.get('name', 'response'),
                    'httpline': 'HTTP/1.1 %s %s' % (resp['code'], resp['status']),
                    'header': '\n'.join('%s: %s' % (x['key'], x['value']) for x in resp['header'] if x['key'] in HEADER_VISIBLE),
                    'responsebody': body
                    }
            of.write('{response}\n```\n{httpline}\n{header}\n```\n{responsebody}\n'.format(**temp))

    if 'item' in data:
      for item in data['item']:
        export(item, of, depth+1)
#export

if __name__=='__main__':
  if len(sys.argv)>1:
    fn = sys.argv[1]
    if os.path.exists(fn):
      with open(fn) as fp:
        data = json.load(fp, encoding='utf-8')
        export(data, len(sys.argv)>2 and codecs.open(sys.argv[2], mode='wb', encoding='utf-8') or sys.stdout)
    else:
      print("Could not find '{}'".format(fn))
  else:
    print("Usage:\n\t{} postman_collection.json > apidoc.md".format(sys.argv[0]))