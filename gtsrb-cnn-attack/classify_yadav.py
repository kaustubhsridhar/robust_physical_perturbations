import sys 
import os

import cv2
import tensorflow as tf
import numpy as np
from tensorflow.python.platform import app
from tensorflow.python.platform import flags

from utils.model import YadavModel
from utils.dataproc import read_img, preprocess_yadav
from utils.eval import top3_as_string
import pandas as pd # added

import cv2

FLAGS = flags.FLAGS
flags.DEFINE_string('weights', "./models/gtsrb_usstop/model_best_test", 'path to the weights for the Yadav model')
flags.DEFINE_string('srcimgs', 'bb_images/mcity_iphone_27Aug/grab_mcity_iphone_advstop', 'Path to the images to be classified.')


def main(argv=None):
    d = {} # added
    imgnames = filter(lambda x: x.lower().endswith(".jpg") or x.lower().endswith(".png"), os.listdir(FLAGS.srcimgs))
    imgs = np.asarray(map(lambda x: preprocess_yadav(x),
                          map(lambda x: cv2.resize(read_img(os.path.join(FLAGS.srcimgs, x)), (FLAGS.img_cols, FLAGS.img_rows)),
                              imgnames))
                      , dtype=np.float32)
    imgs = imgs[:,:,:] # imgs[:5000,:,:] takes first 5000 and imgs[5000:,:,:] will do the rest
    print 'Loaded images from %s'%FLAGS.srcimgs
    sys.stdout.flush()
    results = []
    with tf.Session() as sess:
        model = YadavModel(train=False)
        saver = tf.train.Saver()
        saver.restore(sess, FLAGS.weights)
        print 'Loaded model from %s'%FLAGS.weights
        sys.stdout.flush()
        print("anticipation of softmax production") #too many images causes below line to fail for some reason
        output = sess.run(model.labels_pred, feed_dict={model.features: imgs, model.keep_prob: 1.0}) 
        print("completion of softmax production")
        for i in range(len(imgs)):
            d.update({imgnames[i]: list(output[i])}) # added
            results.append((imgnames[i], top3_as_string(output, i)))
    for i in range(len(results)):
        print results[i][0], results[i][1]

    df = pd.DataFrame(d).T # added
    df.to_csv(FLAGS.srcimgs+"/predictions.csv") # added

if __name__ == "__main__":
    app.run()
