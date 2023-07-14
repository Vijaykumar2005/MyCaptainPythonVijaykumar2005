frequency=input("Please enter a string:")
count = {}

for letter in frequency:
  if letter in count:
    count[letter] += 1
  else:
    count[letter] = 1

for key,value in count.items():
  print(f"{key}={value}")
