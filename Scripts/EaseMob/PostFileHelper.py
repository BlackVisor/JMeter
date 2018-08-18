# -*- coding: utf-8 -*-
#encoding:utf-8    #设置编码方式
import httplib
import mimetypes
import json
import sys
import urllib2
import codecs

class PostFileHelper:
    def __init__(self,host, fields, files):
        self.host = host
        #self.selector = selector
        self.fields = fields
        self.files = files

    def post_multipart(self):
        content_type, body = self.encode_multipart_formdata(self.fields, self.files)
        req = urllib2.Request(self.host, data=body)
        req.add_header('Content-Type', '%s' % content_type)
        req.add_header('User-Agent', 'Mozilla/5.0')
        resp = urllib2.urlopen(req, timeout=20)
        # get response
        qrcont = resp.read()
        return qrcont
        '''
        h = httplib.HTTP(self.host)
        #h.putrequest('POST', self.selector)
        h.putheader('content-type', content_type)
        h.putheader('content-length', str(len(body)))
        h.endheaders()
        h.send(body)
        errcode, errmsg, headers = h.getreply()
        return h.file.read()
        '''
    def ReadFileAsContent(self,filename):
        # print filename
        try:
            with open(filename, 'rb') as f:
            #with codecs.open(filename, encoding='utf-8') as f:
                filecontent = f.read()
        except Exception, e:
            print 'The Error Message in ReadFileAsContent(): ' + e.message
            return ''
        return filecontent

    def encode_multipart_formdata(self,fields, files):
        LIMIT = '----------lImIt_of_THE_fIle_eW_$'
        CRLF = '\r\n'
        L = []
        for key, value in fields.items():
            L.append('--' + LIMIT)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        if len(files) > 0:
            filejson = json.loads(files)
            name = filejson["name"]
            filelist = filejson["files"]
            for item in filelist:
                path = item["filePath"]
                L.append('--' + LIMIT)
                L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (name, path))
                L.append('Content-Type: %s' % self.get_content_type(path))
                L.append('')
                L.append(self.ReadFileAsContent(path))
        L.append('--' + LIMIT + '--')
        L.append('')
        body = CRLF.join(L)
        content_type = 'multipart/form-data; boundary=%s' % LIMIT
        return content_type, body

    def get_content_type(self,filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'