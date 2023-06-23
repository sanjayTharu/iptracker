from django.shortcuts import render
import requests
# Create your views here.

def iptracer(request):
    if request.method == 'POST':
        ip_address=request.POST['ip_address']
        results=get_ip_details(ip_address)
        return render(request,'iplogger/index.html',{'results':results})
    else:
        return render(request,'iplogger/index.html')
    
def get_ip_details(ip_address):
    url=f"http://ip_api.com/json/{ip_address}"
    response=requests.get(url)
    data=response.json()

    if data['status']=="fail":
        return "Failed to track IP address"
    
    country=data['country']
    city=data['city']
    zip_code=data['zip']
    latitude=data['lat']
    longitude=data['lon']

    result = f"IP Address: {ip_address}\n"
    result += f"Country:{country}"
    result += f"City : {city}"
    result += f"Zip code : {zip_code}"
    result += f"Latitude : {latitude}"
    result += f"Longitude : {longitude}"
    return result