numbers = [1, "π", 2, "π₯", 3, "β­οΈ", 4, "π", 5, "π₯", 6, "β­οΈ", 7, "π", 8, "π₯", 9, "β­οΈ", 10, "π", 11, "π₯", 12, "β­οΈ", 13, "π", 14, "π₯", 15, "β­οΈ", 16]
result = 0

for number in numbers:
  if isinstance(number,int):
  #if type(number) == int:
    result += number

print(f"κ²°κ³Όκ°μ {result} μλλ€.")