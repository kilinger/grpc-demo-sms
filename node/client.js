var grpc = require('grpc');
var PROTO_PATH = __dirname + '/../sms.proto';
var proto = grpc.load(PROTO_PATH).sms;

var tel = '2938478374';
var msg = 'ed';


function main() {

  var client = new proto.SMS('localhost:50052',
                             grpc.credentials.createInsecure());
  client.send({tel: tel, msg: msg}, function(err, response) {
    console.log('STATUS:', response.status);
  });
}

main();
