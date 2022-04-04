import requests

class alg:
    def algo(Service:str):
        Service = Service.upper()
        with requests.get("https://pastebin.com/raw/Bi6xFcCV") as checkLoad:# Google.com is where you need to replace the API link with
            checkLoad = checkLoad.text
            if "load" in checkLoad: return False
        match Service:
            case "PAYPAL":
                print (" Send API request with PAYPAL Script here. ")
            case "VENMO":
                print (" Send API Request with VENMMO script here. ")
            case _:
                print (" error, {x} not in array.".format(x=Service))