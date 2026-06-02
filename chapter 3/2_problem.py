# Wrinte program to fill  in a letter template givenbelow with name and date

letter =''' Dear <|name|>,
            You are selected !
            <|Date|>'''

print(letter.replace("<|name|>","prakash").replace("<|date|" , "24 september 2050"))