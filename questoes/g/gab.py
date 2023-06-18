def is_counting_community(document):
    numbers = []
    for line in document:
      line = line.replace(',', '').replace('.', '')
      words = line.split()
      print(words)
      for word in words:
        if "-" in word:
          word = word.replace("-","")
          print(word)
      if word.isalnum():      
            numbers.append(int(word))
    
    print(numbers)
    numbers.sort()
    for i in range(len(numbers) - 2):
        if numbers[i+1] == numbers[i] + 1 and numbers[i+2] == numbers[i] + 2:
            return True
    return False


# Read the input
n = int(input())
document = []
for _ in range(n):
    line = input().strip()
    document.append(line)

# Check if the document is from a counting community
if is_counting_community(document):
    print("123")
else:
    print(":)")
