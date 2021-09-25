import fasttext
model = fasttext.train_supervised("hf_expert_qtc_seqs_fasttext.txt",
                                  epoch=500, lr=0.1)
print(model.labels)
print(model.words)


per_class_results = model.test_label('hf_study_qtc_seqs_fasttext.txt')
for label in per_class_results.keys():
    print(label, per_class_results[label])

# def print_results(N, p, r):
#     print("N\t" + str(N))
#     print("P@{}\t{:.3f}".format(1, p))
#     print("R@{}\t{:.3f}".format(1, r))

# print(model.test_label('hf_study_qtc_seqs_fasttext.txt'))
# # print_results(*model.test('hf_study_qtc_seqs_fasttext.txt'))
# print(model.predict("--++ -+++ --++ ++++"))
