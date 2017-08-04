# -*- coding: utf-8 -*-
import os
import urllib
import urllib2

from concurrent import futures
import time

import grpc

import sms_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
HOST = os.environ.get('SMS_HOST', 'http://x.x.x.x/mt?')
USER = os.environ.get('SMS_USER', 'user')
PWD = os.environ.get('SMS_PWD', 'pwd')

tel = '28719849184'
msg = u'msg'


def send_sms(tel, msg):

    msg = msg.encode('gbk').encode('hex')
    data = dict(un=USER, pw=PWD, da=tel, sm=msg, dc=15, rd=0)
    f = urllib2.urlopen(url=HOST, data=urllib.urlencode(data))
    r = f.read()
    print r
    # res = eval('dict(%s)' % r)
    # res = dict((l.split('=') for l in r.split(',')))
    f.close()
    return r


class SMS(sms_pb2.SMSServicer):

    def Send(self, request, context):
        status = 0
        resp = send_sms(request.tel, request.msg)
        if isinstance(resp, basestring) and resp.startswith('id='):
            status = 1
        return sms_pb2.SMSReply(status=status)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sms_pb2.add_SMSServicer_to_server(SMS(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
