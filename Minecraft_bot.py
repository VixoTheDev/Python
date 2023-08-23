import socket
import time

def send_mesage(client_socket, chat_message):
    chat_packet = b'\x02' + len(chat_message).to_bytes(2, byteorder='big') + chat_message.encode() # create packet that will send chat message
    client_socket.send(chat_packet) # send chat message 

def set_nickname(client_socket, nickname):
    nickname_packet = b'\xFE\xFD\x09' + b'\x00' + nickname.encode() + b'\x00' # create packet that will set bot nickname
    client_socket.send(nickname_packet) # set bot nickname

server_ip = "your_server_ip_here" # Server IP (don't use domian)
server_port = 25565 # Server Port 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Socket 

try:
    client_socket.connect((server_ip, server_port)) # Connect bot to server
     
    print("Connected to the server") # sends message to console

    nickname = "test_bot" # nickname of bot

    time.sleep(2)  # wait for 2 seconds before sending message

    send_mesage(client_socket, "Test Message") # Send message to server using bot

except socket.error as e: #if connecting bot cause erorro it will enable code 
    print("Error:", e) # send error message to console

finally: # if connecting bot dont casue error it will enable code
    client_socket.close() # Close socket. that will disconnect bot from server
    print("Socket closed") # sends message to console
