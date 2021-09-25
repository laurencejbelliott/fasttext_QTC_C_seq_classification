__author__ = "Laurence Roberts-Elliott"

sample_counts = {"u": 0, "pbl": 0, "pbr": 0, "pcl": 0, "pcr": 0, "rotl": 0, "rotr": 0}
with open("hf_study_qtc_seqs_fasttext.txt", "rb") as source_file:
    samples = source_file.readlines()
    for sample in samples:
        sample = str(sample).split(" ")
        label = sample[0][11:]
        sample = sample[1:]
        sample[-1] = sample[-1].replace("\\n'", "")
        sample = " ".join(sample)
        print(label)
        print(sample)
        with open("CV_dataset/"+label+"/"+str(sample_counts[label])+".txt", "w") as output_file:
            output_file.write(sample)
        sample_counts[label] += 1

with open("hf_expert_qtc_seqs_fasttext.txt", "rb") as source_file:
    samples = source_file.readlines()
    for sample in samples:
        sample = str(sample).split(" ")
        label = sample[0][11:]
        sample = sample[1:]
        sample[-1] = sample[-1].replace("\\n'", "")
        sample = " ".join(sample)
        print(label)
        print(sample)
        with open("CV_dataset/"+label+"/"+str(sample_counts[label])+".txt", "w") as output_file:
            output_file.write(sample)
        sample_counts[label] += 1

