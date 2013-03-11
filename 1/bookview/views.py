# Create your views here.
from django.http import HttpResponse
from models import *

DOMAIN = 'psave'

KEY_BOOK = 'booknames'
KEY_COUNT = 'bookcounts'
KEY_URL = 'bookurls'

def listbook(request):
    data = 'path : ' + request.path
    data = data + '\n' + 'host : ' + request.get_host()
    data = data + '\n' + 'full_path : ' + request.get_full_path()
    data = data + '>>>>>>>>>>>>>>> :   '
    d = tryGetValue(request, 'd')
    if d:
        data = data + 'key : d & value : ' + d[1] 
    
    return HttpResponse('list = ' + data)

def tryGetValue(request, key):
    if key != None and key in request.GET and request.GET[key]:
        value = request.GET[key]
        
        return (key, value)
    
    return None
    
def tryGetSplitValue(request, key):
    if key != None and key in request.GET and request.GET[key]:
        value = request.GET[key]
        
        if value:
            return value.split(':')
    return None

def savetest(request):
    books = tryGetSplitValue(request, KEY_BOOK)
    if books == None:
        return HttpResponse('error for {0}'.format(KEY_BOOK))
    urls = tryGetSplitValue(request, KEY_URL)
    if urls == None:
        return HttpResponse('error for {0}'.format(KEY_URL))
        
    if len(books) != len(urls):
        return HttpResponse('error for count')
        
    bookDict = {}
    for i in range(0, len(books)):
        bookDict[books[i]] = urls[i]
       

    url = try_save_file(DOMAIN, 'save.txt', str(bookDict))
    return HttpResponse('save Url : ' + url)

def showsave(request):
    data = try_get_data(DOMAIN, 'save.txt')
    return HttpResponse('save data : ' + data)

