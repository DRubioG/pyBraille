
class pyBraille():
    def __init__(self, black=chr(9679), white=chr(9675)):
       self.black=black
       self.white=white
       self.letras={'a': "200", 'b': "220", 'c' : "300", 'd' : "310", 'e' : "210", 'f' : "320",
        'g' : "330", 'h' : "230", 'i' : "120", 'j' : "130", 'k' : "202", 'l' : "222", 'm' : "302",
        'n' : "312", 'o' : "212", 'p' : "322", 'q' : "332", 'r' : "232", 's' : "122", 't' : "132",
        'u' : "203", 'v' : "223", 'x' : "303", 'y' : "313", 'z' : "213", 'á' : "233", 'é' : "123", 
        'í' : "102", 'ó' : "103", 'ú' : "133", 'ñ' : "331", 'w' : "131", 'ü' : "231", '&' : "313", 
        '.' : "001", ',' : "020", '¿' : "021", '?' : "021", '¡' : "032", '!' : "032", ';' : "022", 
        '"' : "023", '(' : "221", ')' : "112", '-' : "003", '*' : "012", '1': "200", '2' : "220", 
        '3' : "300", '4' : "310", '5' : "210", '6' : "320", '7' : "330", '8' : "230", '9' : "120", 
        '0' : "130", ' ' : "444", '|' : "101"}
       self.str=""
       
    def translate(self, text):
        for i in range(3):
            if i>0:
                self.str+="\n"
            for j in range(len(text)):  
                if text[j].isupper():
                    if i==0:
                        self.str=self.line1(self.str)
                    elif i==1:
                        self.str=self.line0(self.str)
                    elif i==2:
                        self.str=self.line1(self.str)

                if text[j].isnumeric():
                    if i==0:
                        self.str=self.line1(self.str)
                    elif i==1:
                        self.str=self.line1(self.str)
                    elif i==2:
                        self.str=self.line3(self.str)

                if self.letras[text[int(j)].lower()][i]=='0':
                    self.str=self.line0(self.str)
                elif self.letras[text[int(j)].lower()][i]=='1':
                    self.str=self.line1(self.str)
                elif self.letras[text[int(j)].lower()][i]=='2':
                    self.str=self.line2(self.str)
                elif self.letras[text[int(j)].lower()][i]=='3':
                    self.str=self.line3(self.str)
                elif self.letras[text[int(j)].lower()][i]=='4':
                    self.str=self.space(self.str)
        return self.str

    
    def line0(self, str):
        return str+self.white+' '+self.white+' '    #   ○ ○
    
    def line1(self, str):
        return str+self.white+' '+self.black+' '    #   ○ ●
    
    def line2(self, str):
        return str+self.black+' '+self.white+' '    #   ● ○
    
    def line3(self, str):
        return str+self.black+' '+self.black+' '    #   ● ●
    
    def space(self, str):
        return str+' '*3
    
    


if __name__=="__main__":
    a=pyBraille()
    
    print(a.translate("Ó"))