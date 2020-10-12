import socketio

sio = socketio.Client()


@sio.event
def response(response):
    print('I received a message!')
    print(response)


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error():
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


def Sendmsg():
    print("hello")
    sio.emit('message', "spinup magnum infra")


if __name__ == '__main__':
    sio.connect('http://54.184.146.53:8090')
    Sendmsg()
