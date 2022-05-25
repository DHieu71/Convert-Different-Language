from unidecode import unidecode
from string import ascii_lowercase
from googletrans import Translator
from ftfy import fix_encoding
t = Translator()

file1 = open('ensub.txt', 'r')
lines = file1.readlines()
for line in lines:
    line = line.strip()
f = open("vietsub.srt", "w", encoding= "utf-8-sig")
for line in lines:
    line = line.strip()
    if line == "":
        f.writelines('\n')
    elif line[0].lower() in ascii_lowercase:
        a = t.translate(line, src='en', dest='vi')
        m = str(a.text)
        f.writelines(fix_encoding(m)+'\n')
    else:
        f.writelines(line+ '\n')
    print(line)
f.close()
        
        
        
        # cach 2 k hay
        # t = Translator()
        # a = t.translate(line, src='en', dest='vi')
        # m = str(a.text.encode('utf-8'))
        # f.write(unidecode(a.text)+'\n')
