package main

import (
	"log"
	"strconv"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "google.golang.org/sms"
)

const (
	address     = "localhost:50051"
	tel         = "2983493443"
	msg         = "w3"
)

func main() {
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewSMSClient(conn)
	r, err := c.Send(context.Background(), &pb.SMSRequest{Tel: tel, Msg: msg})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf(strconv.FormatInt(r.Status, 32))
}
