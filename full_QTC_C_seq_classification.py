import fasttext
model = fasttext.train_supervised("hf_expert_full_qtc_seqs_fasttext.txt", epoch=40, lr=.1)
print(model.labels)
print(model.words)


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


print_results(*model.test('hf_study_full_qtc_seqs_fasttext.txt'))
print(model.predict("--++ -+++ --++ ++++"))