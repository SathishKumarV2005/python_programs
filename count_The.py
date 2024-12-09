'''Problem #1
Read a passage.(you can hardcode a long passage).
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg: The king went to the forest with the wife and a servernt. The king shot a deer.The king went to the forest again the next day.


On a bright sunny morning, the birds chirped melodiously in the trees. A gentle breeze blew across the garden, carrying a sweet scent of blooming flowers.
In the corner of the yard, a small cat lounged lazily, soaking up the warmth of the sun.Nearby, a boy sat on a wooden bench, reading a book with a thoughtful expression.
It was truly the perfect start to a beautiful day.

answer is 4 (The king, the forest, The King the next).
'''

passage=input("Enter any Passage:")
count=0

sentence_list=passage.split(".")
words_list=[]
for s in sentence_list:
    words=s.split()
    for w in words:
        words_list.append(w)

result_list=[]

for w in words_list:
    if w.lower() == "the" or w.lower() == "a":
        result_list.append(w)


for r in range(0,len(result_list)-1):
    if result_list[r].lower() == "the" and result_list[r+1].lower() =="the":
        count+=1

print("count of 'The' followed by 'The' without 'a' in between them in  given passage is:",count)
