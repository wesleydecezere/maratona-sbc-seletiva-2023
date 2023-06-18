import os

folder_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
file_name = "main.py"
test_file = "test.txt"
os.mkdir("problems")
os.chdir("problems")
# Create the folder
for f in folder_name:
  os.mkdir(f)
  os.chdir(f)
  # Create the file
  with open(file_name, "w") as file:
    file.write("# Your Python code goes here")
  os.chdir("..")
