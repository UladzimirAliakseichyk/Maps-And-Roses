from django.shortcuts import render
from services import create_map, get_from_pickle
from django.http import HttpRequest

def main(request):
    context = get_from_pickle()
    return render(request,'index.html',context=context)

def rose_map(request:HttpRequest):
    page_name = request.path
    rose_name = page_name.replace('/','')
    context = create_map(rose_name)

    return render(request,f'{rose_name}.html',context)