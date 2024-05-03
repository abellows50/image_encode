#! /usr/bin/python3
import os
import random
try:
  import cv2
except:
  os.system("pip3 install opencv-python")
  import cv2
try:
  import sys
except:
  os.system("pip3 install sys")
  import sys

class CImage:
  #basic code
  code ={"\n":[0,8],"A":[0,9],"B":[1,0],"C":[1,1],"D":[1,2],"E":[1,3],"F":[1,4],"G":[1,5],"H":[1,6],"I":[1,7],"J":[1,8],"K":[1,9],"L":[2,0],"M":[2,1],"N":[2,2],"O":[2,3],"P":[2,4],"Q":[2,5],"R":[2,6],"S":[2,7],"T":[2,8],"U":[2,9],"V":[3,0],"W":[3,1],"X":[3,2],"Y":[3,3],"Z":[3,4],"0":[3,5],"1":[3,6],"2":[3,7],"3":[3,8],"4":[3,9],"5":[4,0],"6":[4,1],"7":[4,2],"8":[4,3],"9":[4,4]," ":[4,5],"!":[4,6],"@":[4,7],"#":[4,8],"$":[4,9],"%":[5,0],"^":[5,1],"&":[5,2],"*":[5,3],"(":[5,4],")":[5,5],"-":[5,6],"_":[5,7],"=":[5,8],"+":[5,9],"[":[6,0],"]":[6,1],"{":[6,2],"}":[6,3],";":[6,4],":":[6,5],"\'":[6,6],"\"":[6,7],",":[6,8],"<":[6,9],".":[7,0],">":[7,1],"/":[7,2],"?":[7,3],"\\":[7,4],"|":[7,5],"`":[7,6],"~":[7,7],"":[7,8],"stop":[9,9]}
  
  def __init__(self, image_path):
    self.img = cv2.imread(image_path)


  def textToCode(self,text):#basic encoding
    encoded = []
    for char in text:
      encoded.append(self.code[char])
    encoded.append(self.code["stop"])
    return encoded

  #switching the color of the pixel
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
  #setting the message
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

  #getting the letter from the code
  def getLetter(self,val):
    for key, value in self.code.items():
        if val == value:
            return key
  
    return "key doesn't exist"
  
  #getting the character from the pixel
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

class CryptImageBasic(CImage):
  pass

class CryptImageAdvanced(CImage):

  code = {
          "\n": [9, 9, 9], 
          "A": [0, 0, 1],
          "B": [0, 0, 2],
          "C": [0, 0, 3],
          "D": [0, 0, 4],
          "E": [0, 0, 5],
          "F": [0, 0, 6],
          "G": [0, 0, 7],
          "H": [0, 0, 8],
          "I": [0, 0, 9],
          "J": [0, 1, 0],
          "K": [0, 1, 1],
          "L": [0, 1, 2],
          "M": [0, 1, 3],
          "N": [0, 1, 4],
          "O": [0, 1, 5],
          "P": [0, 1, 6],
          "Q": [0, 1, 7],
          "R": [0, 1, 8],
          "S": [0, 1, 9],
          "T": [0, 2, 0],
          "U": [0, 2, 1],
          "V": [0, 2, 2],
          "W": [0, 2, 3],
          "X": [0, 2, 4],
          "Y": [0, 2, 5],
          "Z": [0, 2, 6],
          "0": [0, 2, 7],
          "1": [0, 2, 8],
          "2": [0, 2, 9],
          "3": [0, 3, 0],
          "4": [0, 3, 1],
          "5": [0, 3, 2],
          "6": [0, 3, 3],
          "7": [0, 3, 4],
          "8": [0, 3, 5],
          "9": [0, 3, 6],
          " ": [0, 3, 7],
          "!": [0, 3, 8],
          "@": [0, 3, 9],
          "#": [0, 4, 0],
          "$": [0, 4, 1],
          "%": [0, 4, 2],
          "^": [0, 4, 3],
          "&": [0, 4, 4],
          "*": [0, 4, 5],
          "(": [0, 4, 6],
          ")": [0, 4, 7],
          "-": [0, 4, 8],
          "_": [0, 4, 9],
          "=": [0, 5, 0],
          "+": [0, 5, 1],
          "[": [0, 5, 2],
          "]": [0, 5, 3],
          "{": [0, 5, 4],
          "}": [0, 5, 5],
          ";": [0, 5, 6],
          ":": [0, 5, 7],
          "'": [0, 5, 8],
          "\"": [0, 5, 9],
          ",": [0, 6, 0],
          "<": [0, 6, 1],
          ".": [0, 6, 2],
          ">": [0, 6, 3],
          "/": [0, 6, 4],
          "?": [0, 6, 5],
          "\\": [0, 6, 6],
          "|": [0, 6, 7],
          "`": [0, 6, 8],
          "~": [0, 6, 9],
          "": [0, 7, 0],
          "stop": [0, 7, 1]
        }
  def __init__(self, image_path):
    super().__init__(image_path)
    self.name = image_path.split(".")[0]
    self.coreImg = cv2.imread(image_path)

  def switchCol(self, pixel, change):
    for i in range(len(change)):
      pixel[i] = pixel[i] + change[i]
    return pixel
  
  def getChar(self, pixel, otherPixel):
    charVal = []
    for i in range(len(pixel)):
      charVal.append(abs(pixel[i] - otherPixel[i]))
    return self.getLetter(charVal)

  
  def decrypt(self, otherImgPath):
    otherImg = cv2.imread(otherImgPath)
    str = ""

    for r in range(len(self.img)):
      for p in range(len(self.img[r])):
        pixel = self.img[r][p]
        otherPixel = otherImg[r][p]
        char = ""
        if pixel[0] != otherPixel[0] or pixel[1] != otherPixel[1] or pixel[2] != otherPixel[2]:
          char = self.getChar(pixel,otherPixel)
          str+=char
        if char == "stop":
          return str
        
    return str
  
  def save(self, path, name):
    os.mkdir(path)
    cv2.imwrite(f"{path}/{name}1.png", self.img)
    cv2.imwrite(f"{path}/{name}2.png", self.coreImg)

