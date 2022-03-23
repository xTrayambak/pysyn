from pydatanet.client import Client, ClientType

def myFuncOnReceiveTCP(data_decoded):
    print(f"I got some data: {data_decoded}")

c = Client(ClientType.UDP)
c.hook_tcp_recv(myFuncOnReceiveTCP)
c.connect("localhost", 5050)
c.send(
    {
        "joemama": True,
        "hello": "world",
        "foo": "bar",
        "data": {
            "name": "joe",
            "age": 33,
            "nationality": "joemamian"
        }
    }
)