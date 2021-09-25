# From https://gist.github.com/aplz/537826ee96c9097a405f4c20c6164e5d
# I have edited this for 3-fold CV and the addition of precision and recall metrics,
# as well as compatibility with the latest fasttext version
import argparse
import os

import fasttext
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score, StratifiedKFold


def read_data(data_dir):
    """
    Import data from a directory. Each of the child directories is assumed to be the label for the files contained in it.
    :param data_dir: the path to a data directory.
    :return: texts, labels: the list of (unprocessed) text files and the list of associated labels.
    """
    print("Converting files from %s to fasttext format." % data_dir)
    texts = []
    labels = []
    for root_directory, child_directories, files in os.walk(data_dir):
        for child_directory in sorted(child_directories):
            label = child_directory
            for sub_root, sub_child_directories, actual_files in os.walk(os.path.join(root_directory, child_directory)):
                for filename in actual_files:
                    file_path = os.path.join(root_directory, child_directory, filename)
                    with open(file_path, 'r') as text_file:
                        text = text_file.read()
                        text = text.lower().replace("\n", " ")
                        if text is None:
                            print("Could not extract text from %s!" % file_path)
                            continue
                        texts.append(text)
                        # append the label in the format as expected by fasttext
                        labels.append("__label__%s" % label)
    print("Imported %s text files." % len(texts))
    return texts, labels


class FasttextEstimator(BaseEstimator):

    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.model = None

    def fit(self, features, labels):
        """
        Train fasttext on the given features and labels.

        :param features: a list of documents.
        :param labels: the list of labels associated with the list of features.
        """
        store_file(os.path.join(self.model_dir, "train.txt"), features, labels)
        self.model = fasttext.train_supervised(os.path.join(self.model_dir, "train.txt"),
                            thread=1, minn=0, maxn=10, bucket=1)
        # self.model = fasttext.load_model(os.path.join(self.model_dir, "CV_model/cv_model.bin"), encoding='utf-8')
        return self

    def score(self, features, labels):
        """
        Compute the macro-f1 score for the predictions on the given features.
        :param features: a list of documents.
        :param labels: the list of labels associated with the list of features.
        :return: f1_score: the macro-f1 score for the predictions on the given features.
        """
        predicted_labels = []
        predictions = self.model.predict(features)
        for prediction in predictions:
            predicted_label = prediction[0][0]
            predicted_labels.append(predicted_label)
        return f1_score(labels, predicted_labels, average="macro")


def store_file(output_file, features, labels):
    """Write the training data in fasttext format to disk.

    :param output_file: the name of the output file.
    :param features: the features, a list of strings.
    :param labels: the labels associated with features.
    """
    with open(output_file, 'w') as f:
        for i in range(0, len(features)):
            f.write("%s %s\n" % (labels[i], features[i]))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", help="path to the directory containing training data",
                    default="/home/user/fasttext_data/")
    ap.add_argument("--model_dir", help="path to the model directory", default="/home/user/temp/")
    args = vars(ap.parse_args())
    texts, labels = read_data(data_dir=args["directory"])
    # print(texts, labels)
    print(np.shape(labels))

    estimator = FasttextEstimator(model_dir=args["model_dir"])
    score = cross_val_score(estimator, texts, labels, cv=StratifiedKFold(n_splits=3), verbose=5)
    print(score)
