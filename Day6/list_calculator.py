numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]
result = 0

for number in numbers:
  if isinstance(number,int):
  #if type(number) == int:
    result += number

print(f"결과값은 {result} 입니다.")