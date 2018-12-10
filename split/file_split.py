import os,sys
import re

list = ["Blood and lymphatic system disorders","Cardiac disorders","Congenital, familial and genetic disorders","Ear and labyrinth disorders","Endocrine disorders","Eye disorders","Gastrointestinal disorders","General disorders and administration site conditions","Hepatobiliary disorders","Immune system disorders","Infections and infestations","Injury, poisoning and procedural complications","Investigations","Metabolism and nutrition disorders","Musculoskeletal and connective tissue disorders","Neoplasms benign, malignant and unspecified (incl cysts and polyps)","Nervous system disorders","Pregnancy, puerperium and perinatal conditions","Product issues","Psychiatric disorders","Renal and urinary disorders","Reproductive system and breast disorders","Respiratory, thoracic and mediastinal disorders","Skin and subcutaneous tissue disorders","Social circumstances","Surgical and medical procedures","Vascular disorders"]

with open('tree.txt', 'r') as istr:
    for i in list:
        file_name = i + "_unformated.txt"
        with open(file_name,'w') as ostr:
            line1 = "Spacer " + i
            ostr.write(line1 + "\n")
            for line in istr:
                if "Vascular disorders" not in i:
                    if list[list.index(i)+1] in line:
                        ostr.close()
                        break
                else:
                    if "Venous valve ruptured" in line:
                        ostr.write(line)
                        break
                ostr.write(line)
for i in list:
    file_name = i +"_unformated.txt"
    file_foramted = i + ".txt"
    with open(file_name, 'r') as istr:
        with open(file_foramted, 'w') as ostr:
            for line in istr:
                a = re.findall(r'\w+', line)
                print (a)
                if a:
                    if (a[0] == "Spacer"):
                        line = line.rstrip('\n') + ' >\n'
                    else:
                        line = "\t" + line
                    ostr.write(line.replace( "Spacer", "<" ) )
                    ostr.write("\n")
