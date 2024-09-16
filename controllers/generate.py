import math
import random

class Generate:
  def __init__(self, length):
    # パスワードの文字数
    # デスクトップ画面もしくはアプリケーションマスターから取得
    self.length = length
    # パスワード生成に使用する文字列
    self.num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    self.letter = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    self.capital = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    self.mark = ("@", "%", ":", "!", "-", "_")

  def generate(self):
    # 初期値
    i = 0
    password = ""

    while i < self.length:
      i += 1

      # 文字列をランダム生成
      param = math.ceil(random.random() * 4)
      if param == 1:
          password += self.num[math.floor(random.random() * len(self.num))]
      
      elif param == 2:
          password += self.letter[math.floor(random.random() * len(self.letter))]
      
      elif param == 3:
          password += self.capital[math.floor(random.random() * len(self.capital))]

      elif param == 4:
          password += self.mark[math.floor(random.random() * len(self.mark))]

    return password

  def generate_without_symbol(self):
    # 初期値
    i = 0
    password = ""

    while i < self.length:
      i += 1

      # 文字列をランダム生成
      param = math.ceil(random.random() * 3)
      if param == 1:
          password += self.num[math.floor(random.random() * len(self.num))]
      
      elif param == 2:
          password += self.letter[math.floor(random.random() * len(self.letter))]
      
      elif param == 3:
          password += self.capital[math.floor(random.random() * len(self.capital))]

    return password