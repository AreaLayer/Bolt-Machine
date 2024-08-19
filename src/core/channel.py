from lndgrpc import Channel
from lndgrpc import RpcError

def main():
    channel = Channel("localhost:10009")
    try:
        channel.getinfo()
    except RpcError as e:
        print(e.code())
        print(e.message())
        print(e.details())
    print(e.metadata())
    