# -*- coding: utf-8 -*-
from __future__ import print_function

import grpc

import sms_pb2

tel = '298349843'
msg = u'wo'


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = sms_pb2.SMSStub(channel)
    response = stub.Send(sms_pb2.SMSRequest(tel=tel, msg=msg))
    print(response.status)


if __name__ == '__main__':
    run()
