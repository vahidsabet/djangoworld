from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html', {'hi': 'dictionary'})


def count(request):
    fulltext = request.GET["fulltext"]
    words= fulltext.split()

    wordDictionary = {}

    for word in words:
        if word in wordDictionary:
            #inc
            wordDictionary[word] += 1
        else:
            #add to dic
            wordDictionary[word] = 1
    #sort desc
    sortedwords= sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fulltext': fulltext, 'count': len(words), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')