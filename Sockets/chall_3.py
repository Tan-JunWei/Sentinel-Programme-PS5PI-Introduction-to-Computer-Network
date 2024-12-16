import socket
import threading
import random

USERS_DB = {
'larry' : 0x496c6b43,
'bridget' : 0xf60977a6,
'billy' : 0x7e337272,
'peter' : 0xe8fbbcbe,
'donald' : 0x14107096,
'hilda' : 0xae1782a5,
'javier' : 0xf623bd34,
'juan' : 0x40ea256f,
'john' : 0xd8177179,
'carolyn' : 0x49559a18,
'jonathan' : 0x58478709,
'martin' : 0xea8e66ad,
'donna' : 0xfdf44767,
'helen' : 0xa4a9c387,
'michael' : 0x9b6baafd,
'velma' : 0x1758ade5,
'linda' : 0xee04ecb3,
'belinda' : 0x689c228d,
'tammy' : 0xeced5f47,
'florida' : 0x327f4716,
'ernest': 0xf93ac6de,
'debra': 0x3d20d707,
'freddie': 0x0c8e88bf,
'martha': 0x3d34adae,
'carol': 0xa3e664d1,
'patricia': 0xf4c66b2b,
'mattie': 0x88e9710a,
'samuel': 0xfe8b33f5,
'melissa': 0xbf9f24c4,
'charles': 0x0e28a0a2,
'jill': 0x5dd3ee0e,
'william': 0xa56ffef9,
'edith': 0x87b851cc,
'dawn': 0x41e2d253,
'scott': 0xcae427c8,
'raymond': 0x2f492ec1,
'robert': 0x037f1270,
'rudy': 0xe6b1d19b,
'meg': 0x852e7a7d,
'frederick': 0x35de9ab1,
'tyler': 0x01580988,
'david': 0x63814141,
'bill': 0x1330d34f,
'todd': 0x1378b9e0,
'thomas': 0xd634a520,
'graciela': 0x9d2fe22f,
'shelly': 0x8adc1f88,
'valerie': 0xf470de7d,
'kenneth': 0x504e3a64,
'jessica': 0x9be8620a,
}

SERVER_PORT = 42915

class ProtocolError(Exception):
    pass

def generate_challenge_response(username):
    challenge = random.randint(0,0xFFFFFFFF)
    password = USERS_DB[username]

    response = challenge ^ password
    response += sum([ord(c) for c in username])

    return challenge, response

def server_output(client, msg):
    client.send(msg.encode() + b'\n')

def client_input(client, expected_action, should_have_arg = False):
    # Read until newline
    msg = ''
    while True:
        c = client.recv(1).decode()
        if not c or c == '\n':
            break
        msg += c

    parts = msg.split('|')

    if len(parts) != 1 + int(should_have_arg):
        server_output(client, "ERROR Invalid message")
        raise ProtocolError()

    if parts[0] != expected_action:
        server_output(client, "ERROR Unexpected action")
        raise ProtocolError()

    return parts[1] if should_have_arg else None

def login(client):
    server_output(client, "LOGIN")
    username = client_input(client, "USERNAME", should_have_arg = True)
    if username not in USERS_DB:
        server_output(client, "ERROR Unknown username")
        return None

    challenge, response = generate_challenge_response(username)
    server_output(client, "CHALLENGE|%d" % challenge)
    client_response = client_input(client, "RESPONSE", should_have_arg = True)
    try:
        if int(client_response) == response:
            return username
        else:
            server_output(client, "ERROR Auth failure")
            return None
    except:
        server_output(client, "ERROR Invalid response")
        return None

def show_songs_for_client(client, username):
    with open('{}.lst'.format(username), 'r') as f:
        inbox = f.read()
        server_output(client, "SONGS\n" + inbox)

def handle(client):
    try:
        client_input(client, "START")
        server_output(client, "BANNER Welcome to Extra Simple Playlist Protocol server! Log in to see your saved list of favorite songs")
        username = login(client)
        if username:
            show_songs_for_client(client, username)
    except ProtocolError as e:
        pass

    client.close()

def main():
    print("* ESPP v3.0 Server started; listening for clients")
    s = socket.socket()
    s.bind(('0.0.0.0', SERVER_PORT))
    s.listen(50)
    while True:
        try:
            k, _ = s.accept()
            print("* Got client connection")
            k.settimeout(3)
            print("Client")
            threading.Thread(target=handle, args=(k,)).start()
        except:
            pass

if __name__ == '__main__':
    main()
