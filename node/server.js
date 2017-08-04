var grpc = require('grpc');
var PROTO_PATH = __dirname + '/../sms.proto';
var proto = grpc.load(PROTO_PATH).sms;

var request = require("request");
var querystring = require('querystring');
var urllib = require('urllib');
var iconv = require("iconv-lite");

var HOST = process.env.SMS_HOST || 'http://x.x.x.x/mt?';
var USER = process.env.SMS_USER || 'user';
var PWD = process.env.SMS_PWD || 'pwd';

function send(call, callback) {
    var status = 0,
        tel = call.request.tel,
        msg = iconv.encode(call.request.msg, 'gbk').toString('hex'),
        data = {un: USER, pw: PWD, da: tel, sm: msg, dc: 15, rd: 0},
        url = HOST + querystring.stringify(data);

    urllib.request(url).then(function (result) {
        result = result.data.toString();
        status = (typeof(result) === 'string' && result.startsWith('id=')) ?1:0;
        console.log(typeof(result), result);
        //console.log(typeof(result), result.data.toString());
        return status
    }).then(function (status) {
        console.log(status);
        callback(null, {status: status});
    }).catch(function (err) {
        console.error(err);
        callback(null, {status: status});
    });

    //callback(null, {status: status});
}

function main() {
    var server = new grpc.Server();
    server.addProtoService(proto.SMS.service, {send: send});
    server.bind('0.0.0.0:50052', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();
