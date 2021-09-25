import os
import os.path
import numpy as np
import fasttext
from sklearn.model_selection import KFold

K = 3
random_state = 2
per_class_results_cv = {
    "u": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "pbl": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "pbr": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "pcl": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "pcr": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "rotl": {"recall_scores": [], "precision_scores": [], "f1_scores": []},
    "rotr": {"recall_scores": [], "precision_scores": [], "f1_scores": []}
 }

dataset_dir = "CV_dataset/"

for label in per_class_results_cv.keys():
    label_dir = dataset_dir + label + "/"
    num_samples = len([name for name in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, name))])
    # print(label, num_samples)
    sample_ids = [i for i in range(num_samples)]
    # print(sample_ids)

splits = []
for train_index, test_index in KFold(n_splits=K, random_state=random_state, shuffle=True).split(sample_ids):
    splits.append([train_index, test_index])

for split in splits:
    with open("temp_cv_training_data.txt", "w") as temp_cv_training_set:
        training_data = []
        for label in per_class_results_cv.keys():
            label_dir = dataset_dir + label + "/"
            for train_sample_id in split[0]:
                with open(label_dir+str(train_sample_id)+".txt", "r") as sample:
                    training_data.append("__label__"+label+" "+sample.readline()+"\n")
        temp_cv_training_set.writelines(training_data)

    with open("temp_cv_test_data.txt", "w") as temp_cv_training_set:
        test_data = []
        for label in per_class_results_cv.keys():
            label_dir = dataset_dir + label + "/"
            for test_sample_id in split[1]:
                with open(label_dir + str(test_sample_id) + ".txt", "r") as sample:
                    test_data.append("__label__" + label + " " + sample.readline() + "\n")
        temp_cv_training_set.writelines(test_data)

    model = fasttext.train_supervised("temp_cv_training_data.txt",
                                      epoch=500, lr=0.1)
    print(model.labels)
    print(model.words)

    per_class_results = model.test_label("temp_cv_test_data.txt")
    for fasttext_label in per_class_results.keys():
        label = fasttext_label[9:]
        # print(label, per_class_results[fasttext_label])
        per_class_results_cv[label]["precision_scores"].append(per_class_results[fasttext_label]["precision"])
        per_class_results_cv[label]["recall_scores"].append(per_class_results[fasttext_label]["recall"])
        per_class_results_cv[label]["f1_scores"].append(per_class_results[fasttext_label]["f1score"])

print(str(K)+"-fold Cross Validation Results:")
# Calculate overall results of K-fold CV as mean of the results of each run
for label in per_class_results_cv.keys():
    print("Situation:", label)
    print(" Precision:", np.mean(per_class_results_cv[label]["precision_scores"]))
    print(" Recall:", np.mean(per_class_results_cv[label]["recall_scores"]))
    print(" F1 score:", np.mean(per_class_results_cv[label]["f1_scores"]))
