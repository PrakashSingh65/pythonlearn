# Wrinte program to fill  in a letter template givenbelow with name and date

letter =''' Dear <|name|>,
You are selected !
<|Date|>'''

print(letter.replace("<|name|>","prakash").replace("<|Date|>","24 september 2026"))