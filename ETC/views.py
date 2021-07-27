from django.http import HttpResponse
from django.shortcuts import render

def  index(request):
     return render(request,'index.html')

def check(request):
    val1=request.GET['flower']
    val2=request.GET['animal']
    val3=request.GET['sport']
    val4=request.GET['father']
    val5=request.GET['bird']
    
    count=0
    correct_ans=["Lotus","Tiger","Hockey","Peacock","Mahatma Gandhi",]
    ans=[val1,val2,val3,val4,val5,]
    var=len(ans)
    for i in range(var):
        if ans[i]==correct_ans[i]:
            count+=1

    return render(request,'result.html',{'count':count})

    