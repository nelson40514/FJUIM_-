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
  # 計算每張牌出現的次數。
  counts = {}
  for card in cards:
    if card[1:] not in counts:
      counts[card[1:]] = 0
    counts[card[1:]] += 1
  # 檢查是否有三張相同牌。
  if 3 in counts.values():
    return "Three of a Kind"
  # 檢查是否有兩對。
  if len(counts) == 3 and 2 in counts.values():
    return "Two Pair"
  # 檢查是否有對子。
  if len(counts) == 4 and 2 in counts.values():
    return "One Pair"
  # 否則，它就是其他。
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

