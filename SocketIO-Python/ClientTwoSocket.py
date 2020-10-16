import socketio
import time

sio1 = socketio.Client()
sio2 = socketio.Client()


@sio1.event
def message(message):
    print('I received a message!', message)
    sio2.emit('response2', message)

# Checking Event Start


@sio2.event
@sio1.event
def connect():
    print("I'm connected!")


@sio2.event
@sio1.event
def connect_error():
    print("The connection failed!")


@sio2.event
@sio1.event
def disconnect():
    print("I'm disconnected!")

# Checking Event Stop

# Checking Event Start 2


@sio2.event
def response2(response2):
    print('I received a message!', response2)
    sio1.emit('response', response2)

# Checking Event Stop 2


if __name__ == '__main__':
    sio1.connect('http://192.168.43.92:5000')
    sio2.connect('http://192.168.43.92:5001')
