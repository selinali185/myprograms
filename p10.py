# anagram creator 

def anagram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0 
    while i < len(abc):
        current_letter = abc[i]
        text_lowered = text.lower()
        if current_letter in text_lowered:
            letter_count = text_lowered.count(current_letter)
            result = result + (current_letter*letter_count)
       # if abc[1] in text.lower():
        #    result += abc[i]*(text.lower().count(abc[i]))
        i += 1
    return result

()  ()
  . . 
  ___
   T 

   ___        ___
  /  \ \_____/ / \
  |               |
  |   __    __    |
  \      *       /
    \    /\     /
     \         /
     |        |             _____
    /          \           /   __|
   /            \         /   /
  /              \        |   |
  |               | \     /   /
  |      ___      |   \__/   /
  |     /    \    |    \_____/
  |    |     |    |    |
  |    |     |    |    | 
  /____\_____/_____\/__|   
  |____|     |_____| 

