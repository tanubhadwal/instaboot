import requests

from global_variable import ACCESS_TOKEN,BASE_URL

calamities = ['earthquake','landslide','volcanic_erruption','flood','tsunami','cyclone','storms','droughts']

# 31.0377824&lng=76.6900991

def natural_calamities():

  lat,long = raw_input("Enter Latitude and Longitude seperated by a space: ").split()

  url = "%s/locations/search?lat=%s&lng=%s&access_token=%s"%(BASE_URL,lat,long,ACCESS_TOKEN)

  response = requests.get(url).json()

  return response

def get_location_post():

  locations = natural_calamities()

  for location in locations['data']:

      if location['id'] == "0":

          pass

      else:

          url = "%s/locations/%s/media/recent?access_token=%s"%(BASE_URL,location['id'],ACCESS_TOKEN)

          response = requests.get(url).json()

          if len(response['data']):

              for posts in response['data']:

                  if posts['caption'] == None:

                      pass

                  else:

                      for calamity in calamities:

                            if calamity in posts['caption']['text']:

                                print "Post with id " + posts['id'] +" has \"" + calamity + "\" in caption."

          else:
            print "hello"
            pass

# get_location_post()562