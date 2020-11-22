from django.shortcuts import render
import requests, time, aiohttp, asyncio
from .utils import fetch
from django.http import JsonResponse

def home_view(request):
    start_time = time.time()
    data = []
    #https://swapi.dev/
    url_list = ['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']

    for url in url_list:
        data.append(requests.get(url).json())

    total = time.time() - start_time
    print('Total time:',total)

    context = {
        'people': data[0],
        'starships': data[1]
    }
    #Total time: 1.9625637531280518
    #2.5806353092193604
    return render(request, 'home.html',context)

async def home_view_async(request):
    #https://docs.aiohttp.org/en/stable/client_reference.html
    start_time = time.time()
    url_list = ['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']
    async with aiohttp.ClientSession() as client:
        tasks = []
        for url in url_list:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        total = time.time() - start_time
        print("Async Total Time: ", total)

        context = {
            'people': results[0],
            'starships': results[1]
        }
        #Async Total Time:  1.0391223430633545
    return render(request, 'home.html',context)
    #return JsonResponse(context)
