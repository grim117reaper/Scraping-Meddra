import os
import re
list = ["Blood and lymphatic system disorders","Cardiac disorders","Congenital, familial and genetic disorders","Ear and labyrinth disorders","Endocrine disorders","Eye disorders","Gastrointestinal disorders","General disorders and administration site conditions","Hepatobiliary disorders","Immune system disorders","Infections and infestations","Injury, poisoning and procedural complications","Investigations","Metabolism and nutrition disorders","Musculoskeletal and connective tissue disorders","Neoplasms benign, malignant and unspecified (incl cysts and polyps)","Nervous system disorders","Pregnancy, puerperium and perinatal conditions","Product issues","Psychiatric disorders","Renal and urinary disorders","Reproductive system and breast disorders","Respiratory, thoracic and mediastinal disorders","Skin and subcutaneous tissue disorders","Social circumstances","Surgical and medical procedures","Vascular disorders"]
for g in list:
    file = g + "_unformated.txt"
    file_open = open(file , 'r+')
    lines = file_open.readlines()
    q = lines[0].split()
    z = ''
    for i in q[1:]:
        z = z + " " + i
    p = "l0<" + z + ">\n"
    file = g + "_un.txt"
    files = open(file,'w+')
    files.write(p)
    written = 1
    len1 = len(lines)
    for i in range(1,len1   ):
        print("inside for")
        a = lines[i].split()
        if a:
            if a[0] == 'Spacer':
                b = lines[i+2].split()
                if b[0] == 'Spacer':
                    z = ''
                    for j in a[1:]:
                        z = z + " " + j
                    a1 = "l1<" + z + " >\n"
                    files.write(a1)
                    z = ''
                    for j in b[1:]:
                        z = z + " " + j
                    b1 = "l2<" + z + " >\n"
                    files.write(b1)
                    written = 0
                else:
                    if written ==1:
                        z = ''
                        for j in a[1:]:
                            z = z + " " + j
                        a2 = "l2<" + z + " >\n"
                        files.write(a2)
                    else:
                        written = 1
            else:
                files.write(lines[i])
