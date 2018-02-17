def enquete():
    moutarde =  "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    rose =      "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    pervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    leblanc =   "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

    code1 = "CATA"
    code2 = "ATGC"

    for suspect in [moutarde,rose,pervenche,leblanc]:
        print(position(code1,suspect))
        print(position(code2,suspect))

    return

# Execution de l'enquête
enquete()