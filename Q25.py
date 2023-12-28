def getDiscriminant(a, b, c):
  """
  計算並回傳判別式（a, b, c 為方程式的係數）
  """
  return b**2 - 4*a*c

def getRoot1(D, a, b):
  """
  計算並回傳第一個根（D為判別式）
  """
  return (-b + D**0.5) / (2*a)

def getRoot2(D, a, b):
  """
  計算並回傳第二個根（D為判別式）
  """
  return (-b - D**0.5) / (2*a)

def main():
  """
  主程式（程式進入點）
  """
  k = int(input())
  for _ in range(k):
    a = float(input())
    b = float(input())
    c = float(input())

    D = getDiscriminant(a, b, c)
    if D > 0:
      # 方程式有兩個實根
      root1 = getRoot1(D, a, b)
      root2 = getRoot2(D, a, b)
      print("{:.1f}".format(root1))
      print("{:.1f}".format(root2))
    elif D == 0:
      # 方程式有一個實根
      root = (-b) / (2*a)
      print("{:.1f}".format(root))

if __name__ == "__main__":
  main()
