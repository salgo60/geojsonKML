import os
import fiona
from fiona import collection
import requests

fiona.drvsupport.supported_drivers['kml'] = 'rw' # enable KML support which is disabled by default
fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default

import sys
# Ange sökvägar för in- och utkataloger
input_directory = 'in'
output_directory = 'kml'

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """#title: stockholm county nature reserve - geoshapeRaw
SELECT ?wd ?wdLabel ?inatPid ?inatP  ?geoshapeRaw    WHERE {
  ?wd wdt:P31 wd:Q179049;
    wdt:P131/wdt:P131 wd:Q104231.
  OPTIONAL {?wd wdt:P7471 ?inatPid}
  BIND(URI(CONCAT("https://www.inaturalist.org/places/",?inatPid)) as ?inatP)
  OPTIONAL {?wd wdt:P3896 ?geoshape}
  BIND(URI(CONCAT(REPLACE(REPLACE(str(?geoshape),"data/main/","w/index.php?title="),"\\\\+", "_"),"&action=raw")) AS ?geoshapeRaw)
 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,sv". }
}
ORDER BY (?wdLabel)"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def saveUrlToFile(filename  , url):
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"GeoJSON data successfully saved to {filename}")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def extractgeojsonFromWD():
    results = get_results(endpoint_url, query)
    for result in results["results"]["bindings"]:
        try:
            geojsonUrl = result["geoshapeRaw"]["value"]
            name = result["wdLabel"]["value"]
            filenameGeoJson = name + ".json"
            #print(name,geojsonUrl)
            saveUrlToFile(input_directory + "/" + filenameGeoJson,geojsonUrl)
        except Exception as e:
            print(f"An error occurred in SPARQL: {str(e)}")
    pass


extractgeojsonFromWD()

# Skapa katalogen för KML-filerna om den inte redan finns
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Lista alla GeoJSON-filer i indatamappen
geojson_files = [f for f in os.listdir(input_directory) if f.endswith('.json')]

print(geojson_files)
# Loopa igenom alla GeoJSON-filer och konvertera dem till KML
# Loopa igenom alla GeoJSON-filer och konvertera dem till KML
for file in geojson_files:
    input_file = os.path.join(input_directory, file)
    output_file = os.path.splitext(file)[0] + '.kml'
    output_file = os.path.join(output_directory, output_file)

    # Öppna GeoJSON-filen och konvertera till KML med fiona
    with collection(input_file, "r") as source:
        with collection(
                output_file, "w", "KML", source.schema.copy(), crs=source.crs
        ) as sink:
            for feature in source:
                sink.write(feature)


print("Konvertering klar.")
