import socket
import cv2
import numpy

TCP_IP = "192.168.8.101"
TCP_PORT = 8002

sock = socket.socket()
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
sock.connect((TCP_IP, TCP_PORT))
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
while ret:
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );

    ret, frame = capture.read()
    decimg=cv2.imdecode(data,1)
    cv2.imshow('CLIENT',decimg)
    cv2.waitKey(30)

sock.close()
cv2.destroyAllWindows()
