'''
import cv2 as cv


def video_demo():
    #0是代表摄像头编号，只有一个的话默认为0
    capture = cv.VideoCapture(0)
    while (True):
        ref, frame = capture.read()

        cv.imshow("1", frame)
        #等待30ms显示图像，若过程中按“Esc”退出
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break


video_demo()
cv.waitKey()
cv.destroyAllWindows()
'''
import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.compat.v1.Session()

# Run the op
#print(sess.run(hello))