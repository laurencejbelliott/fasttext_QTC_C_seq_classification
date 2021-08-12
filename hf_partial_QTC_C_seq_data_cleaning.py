__author__ = "Laurence Roberts-Elliott"
import pickle

if __name__ == "__main__":
    # Load partial and complete experimenter QTC_C seqs
    with open("QTCC_HRSI_HMMs/from_bags/hf_expert_qtc_seqs.pickle", 'rb') as pickle_file:
        lab_seqs = pickle.load(pickle_file)

    unwanted_chars = ["'", ",", "[", "]"]
    u_seqs = []
    for u_seq in lab_seqs["ul"]:
        seq_str = str(u_seq)
        for char in unwanted_chars:
            seq_str = seq_str.replace(char, "")
        u_seqs.append("__label__u " + seq_str + "\n")
    for u_seq in lab_seqs["ur"]:
        seq_str = str(u_seq)
        for char in unwanted_chars:
            seq_str = seq_str.replace(char, "")
        u_seqs.append("__label__u " + seq_str + "\n")

    str_lab_seqs = {"u": u_seqs}
    for key in lab_seqs.keys():
        if key != "ul" and key != "ur":
            str_lab_seqs[key] = []
            for seq in lab_seqs[key]:
                seq_str = str(seq)
                for char in unwanted_chars:
                    seq_str = seq_str.replace(char, "")
                str_lab_seqs[key].append("__label__" + key + " " + seq_str + "\n")

    print(str_lab_seqs)

    with open("hf_expert_qtc_seqs_fasttext.txt", "w") as expert_qtc_seqs_file:
        for key in str_lab_seqs.keys():
            expert_qtc_seqs_file.writelines(str_lab_seqs[key])

    # Load partial and complete study QTC_C seqs
    with open("QTCC_HRSI_HMMs/from_bags/hf_study_qtc_seqs.pickle", 'rb') as pickle_file:
        lab_seqs = pickle.load(pickle_file)

    unwanted_chars = ["'", ",", "[", "]"]
    u_seqs = []
    for u_seq in lab_seqs["u"]:
        seq_str = str(u_seq)
        for char in unwanted_chars:
            seq_str = seq_str.replace(char, "")
        u_seqs.append("__label__u " + seq_str + "\n")

    str_lab_seqs = {"u": u_seqs}
    for key in lab_seqs.keys():
        if key != "ul" and key != "ur":
            str_lab_seqs[key] = []
            for seq in lab_seqs[key]:
                seq_str = str(seq)
                for char in unwanted_chars:
                    seq_str = seq_str.replace(char, "")
                str_lab_seqs[key].append("__label__" + key + " " + seq_str + "\n")

    print(str_lab_seqs)

    with open("hf_study_qtc_seqs_fasttext.txt", "w") as expert_qtc_seqs_file:
        for key in str_lab_seqs.keys():
            expert_qtc_seqs_file.writelines(str_lab_seqs[key])
