def solution(text: str) -> str:
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
    answer = 'z'
    count = 0
    text = text.lower()
    for letter in text:        
       if letter in letters:           
           if text.count(letter) > count or (text.count(letter) == count and letter < answer) :
               count = text.count(letter)
               answer = letter 
    return answer
