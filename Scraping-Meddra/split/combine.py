import os
list = ["Blood and lymphatic system disorders","Cardiac disorders","Congenital, familial and genetic disorders","Ear and labyrinth disorders","Endocrine disorders","Eye disorders","Gastrointestinal disorders","General disorders and administration site conditions","Hepatobiliary disorders","Immune system disorders","Infections and infestations","Injury, poisoning and procedural complications","Investigations","Metabolism and nutrition disorders","Musculoskeletal and connective tissue disorders","Neoplasms benign, malignant and unspecified (incl cysts and polyps)","Nervous system disorders","Pregnancy, puerperium and perinatal conditions","Product issues","Psychiatric disorders","Renal and urinary disorders","Reproductive system and breast disorders","Respiratory, thoracic and mediastinal disorders","Skin and subcutaneous tissue disorders","Social circumstances","Surgical and medical procedures","Vascular disorders"]

file_output = "combined.xml"
file_write = open(file_output , 'w+')
f = "<root>\n"
file_write.write(f)
for i in list:
    file_name = i + ".xml"
    file = open(file_name , 'r+')
    lines = file.readlines()
    for z in lines:
        file_write.write(z)
    file.close()
f = "</root>\n"
file_write.write(f)
file_write.close()
