import os
import re
list = ["Blood and lymphatic system disorders","Cardiac disorders","Congenital, familial and genetic disorders","Ear and labyrinth disorders","Endocrine disorders","Eye disorders","Gastrointestinal disorders","General disorders and administration site conditions","Hepatobiliary disorders","Immune system disorders","Infections and infestations","Injury, poisoning and procedural complications","Investigations","Metabolism and nutrition disorders","Musculoskeletal and connective tissue disorders","Neoplasms benign, malignant and unspecified (incl cysts and polyps)","Nervous system disorders","Pregnancy, puerperium and perinatal conditions","Product issues","Psychiatric disorders","Renal and urinary disorders","Reproductive system and breast disorders","Respiratory, thoracic and mediastinal disorders","Skin and subcutaneous tissue disorders","Social circumstances","Surgical and medical procedures","Vascular disorders"]
l0=""
l1=""
l2=""
l0_split=""
l1_split=""
l2_split=""
z=""
l3=""
for g in list:
    file = g + ".txt"
    file_open = open(file , 'r+')
    w = g + ".xml"
    files = open(w , "w+")
    lines = file_open.readlines()
    for i in lines:
        z = i.split()
        if "l0<" in i or "l1<" in i or "l2<" in i or "l0</" in i or "l1</" in i or "l2</" in i:
            if "l0< " in i:
                for j in z[1:len(z)-1]:
                    l0_split = l0_split+" "+j
                l0 = "<level0 name =\""+l0_split+"\">\n"
                files.write(l0)
                l0_split=""
            if "l1< " in i:
                for j in z[1:len(z)-1]:
                    l1_split = l1_split+" "+j
                l1 = "<level1 name =\""+l1_split+"\">\n"
                files.write(l1)
                l1_split=""
            if "l2< " in i:
                for j in z[1:len(z)-1]:
                    l2_split = l2_split+" "+j
                l2 = "<level2 name =\""+l2_split+"\">\n"
                files.write(l2)
                l2_split=""
            if "l0</ " in i:
                files.write("</level0>\n")
            if "l1</ " in i:
                files.write("</level1>\n")
            if "l2</ " in i:
                files.write("</level2>\n")
        else:
            l3 = "<level3>\n"
            files.write(l3)
            files.write(i)
            l3 = "</level3>\n"
            files.write(l3)
    files.close()
    file_open.close()
os.system("rm *.txt")
