import requests
import json
import pandas as pd
# URL of the GraphQL API
url = 'https://api.bezrealitky.cz/graphql/'

# Headers
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Your GraphQL query
query = """
query AdvertList($locale: Locale!, $estateType: [EstateType], $offerType: [OfferType], $disposition: [Disposition], $region: ID, $regionOsmIds: [ID], $limit: Int = 15, $offset: Int = 0, $order: ResultOrder = TIMEORDER_DESC, $petFriendly: Boolean, $balconyFrom: Float, $balconyTo: Float, $loggiaFrom: Float, $loggiaTo: Float, $terraceFrom: Float, $terraceTo: Float, $cellarFrom: Float, $cellarTo: Float, $parking: Boolean, $garage: Boolean, $newBuilding: Boolean, $lift: Boolean, $ownership: [Ownership], $construction: [Construction], $equipped: [Equipped], $priceFrom: Int, $priceTo: Int, $surfaceFrom: Int, $surfaceTo: Int, $advertId: [ID], $roommate: Boolean, $includeImports: Boolean, $boundaryPoints: [GPSPointInput], $discountedOnly: Boolean, $barrierFree: Boolean, $polygonBuffer: Int, $availableFrom: DateTime) {  listAdverts(    offerType: $offerType    estateType: $estateType    disposition: $disposition    limit: $limit    regionId: $region    regionOsmIds: $regionOsmIds    offset: $offset    order: $order    petFriendly: $petFriendly    balconySurfaceFrom: $balconyFrom    balconySurfaceTo: $balconyTo    loggiaSurfaceFrom: $loggiaFrom    loggiaSurfaceTo: $loggiaTo    terraceSurfaceFrom: $terraceFrom    terraceSurfaceTo: $terraceTo    cellarSurfaceFrom: $cellarFrom    cellarSurfaceTo: $cellarTo    parking: $parking    garage: $garage    newBuilding: $newBuilding    lift: $lift    ownership: $ownership    construction: $construction    equipped: $equipped    priceFrom: $priceFrom    priceTo: $priceTo    surfaceFrom: $surfaceFrom    surfaceTo: $surfaceTo    ids: $advertId    roommate: $roommate    includeImports: $includeImports    boundaryPoints: $boundaryPoints    discountedOnly: $discountedOnly    polygonBuffer: $polygonBuffer    barrierFree: $barrierFree    availableFrom: $availableFrom  ) {    list {      id      uri      estateType      offerType      disposition      imageAltText(locale: $locale)      mainImage {        id        url(filter: RECORD_THUMB)        __typename      }      address(locale: $locale)      surface      surfaceLand      tags(locale: $locale)      price      charges      currency      petFriendly      reserved      highlighted      roommate      project {        id        __typename      }      gps {        lat        lng        __typename      }      mortgageData(locale: $locale) {        rateLow        rateHigh        loan        years        __typename      }      originalPrice      isDiscounted      nemoreport {        id        status        timeCreated        __typename      }      isNew      videos {        id        previewUrl        status        __typename      }      links {        id        url        type        status        __typename      }      __typename    }    totalCount    __typename  }  actionList: listAdverts(    offerType: $offerType    estateType: $estateType    disposition: $disposition    regionId: $region    regionOsmIds: $regionOsmIds    offset: $offset    order: $order    petFriendly: $petFriendly    balconySurfaceFrom: $balconyFrom    balconySurfaceTo: $balconyTo    loggiaSurfaceFrom: $loggiaFrom    loggiaSurfaceTo: $loggiaTo    terraceSurfaceFrom: $terraceFrom    terraceSurfaceTo: $terraceTo    cellarSurfaceFrom: $cellarFrom    cellarSurfaceTo: $cellarTo    parking: $parking    garage: $garage    newBuilding: $newBuilding    lift: $lift    ownership: $ownership    construction: $construction    equipped: $equipped    priceFrom: $priceFrom    priceTo: $priceTo    surfaceFrom: $surfaceFrom    surfaceTo: $surfaceTo    ids: $advertId    roommate: $roommate    includeImports: $includeImports    boundaryPoints: $boundaryPoints    discountedOnly: true    limit: 3    availableFrom: $availableFrom  ) {    list {      id      uri      estateType      offerType      disposition      imageAltText(locale: $locale)      mainImage {        id        url(filter: RECORD_THUMB)        __typename      }      address(locale: $locale)      surface      surfaceLand      tags(locale: $locale)      price      charges      currency      petFriendly      reserved      highlighted      roommate      project {        id        __typename      }      gps {        lat        lng        __typename      }      mortgageData(locale: $locale) {        rateLow        rateHigh        loan        years        __typename      }      originalPrice      isDiscounted      nemoreport {        id        status        timeCreated        __typename      }      isNew      videos {        id        previewUrl        status        __typename      }      links {        id        url        type        status        __typename      }      __typename    }    totalCount    __typename  }}"""

# Your variables
variables = {
  "limit": 4000,
  "offset": 0,
  "order": "TIMEORDER_DESC",
  "locale": "CS",
  "offerType": ["PRONAJEM"],
  "estateType": ["BYT"],
  "priceTo": 25000,
  "regionOsmIds": ["R435541"],
  "roommate": False,
  "includeImports": False
}

# Sending the request
response = requests.post(url, json.dumps({'query': query, 'variables': variables}), headers=headers)

# Parsing the response
data = response.json()

# Printing the data
print(data)
adverts = data['data']['listAdverts']['list']

# Convert to pandas DataFrame
df = pd.json_normalize(adverts)
df.to_csv('prenajom_praha_bezrealitky1.csv')