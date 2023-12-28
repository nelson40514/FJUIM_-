def compare_password(correct_password, guess_password):
  """
  比較密碼，回傳正確字元數和位置正確字元數。

  Args:
      correct_password: 正確的密碼。
      guess_password: 猜測的密碼。

  Returns:
      一個元組，包含正確字元數和位置正確字元數。
  """
  correct_count = 0
  correct_position_count = 0
  for i in range(4):
      if guess_password[i] == correct_password[i]:
          correct_position_count += 1
          correct_password[i] = ''
      elif guess_password[i] in correct_password:
          correct_count += 1
          correct_password[correct_password.index(guess_password[i])] = ''
  return correct_count, correct_position_count


def main():
  """
  主函數。
  """
  correct_password = input()
  while True:
      guess_password = input()
      if guess_password == "-1":
          break
      correct_count, correct_position_count = compare_password(correct_password.split(), guess_password.split())
      print("{}A{}B".format(correct_position_count, correct_count))


if __name__ == "__main__":
  main()
