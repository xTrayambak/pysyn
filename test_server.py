from pydatanet.server import Server, ServerType

def onPacketSend(sender, data):
    print(f"{sender.getIp()} sent me this!: {data}")

s = Server(
    "localhost", 5050, ServerType.TCP
)
s.on_recv_bind(onPacketSend)
s.connect()