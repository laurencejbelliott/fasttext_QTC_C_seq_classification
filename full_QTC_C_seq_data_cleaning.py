__author__ = "Laurence Roberts-Elliott"
import pickle

if __name__ == "__main__":
    unwanted_chars = ["'", ",", "[", "]"]
    # Load partial and complete experimenter QTC_C seqs
    with open("controlled_lab_qtc_seqs.pickle", 'rb') as pickle_file:
        lab_seqs = pickle.load(pickle_file)


    # print(lab_seqs.keys())
    seqs = {"u": [], "pbl": [], "pbr": [], "pcl": [], "pcr": [], "rotl": [], "rotr": []}

    for key in lab_seqs.keys():
        class_label = key[0:4]
        print(class_label)
        if key[0] == "u":
            seqs["u"].append(lab_seqs[key])
        elif class_label == "pb_l":
            seqs["pbl"].append(lab_seqs[key])
        elif class_label == "pb_r":
            seqs["pbr"].append(lab_seqs[key])
        elif class_label == "pc_l":
            seqs["pcl"].append(lab_seqs[key])
        elif class_label == "pc_r":
            seqs["pcr"].append(lab_seqs[key])
        elif key.split("_")[1] == "rotl":
            seqs["rotl"].append(lab_seqs[key])
        elif key.split("_")[1] == "rotr":
            seqs["rotr"].append(lab_seqs[key])

    print(seqs)

    u_seqs = []
    for u_seq in seqs["u"]:
        seq_str = str(u_seq)
        for char in unwanted_chars:
            seq_str = seq_str.replace(char, "")
        u_seqs.append("__label__u " + seq_str + "\n")

    str_lab_seqs = {"u": u_seqs}
    for key in seqs.keys():
        if key != "u":
            str_lab_seqs[key] = []
            for seq in seqs[key]:
                seq_str = str(seq)
                for char in unwanted_chars:
                    seq_str = seq_str.replace(char, "")
                str_lab_seqs[key].append("__label__" + key + " " + seq_str + "\n")

    print(str_lab_seqs)

    with open("expert_full_qtc_seqs_fasttext.txt", "w") as expert_qtc_seqs_file:
        for key in str_lab_seqs.keys():
            expert_qtc_seqs_file.writelines(str_lab_seqs[key])


    # Load partial and complete study QTC_C seqs
    with open("study_qtc_seqs.pickle", 'rb') as pickle_file:
        lab_seqs = pickle.load(pickle_file)

    # print("Study QTC Seqs:", lab_seqs)
    # print(lab_seqs.keys())
    seqs = {"u": [], "pbl": [], "pbr": [], "pcl": [], "pcr": [], "rotl": [], "rotr": []}

    for key in lab_seqs.keys():
        class_label = key.split("_")[0]
        print(class_label)
        if key[0] == "u":
            seqs["u"].append(lab_seqs[key])
        elif class_label == "pbl":
            seqs["pbl"].append(lab_seqs[key])
        elif class_label == "pbr":
            seqs["pbr"].append(lab_seqs[key])
        elif class_label == "pcl":
            seqs["pcl"].append(lab_seqs[key])
        elif class_label == "pcr":
            seqs["pcr"].append(lab_seqs[key])
        elif class_label == "rotl":
            seqs["rotl"].append(lab_seqs[key])
        elif class_label == "rotr":
            seqs["rotr"].append(lab_seqs[key])

    print(seqs)

    u_seqs = []
    for u_seq in seqs["u"]:
        seq_str = str(u_seq)
        for char in unwanted_chars:
            seq_str = seq_str.replace(char, "")
        u_seqs.append("__label__u " + seq_str + "\n")

    str_lab_seqs = {"u": u_seqs}
    for key in seqs.keys():
        if key != "u":
            str_lab_seqs[key] = []
            for seq in seqs[key]:
                seq_str = str(seq)
                for char in unwanted_chars:
                    seq_str = seq_str.replace(char, "")
                str_lab_seqs[key].append("__label__" + key + " " + seq_str + "\n")

    print(str_lab_seqs)

    with open("study_full_qtc_seqs_fasttext.txt", "w") as expert_qtc_seqs_file:
        for key in str_lab_seqs.keys():
            expert_qtc_seqs_file.writelines(str_lab_seqs[key])

    # with open("QTCC_HRSI_HMMs/from_bags/hf_study_qtc_seqs.pickle", 'rb') as pickle_file:
    #     lab_seqs = pickle.load(pickle_file)
    #
    # unwanted_chars = ["'", ",", "[", "]"]
    # u_seqs = []
    # for u_seq in lab_seqs["u"]:
    #     seq_str = str(u_seq)
    #     for char in unwanted_chars:
    #         seq_str = seq_str.replace(char, "")
    #     u_seqs.append("__label__u " + seq_str + "\n")
    #
    # str_lab_seqs = {"u": u_seqs}
    # for key in lab_seqs.keys():
    #     if key != "ul" and key != "ur":
    #         str_lab_seqs[key] = []
    #         for seq in lab_seqs[key]:
    #             seq_str = str(seq)
    #             for char in unwanted_chars:
    #                 seq_str = seq_str.replace(char, "")
    #             str_lab_seqs[key].append("__label__" + key + " " + seq_str + "\n")
    #
    # print(str_lab_seqs)
    #
    # with open("hf_study_full_qtc_seqs_fasttext.txt", "w") as expert_qtc_seqs_file:
    #     for key in str_lab_seqs.keys():
    #         expert_qtc_seqs_file.writelines(str_lab_seqs[key])
