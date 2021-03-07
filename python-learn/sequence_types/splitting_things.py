panagram = """The quick brown 
fox jumps\t over 
the lazy dog"""

print(panagram)
words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ["9", " ",
                  "2", "2", "3", " ",
                  "3", "7", "2", " ",
                  "0", "3", "6", " ",
                  "8", "5", "4", " ",
                  "7", "7", "5", " ",
                  "8", "0", "7",
                  ]
values_list = "".join(generated_list)
print(values_list)