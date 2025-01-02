import requests

def fetchs(name):
    url=f"https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query={name}"
    ans=requests.get(url)
    res=ans.json()
    if res['success'] :
        if "data" in res:
            print(res['data']['data'][0]["Name"])
            print(res['data']['data'][0]["CurrentPrice"])
            print(res['message']+"...")
            
    else:
        raise ValueError("could not find")
            


str=input("enter campany name")
fetchs(str)

