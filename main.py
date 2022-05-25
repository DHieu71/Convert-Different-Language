from string import ascii_lowercase
from googletrans import Translator
from ftfy import fix_encoding
def main():
    # Creat client to connnect ggtrans
    Client = Translator()
    
    # Read file translate
    ReadFile = open('ensub.txt', 'r')
    Lines = ReadFile.readlines()
    
    # Write file need to translate
    WriteFile = open("vietsub.srt", "w", encoding= "utf-8-sig")
    
    for Line in Lines:
        Line = Line.strip()
        if Line == "":
            WriteFile.writelines('\n')
        elif Line[0].lower() in ascii_lowercase:
            InfoTrans = Client.translate(Line, src='en', dest='vi')
            Text = str(InfoTrans.text)
            WriteFile.writelines(fix_encoding(Text)+'\n')
        else:
            WriteFile.writelines(Line+ '\n')
        print(Line)
    WriteFile.close()
    
if __name__ == "__main__":
    main()
