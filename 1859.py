class Solution:
  def sortSentence(self, s: str) -> str:
    dic = {} 
    for i in s.split(): 
        dic[i[-1]] = i[:-1] //숫자와 문자 분리해서 dict로 저장
dic[2] = 'is'
    final = [] 
    for num, word in sorted(dic.items()): 
        final.append(word) 
    return " ".join(final)
