#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, os, codecs

from StringIO import StringIO


def export(data, of, depth=1):
    '''Going thought the dict and print out every item with markdown
    @param data {dict} the postman structure
    @param of {file descriptor} for writing out the data
    @param depth {number} when recursing into "item"
    '''
    if 'name' in data:
      of.write("%s %s\n" % (depth*"#", data['name']))
    if 'info' in data:
      of.write("%s %s\n" % (depth*"#", data['info']['name']))
      if 'description' in data['info']:
          of.write("{}\n".format(data[u'info'][u'description']))
    if 'request' in data:
      of.write("%s %s\n" % ((depth+1)*"#", data['request'].get('name', 'request')))
      of.write("```\n%s %s\n```\n" % (
        data['request'].get('method', 'GET'),
        data['request'].get('url', 'GET')))
      if 'body' in data['request'] and data['request'].get('method', 'GET') not in ('GET', 'HEAD'):
        of.write("```\n%s\n```\n" % json.dumps(data['request'].get('body', ''), indent=4))
      if 'response' in data:
        for resp in data['response']:
          of.write("%s %s\n" % ((depth+1)*"#", resp.get('name', 'response')))
          if 'description' in resp:
            of.write("%s\n" % resp['description'])
          of.write("```\nHTTP/1.1 %s %s\n" % (resp['code'], resp['status']))
          for head in resp['header']:
            if head['name'] in ("Cache-Control", "Content-Type"):
                of.write("%s: %s\n" % (head['key'], head['value']))
          of.write("\n%s\n```\n" % json.dumps(resp['body'], indent=4))
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
        of = StringIO()
        export(data, of)
        of.seek(0)
        if len(sys.argv)>2:
            with codecs.open(sys.argv[2], mode='wb', encoding='utf-8') as out:
                out.write(of.read())
        else:
            print of.read()
    else:
      print("Could not find '{}'".format(fn))
  else:
    print("Usage:\n\t{} postman_collection.json > apidoc.md".format(sys.argv[0]))