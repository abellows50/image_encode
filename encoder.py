import cv2
import sys

class CryptImage:
  code ={"A":[0,9],"B":[1,0],"C":[1,1],"D":[1,2],"E":[1,3],"F":[1,4],"G":[1,5],"H":[1,6],"I":[1,7],"J":[1,8],"K":[1,9],"L":[2,0],"M":[2,1],"N":[2,2],"O":[2,3],"P":[2,4],"Q":[2,5],"R":[2,6],"S":[2,7],"T":[2,8],"U":[2,9],"V":[3,0],"W":[3,1],"X":[3,2],"Y":[3,3],"Z":[3,4],"0":[3,5],"1":[3,6],"2":[3,7],"3":[3,8],"4":[3,9],"5":[4,0],"6":[4,1],"7":[4,2],"8":[4,3],"9":[4,4]," ":[4,5],"!":[4,6],"@":[4,7],"#":[4,8],"$":[4,9],"%":[5,0],"^":[5,1],"&":[5,2],"*":[5,3],"(":[5,4],")":[5,5],"-":[5,6],"_":[5,7],"=":[5,8],"+":[5,9],"[":[6,0],"]":[6,1],"{":[6,2],"}":[6,3],";":[6,4],":":[6,5],"\'":[6,6],"\"":[6,7],",":[6,8],"<":[6,9],".":[7,0],">":[7,1],"/":[7,2],"?":[7,3],"\\":[7,4],"|":[7,5],"`":[7,6],"~":[7,7],"":[7,8],"stop":[9,9]}
  def __init__(self, image_path):

    self.img = cv2.imread(image_path)


  def textToCode(self,text):
    encoded = []
    for char in text:
      encoded.append(self.code[char])
    encoded.append(self.code["stop"])
    return encoded

  def switchCol(self, pixel, change):
    r = pixel[0]
    rmod = r%10
    r = r - rmod

    r = r + change[0]
    pixel[0] = r   

    g = pixel[1]
    gmod = g%10
    g = g - gmod

    g = g + change[1]
    pixel[1] = g

    return pixel

  def setMsg(self, msg):
    self.msg = msg.upper()
    self.encoded = self.textToCode(msg.upper())
    self.encrypt()

  def encrypt(self):
    c = 0
    for r in range(len(self.img)):
      for p in range(len(self.img[r])):
        self.img[r][p] = self.switchCol(self.img[r][p], self.encoded[c])
        c+=1
        if c>len(self.encoded)-1:
          return

  def getLetter(self,val):
    for key, value in self.code.items():
        if val == value:
            return key
  
    return "key doesn't exist"
  
  def getChar(self,pixel):
    r = pixel[0]
    rmod = r%10

    g = pixel[1]
    gmod = g%10

    char = self.getLetter([rmod,gmod])
    return char
    
  def decrypt(self):
    str = ""

    for row in self.img:
      for pixel in row:

        char = self.getChar(pixel)
        str+=char

        if char == "stop":
          return str
          
  def save(self, path):
    cv2.imwrite(path, self.img)

if "-e" in sys.argv:
    msg = sys.argv[1]
    src = sys.argv[2]
    dest = sys.argv[3]
    
    encoder = CryptImage(src)
    encoder.setMsg(msg)
    encoder.save(dest)
    
    print(f"Saved Message in {dest}")
    
elif "-d" in sys.argv:
    src = sys.argv[1]
    decoder = CryptImage(src)
    msg = decoder.decrypt()
    print(msg)

else:
    print("You need a flag -e or -d")

    


  

