from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO nyu.edu\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCmd = "MAIL FROM:<js14094@nyu.edu>\r\n"
    clientSocket.send(mailFromCmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCmd = "RCPT TO:<admin@nyu.edu>\r\n"
    clientSocket.send(rcptToCmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCmd = "DATA\r\n"
    clientSocket.send(dataCmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: SMTP CLIENT\r\n\r\n"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCmd = "QUIT\r\n"
    clientSocket.send(quitCmd.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')