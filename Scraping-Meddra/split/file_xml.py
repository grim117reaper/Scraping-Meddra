import os
import re
list = ["Blood and lymphatic system disorders","Cardiac disorders","Congenital, familial and genetic disorders","Ear and labyrinth disorders","Endocrine disorders","Eye disorders","Gastrointestinal disorders","General disorders and administration site conditions","Hepatobiliary disorders","Immune system disorders","Infections and infestations","Injury, poisoning and procedural complications","Investigations","Metabolism and nutrition disorders","Musculoskeletal and connective tissue disorders","Neoplasms benign, malignant and unspecified (incl cysts and polyps)","Nervous system disorders","Pregnancy, puerperium and perinatal conditions","Product issues","Psychiatric disorders","Renal and urinary disorders","Reproductive system and breast disorders","Respiratory, thoracic and mediastinal disorders","Skin and subcutaneous tissue disorders","Social circumstances","Surgical and medical procedures","Vascular disorders"]
for g in list:
    file = g + "_un.txt"
    file_open = open(file , 'r+')
    lines = file_open.readlines()
    file = g + "_unformat.txt"
    l0_last = ''
    l1_last = ''
    l2_last = ''
    l0 = 0
    l1 = 0
    l2 = 0
    files = open(file,'w+')
    for i in range(0,len(lines)):
        if l0 == 0:
            if "l0<" in lines[i]:
                l0 = 1
                t = lines[i].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l0_last = "l0</" + z +"\n"
        if l1 == 0:
            if "l1<" in lines[i]:
                l1 = 1
                t = lines[i].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l1_last = "l1</" + z +"\n"
        if l2 == 0:
            if "l2<" in lines[i]:
                l2 = 1
                t = lines[i].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l2_last = "l2</" + z +"\n"
        if l0 == 1 and l1 == 1 and l2 >= 1:
            if "l1<" in lines[i]:
                files.write(l2_last)
                files.write(l1_last)
                t = lines[i].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l1_last = "l1</" + z +"\n"
                t = lines[i+1].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l2_last = "l2</" + z +"\n"
                l2 = 2
            if "l2<" in lines[i] and l2 != 2:
                files.write(l2_last)
                t = lines[i].strip()
                z=''
                for j in t[3:]:
                    z = z + j
                l2_last = "l2</" + z +"\n"
            else:
                l2 = 3
        files.write(lines[i])
    files.write(l2_last)
    files.write(l1_last)
    files.write(l0_last)
    files.close()

for g in list:
    file = g + "_unformat.txt"
    file_out = g + ".txt"
    in_file = open(file,"r")
    out = open(file_out , "w+")
    in_lines = in_file.readlines()
    i = 0
    while (i != len(in_lines)):
        if "l1< " in in_lines[i]:
            out.write(in_lines[i])
            i = i+2
            continue
        else:
            out.write(in_lines[i])
            i = i + 1
    out.close()
