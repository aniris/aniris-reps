from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'home.html')
def result(request):
    sentence = request.GET['sentence']

    wordList = sentence.split()
# 단어마다 나눠짐
    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1 #워드 딕셔너리 있는곳이 1더함?
        else:
            wordDict[word] = 1 #처음 나오는 건 1로 초기화
    return render(request,'result.html',{'fulltext':sentence,'count':len(wordList),'wordDict':wordDict.items})