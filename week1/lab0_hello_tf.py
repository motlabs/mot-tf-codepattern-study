'''

filename: lab0_hello_tf.py
description: The purpose of this script check whether you install tensorflow correctly.

author : jaewook kang 2018 june

'''

import tensorflow as tf

hello   = tf.constant('Hello, TensorFlow!')
sess    = tf.Session()
print ('[Lab0] %s' % sess.run(hello))
# Hello, TensorFlow!
a = tf.constant(10)
b = tf.constant(32)
print ('[Lab0] a + b = %s' % sess.run(a+b))
# 42
