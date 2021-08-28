import fasttext
model = fasttext.train_supervised("hf_expert_full_qtc_seqs_fasttext.txt", epoch=40, lr=.1)
print(model.labels)
print(model.words, "\n")

per_class_results = model.test_label('hf_study_full_qtc_seqs_fasttext.txt')
# print(per_class_results)
for label in per_class_results.keys():
    print(label, per_class_results[label])
# print_results(*model.test('hf_study_full_qtc_seqs_fasttext.txt'))

# with open("hf_study_full_qtc_seqs_fasttext.txt") as file:
#     for line in file.readlines():
#         true_label = line.split(" ")[0]
#
#         if true_label == "__label__pcr":
#             line = line.split(" ")[1:]
#             line[-1] = line[-1][:-1]
#             line = " ".join(line)
#             predicted_label = model.predict(line)[0][0]
#             print(line)
#             print("True label:", true_label, "Predicted label:", predicted_label)
#             print("Prediction is correct:", true_label == predicted_label)
#             print("")
