
import requests
import urllib

from global_variable import BASE_URL, ACCESS_TOKEN

calamities = ['earthquake','landslide','volcanic_erruption','flood','tsunami','cyclone','storms','droughts']

#lattitude,longtiude = 28.6303,77.2201

def natural_calamities():
    lattitude,longtiude = raw_input("Enter space separated lattitude and longitude : ").split()
    request_url=(BASE_URL+'/locations/search?lat=%s&lng=%s&access_token=%s' )%(lattitude,longtiude,ACCESS_TOKEN)
    print 'GET %s'%request_url
    location = requests.get(request_url).json()
    if location['meta']['code'] == 200:
        if len(location['data']):
            for x in range(0, len(location['data'])):
                id = location['data'][x]['id']
                print id
                request_url = (BASE_URL + '/locations/%s/media/recent?access_token=%s')%(id,ACCESS_TOKEN)
                media = requests.get(request_url).json()
                if media['meta']['code'] == 200:
                    if len(media['data']):
                        for x in range(0, len(media['data'])):
                            print media['data'][x]['tags']
                            print list(set(calamities) & set(media['data'][x]['tags']))
                            if len(list(set(calamities) & set(media['data'][x]['tags']))):
                                try:
                                    urllib.urlretrieve(media['data'][x]['images']['standard_resolution']['url'], media['data'][x]['id']+'.jpg')
                                except:
                                    print "Unable to Download"
                else:
                    print "HTTP CODE : Other than 200"
    else:
        print("HTTP CODE : Other than 200 (while retrieving location ids")

# if __name__ == "__main__":
#     natural_calamities()