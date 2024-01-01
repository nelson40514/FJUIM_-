def is_straight_flush(cards):
  """
  檢查手牌是不是同花順。

  Args:
    cards: 一手五張牌。

  Returns:
    如果手牌是同花順，則回傳 True，否則回傳 False。
  """

  # 檢查手牌是不是順子。
  if not is_straight(cards):
    return False

  # 檢查手牌是不是同花。
  if not is_flush(cards):
    return False

  # 手牌是同花順。
  return True


def is_four_of_a_kind(cards):
  """
  檢查手牌是不是鐵支。

  Args:
    cards: 一手五張牌。

  Returns:
    如果手牌是鐵支，則回傳 True，否則回傳 False。
  """

  # 計算每張牌出現的次數。
  counts = {}
  for card in cards:
    if card[1] not in counts:
      counts[card[1]] = 0
    counts[card[1]] += 1

  # 檢查是否有四張相同牌的牌。
  return any(count == 4 for count in counts.values())


def is_full_house(cards):
  """
  檢查手牌是不是葫蘆。

  Args:
    cards: 一手五張牌。

  Returns:
    如果手牌是葫蘆，則回傳 True，否則回傳 False。
  """

  # 計算每張牌出現的次數。
  counts = {}
  for card in cards:
    if card[1] not in counts:
      counts[card[1]] = 0
    counts[card[1]] += 1

  # 檢查是否有三張一張牌和兩張另一張牌。
  three_of_a_kind = False
  pair = False
  for count in counts.values():
    if count == 3:
      three_of_a_kind = True
    elif count == 2:
      pair = True

  # 手牌是葫蘆。
  return three_of_a_kind and pair


def is_straight(cards):
  """
  檢查手牌是不是順子。

  Args:
    cards: 一手五張牌。

  Returns:
    如果手牌是順子，則回傳 True，否則回傳 False。
  """

  # 將牌的文字轉為數字
  for card in cards:
    try:
      card[1] = int(card[1])
    except ValueError:
      if card[1] == 'A':
        card[1] = 1
      elif card[1] == 'J':
        card[1] = 11
      elif card[1] == 'Q':
        card[1] = 12
      elif card[1] == 'K':
        card[1] = 13

  # 根據牌的等級排序。
  cards.sort(key=lambda x: x[1])

  # 檢查手牌是不是輪轉順子。
  if cards[0][1] == 1 and cards[1][1] == 10 and cards[2][1] == 11 and cards[3][
      1] == 12 and cards[4][1] == 13:
    return True

  # 檢查手牌是不是普通順子。
  return all(cards[i][1] == cards[i + 1][1] for i in range(4))


def is_flush(cards):
  """
  檢查手牌是不是同花。

  Args:
    cards: 一手五張牌。

  Returns:
    如果手牌是同花，則回傳 True，否則回傳 False。
  """

  # 檢查手牌中的所有牌花色是否相同。
  suit = cards[0][0]
  return all(card[0] == suit for card in cards)


def classify_poker(cards):
  """
  將撲克牌分類。

  Args:
    cards: 一個包含五張撲克牌字串的列表。

  Returns:
    一個代表這副牌的分類的字串。
  """
  
  # 檢查輸入是否有效。
  if len(cards) != 5:
    return "Invalid"
  for i in range(len(cards)):
    card = cards[i]
    if len(card) > 3:
      return "Invalid"
    if card[0] not in "CDHS":
      return "Invalid"
    # 計算有沒有重複出現的牌
    for j in range(i+1,len(cards)):
      if cards[j] == card:
        return "Invalid"

  cards = [[card[0], card[1:]] for card in cards]
  # 檢查這些牌是否是同花順。
  if is_straight_flush(cards):
    return "Straight Flush"

  # 檢查這些牌是否是四條。
  if is_four_of_a_kind(cards):
    return "Four of a Kind"

  # 檢查這些牌是否為葫蘆。
  if is_full_house(cards):
    return "Full House"

  # 檢查這些牌是否是順子。
  if is_straight(cards):
    return "Straight"

  # 檢查這些牌是否是同花。
  if is_flush(cards):
    return "Flush"

  # 這些牌並不是特殊牌。
  return "Other"


def main():
  """
  從使用者取得輸入並分類撲克牌。
  """
  while True:
    cards = input()
    if cards == "0":
      break
    cards = cards.split()
    classification = classify_poker(cards)
    print(classification)


if __name__ == "__main__":
  main()
