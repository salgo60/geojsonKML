# geojsonKML
Python code to convert geojson to KML that can be used on iNaturlist for nature reservate see converted files [salgo60/geojson/kml](https://github.com/salgo60/geojsonKML/tree/main/kml) 
* format of files are   <wikidata Qnummer>_<name in english from wikidata>.kml
* exemple created  files
   * [Q10510107_Grössjön.kml](https://github.com/salgo60/geojsonKML/blob/main/kml/Q10510107_Gr%C3%B6ssj%C3%B6n.kml)
   * [Q10532258_Högemon.kml](https://github.com/salgo60/geojsonKML/blob/main/kml/Q10532258_H%C3%B6gemon.kml)
   * [Q10593846_Nabbens naturreservat.kml](https://github.com/salgo60/geojsonKML/blob/main/kml/Q10593846_Nabbens%20naturreservat.kml)
   * ...

Exemple how a swedish nature reserve is represented  
* Östra Järvafältets nature reservat
  * [json](https://commons.wikimedia.org/wiki/Data:/Sweden/Nature_reserves/2020/%C3%96stra_J%C3%A4rvaf%C3%A4ltet/2002740.map)
  * iNaturalist [197743](https://www.inaturalist.org/observations?place_id=197743)
  * wikidata [Q30158554](https://www.wikidata.org/wiki/Q30158554)
  * The swedish The Nature Conservation Register - Naturvårdsregistret [2002740](http://skyddadnatur.naturvardsverket.se/sknat/?nvrid=2002740)
  * Open street Map [10627921](https://www.openstreetmap.org/relation/10627921)
 
## SPARQL
* [Nature reserves in Stockholms county](https://w.wiki/8g9N) / [Sweden](https://w.wiki/8gFm)
   * [same with link commons geoshape](https://w.wiki/8gAn)
   * [same with Raw geojson link](https://w.wiki/8gBH) 

# iNaturalist
* discussion iNatForum [Creating iNaturalist places and linking to Wikidata using geojson](https://forum.inaturalist.org/t/creating-inaturalist-places-and-linking-to-wikidata-using-geojson/12220/3)
## Check iNaturalist for swedish nature reserves
 
* [Notebook](https://github.com/salgo60/geojsonKML/blob/main/notebook/Find%20iNaturalist%20places.ipynb) 

<img width="938" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/1b3d9065-1fc0-4bbe-91b8-00e36b7875ee">

### Wikidata <-> iNaturlist
* Sweden [SPARQL](https://w.wiki/8gW9) - wikidata nature reserves already connected with iNaturalist

<img width="1075" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/ce6785fa-f930-4698-9da9-a40d7696c305">

* same [world on a map](https://w.wiki/8gWM)

 <img width="1352" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/6b2eb14d-767c-4646-af39-e60b9eba1969">
