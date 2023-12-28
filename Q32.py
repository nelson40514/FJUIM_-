def is_flush(cards):
  """
  判斷五張牌是否為同花。
  
  Args:
    cards: 五張牌，由空白隔開。
  
  Returns:
    如果五張牌是同花，返回True，否則返回False。
  """
  suits = [card[0] for card in cards]
  return len(set(suits)) == 1


def is_straight(cards):
  """
  判斷五張牌是否是順子。
  
  Args:
    cards: 五張牌，用空格分隔。
  
  Returns:
    True 如果五張牌是順子，否則 False。
  """
  values = []
  for card in cards:
    value = card[1:]
    if value == 'A':
      values.append(1)
    elif value == 'T':
      values.append(10)
    elif value == 'J':
      values.append(11)
    elif value == 'Q':
      values.append(12)
    elif value == 'K':
      values.append(13)
    else:
      values.append(int(value))
  values.sort()
  
  # 處理 10JQKA 兩個特殊情況
  if values == [10, 11, 12, 13, 1]:
    return True
  
  # 一般情況
  for i in range(1, len(values)):
    if values[i] - values[i - 1] != 1:
      return False
  return True


def main():
  """
  主函數。
  """
  # 讀取測資數量
  num_tests = int(input())

  # 處理測資
  for _ in range(num_tests):
    # 讀取五張牌
    cards = input().split()

    # 檢查輸入是否有效。
    if len(cards) != 5:
      print("Invalid")
      continue
    for card in cards:
      if len(card) > 3:
        print("Invalid")
        continue
      if card[0] not in "CDHS":
        print("Invalid")
        continue
        
    # 判斷五張牌是同花、順子還是其他
    if is_flush(cards):
      print("Flush")
    elif is_straight(cards):
      print("Straight")
    else:
      print("Other")


if __name__ == "__main__":
  main()