class CryptImageAdvancedSalty(CryptImageAdvanced):
  def __init__(self, image_path, salt_max=10):
    super().__init__(image_path)
    self.salt = cv2.imread(image_path)

    for r in range(len(self.img)):
      for p in range(len(self.img[r])):
        self.salt[r][p] = [random.randint(0,salt_max),random.randint(0,salt_max),random.randint(0,salt_max)]
    
  def switchCol(self, pixel, change, salt):
    #pixel from the base image
    #change from the message
    #salt from the salt image
    # print(f"PIXEL{pixel}")
    # print(f"CHANGE:{change}")
    # print(f"SALT: {salt}")
    for i in range(len(change)):
        pixel[i] = (pixel[i] + change[i] + salt[i])  # Ensure result is within valid range
    # print(f"PIXEL+salt+change{pixel}")
    return pixel



  def getChar(self, pixel, otherPixel, saltPixel):
    #pixel from the image that is pixel+salt+change
    #otherPixel from the image that is pixel
    #saltPixel from the image that is salt
    # print(f"PIXEL+salt+change{pixel}")
    # print(f"Old Pixel:{otherPixel}")
    # print(f"SALT: {saltPixel}")
    charVal = []
    for i in range(len(pixel)):
        diff = pixel[i] - otherPixel[i] - saltPixel[i]
        # Ensure result is within valid range (0 to 255)
        charVal.append(max(0, min(diff, 255)))
    # print(f"Change: {pixel}")
    return self.getLetter(charVal)


  def encrypt(self):
    c = 0
    for r in range(len(self.img)):
      for p in range(len(self.img[r])):
        # print(f"Salt: {self.salt[r][p]}")
        self.img[r][p] = self.switchCol(self.img[r][p], self.encoded[c], self.salt[r][p])
        c+=1
        if c>len(self.encoded)-1:
          return
        
  def decrypt(self, otherImgPath, salt):
    otherImg = cv2.imread(otherImgPath)
    self.salt = cv2.imread(salt)
    
    str = ""

    for r in range(len(self.img)):
      for p in range(len(self.img[r])):
        pixel = self.img[r][p].astype(int)
        otherPixel = otherImg[r][p].astype(int)
        saltPixel = self.salt[r][p].astype(int)
        char = ""
        if pixel[0] != otherPixel[0] or pixel[1] != otherPixel[1] or pixel[2] != otherPixel[2]:
          char = self.getChar(pixel,otherPixel,saltPixel)
          str+=char
        if char == "stop":
          return str
        
    return str

  def save(self, path, name):
    # print(self.salt[0][0])
    try:
      os.mkdir(path)
    except:
      pass

    cv2.imwrite(f"{path}/{name}1.png", self.img)
    cv2.imwrite(f"{path}/{name}2.png", self.coreImg)
    cv2.imwrite(f"{path}/{name}3.png", self.salt)



def main():

  def getargs():
      msg = sys.argv[1]
      src = sys.argv[2]
      dest = sys.argv[3]

      return (msg, src, dest)
  
  if "-e" in sys.argv:
    sys.argv.remove("-e")
      
    if "-b" in sys.argv:
      sys.argv.remove("-b")
      msg, src, dest = getargs()
      encoder = CryptImageBasic(src)
      encoder.setMsg(msg)
      encoder.save(dest)

    if "-a" in sys.argv:
      # msg src_image)location dirName
      sys.argv.remove("-a")
      msg, src, dest = getargs()
      name = sys.argv[4]
      encoder = CryptImageAdvanced(src)
      encoder.setMsg(msg)
      encoder.save(dest, name)

    if "-salty" in sys.argv:
      sys.argv.remove("-salty")
      msg, src, dest = getargs()
      try:
        name = sys.argv[4]
      except:
        name = dest
        
      try:
        salt = int(sys.argv[5])
      except:
        salt = 10
      encoder = CryptImageAdvancedSalty(src, salt)
      encoder.setMsg(msg)
      encoder.save(dest, name)

    print(f"Saved Message in {dest}")
    
  elif "-d" in sys.argv:
      sys.argv.remove("-d")
      if "-b" in sys.argv:
        sys.argv.remove("-b")
        src = sys.argv[1]
        decoder = CryptImageBasic(src)
        msg = decoder.decrypt()
        print(msg)
      if "-a" in sys.argv:
        sys.argv.remove("-a")
        src = sys.argv[1]
        other = sys.argv[2]
        decoder = CryptImageAdvanced(src)
        msg = decoder.decrypt(other)
        print(msg)
      if "-salty" in sys.argv:
        sys.argv.remove("-salty")
        src = sys.argv[1]
        other = sys.argv[2]
        salt = sys.argv[3]
        decoder = CryptImageAdvancedSalty(src)
        msg = decoder.decrypt(other, salt)
        print(msg)


  else:
      print("You need a flag -e or -d")

      
if __name__ == "__main__":
  main()

  

