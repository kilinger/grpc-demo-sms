# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sms.proto',
  package='sms',
  syntax='proto3',
  serialized_pb=_b('\n\tsms.proto\x12\x03sms\"&\n\nSMSRequest\x12\x0b\n\x03tel\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x1a\n\x08SMSReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32/\n\x03SMS\x12(\n\x04Send\x12\x0f.sms.SMSRequest\x1a\r.sms.SMSReply\"\x00\x42/\n\x14io.grpc.examples.smsB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SMSREQUEST = _descriptor.Descriptor(
  name='SMSRequest',
  full_name='sms.SMSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tel', full_name='sms.SMSRequest.tel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='sms.SMSRequest.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=56,
)


_SMSREPLY = _descriptor.Descriptor(
  name='SMSReply',
  full_name='sms.SMSReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='sms.SMSReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['SMSRequest'] = _SMSREQUEST
DESCRIPTOR.message_types_by_name['SMSReply'] = _SMSREPLY

SMSRequest = _reflection.GeneratedProtocolMessageType('SMSRequest', (_message.Message,), dict(
  DESCRIPTOR = _SMSREQUEST,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:sms.SMSRequest)
  ))
_sym_db.RegisterMessage(SMSRequest)

SMSReply = _reflection.GeneratedProtocolMessageType('SMSReply', (_message.Message,), dict(
  DESCRIPTOR = _SMSREPLY,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:sms.SMSReply)
  ))
_sym_db.RegisterMessage(SMSReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024io.grpc.examples.smsB\017HelloWorldProtoP\001\242\002\003HLW'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SMSStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Send = channel.unary_unary(
        '/sms.SMS/Send',
        request_serializer=SMSRequest.SerializeToString,
        response_deserializer=SMSReply.FromString,
        )


class SMSServicer(object):

  def Send(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SMSServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Send': grpc.unary_unary_rpc_method_handler(
          servicer.Send,
          request_deserializer=SMSRequest.FromString,
          response_serializer=SMSReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sms.SMS', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaSMSServicer(object):
  def Send(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSMSStub(object):
  def Send(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Send.future = None


def beta_create_SMS_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('sms.SMS', 'Send'): SMSRequest.FromString,
  }
  response_serializers = {
    ('sms.SMS', 'Send'): SMSReply.SerializeToString,
  }
  method_implementations = {
    ('sms.SMS', 'Send'): face_utilities.unary_unary_inline(servicer.Send),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SMS_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('sms.SMS', 'Send'): SMSRequest.SerializeToString,
  }
  response_deserializers = {
    ('sms.SMS', 'Send'): SMSReply.FromString,
  }
  cardinalities = {
    'Send': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'sms.SMS', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
