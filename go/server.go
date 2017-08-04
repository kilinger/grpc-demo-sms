package main

import (
	"os"
	"log"
	"net"
	"fmt"
	"bytes"
	"strings"
	"net/http"
	"io/ioutil"

	"github.com/axgle/mahonia"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "google.golang.org/sms"
)

const (
	HOST = os.Getenv("SMS_HOST") || "http://x.x.x.x/mt?"
	USER = os.Getenv("SMS_USER") || "user"
	PWD = os.Getenv("SMS_PWD") || "pwd"
	port = ":50051"
)

type server struct{}

func Urlencode(data map[string]string) string {
	var buf bytes.Buffer
	for k, v := range data {
		buf.WriteString(k)
		buf.WriteByte('=')
		buf.WriteString(v)
		buf.WriteByte('&')
	}
	s := buf.String()
	return s[0 : len(s) - 1]
}

func (s *server) Send(ctx context.Context, in *pb.SMSRequest) (*pb.SMSReply, error) {
	enc := mahonia.NewEncoder("gbk")
	msg := enc.ConvertString(in.Msg)
	msg = fmt.Sprintf("%x", msg)
	data := map[string]string{"un": USER, "pw": PWD, "da": in.Tel, "sm": msg, "dc": "15", "rd": "0"}
	url := HOST + Urlencode(data)
	res, err := http.Get(url);
    if err != nil {
        log.Fatal(err)
    }
    result, err := ioutil.ReadAll(res.Body)
    res.Body.Close()
    if err != nil {
		log.Fatal(err)
    }
	var status int64 = 0
	if strings.HasPrefix(string(result), "id=") {
		status =1
	}

	return &pb.SMSReply{Status: status}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterSMSServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
