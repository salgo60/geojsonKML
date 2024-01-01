current status: most swedish protected areas are not on iNaturalist see official map [skyddadnatur.naturvardsverket.se](https://skyddadnatur.naturvardsverket.se/)

<img width="858" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/58b092e3-f8f5-4fea-898c-e0ee87c0c496">

* [map](https://w.wiki/8g$V) items with an id [P3613](https://www.wikidata.org/wiki/Property:P3613) = Naturvårdsregistret ID = identifier for an area protected see in swedish [Skyddad natur](https://www.naturvardsverket.se/amnesomraden/skyddad-natur/) - [map tool](https://skyddadnatur.naturvardsverket.se/)


* wikidata objects with [P3613](https://www.wikidata.org/wiki/Property:P3613) = **6599**
<img width="821" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/b95a7b36-fb55-42df-8826-0ef34670d5ea"> 

<img width="612" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/72541129-66b9-4b55-b423-f6055428c5e8"> 


 
# geojsonKML
Python code to convert geojson to KML that can be used on iNaturlist for nature reservate see converted files [salgo60/geojson/kml](https://github.com/salgo60/geojsonKML/tree/main/kml) >  5 530 files 
* format of files are  Naturvårdsregistret ID _ wikidata Qnummer _ name in english from wikidata .kml
* exemple created  files
   * [2000588_Q18292056_Lunnelid, Råda.kml](https://github.com/salgo60/geojsonKML/blob/main/kml/2000588_Q18292056_Lunnelid%2C%20R%C3%A5da.kml)
   * [2000001_Q30159379_Stommens ekäng.kml
](https://github.com/salgo60/geojsonKML/blob/main/kml/2000001_Q30159379_Stommens%20ek%C3%A4ng.kml) 
   * [2000154_Q10481121_Eldgarnsö Nature Reserve.kml](https://github.com/salgo60/geojsonKML/blob/main/kml/2000154_Q10481121_Eldgarns%C3%B6%20Nature%20Reserve.kml) 
   * ...

Exemple how a swedish nature reserve is represented  
* Östra Järvafältets nature reservat
  * [json](https://commons.wikimedia.org/wiki/Data:/Sweden/Nature_reserves/2020/%C3%96stra_J%C3%A4rvaf%C3%A4ltet/2002740.map)
  * iNaturalist [197743](https://www.inaturalist.org/observations?place_id=197743)
  * wikidata [Q30158554](https://www.wikidata.org/wiki/Q30158554) - graf
  * The swedish The Nature Conservation Register - Naturvårdsregistret [2002740](http://skyddadnatur.naturvardsverket.se/sknat/?nvrid=2002740)
  * Open street Map [10627921](https://www.openstreetmap.org/relation/10627921)
 
<img width="1351" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/0e15ed65-f2c6-4b1a-a212-33abc0ac90dc">

<img width="1351" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/0a55d911-1b2d-4595-a493-33c7a0ad5a76">

<img width="1254" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/cbde2fe3-c73e-4578-b5a2-f0831f1cdc74">
 
## SPARQL
* [Nature reserves in Stockholms county](https://w.wiki/8g9N) / [Sweden](https://w.wiki/8gFm)
   * [same with link commons geoshape](https://w.wiki/8gAn)
   * [same with Raw geojson link](https://w.wiki/8gBH)
* Wikidata objects with [P3613](https://www.wikidata.org/wiki/Property:P3613) but missing geoshape [P3896](https://www.wikidata.org/wiki/Property:P3896) - [sparql](https://w.wiki/8giM) = 61
* Wikidata has duplicates fir iNaturalist Place id [query sweden](https://w.wiki/8gmR)

# iNaturalist
* discussion iNatForum
   * [All swedish nature reserves as places available](https://forum.inaturalist.org/t/all-swedish-nature-reserves-as-places-available/47854/1) 

<img width="1030" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/8bd8b64e-45d7-4ea2-bb4f-b493201d465f">

   * [Creating iNaturalist places and linking to Wikidata using geojson](https://forum.inaturalist.org/t/creating-inaturalist-places-and-linking-to-wikidata-using-geojson/12220/3)
   * [Use Wikidata for place names and Wikipedia descriptions](https://forum.inaturalist.org/t/use-wikidata-for-place-names-and-wikipedia-descriptions/7702/1)
## Check iNaturalist for swedish nature reserves
 
* [Notebook](https://github.com/salgo60/geojsonKML/blob/main/notebook/Find%20iNaturalist%20places.ipynb) 

<img width="938" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/1b3d9065-1fc0-4bbe-91b8-00e36b7875ee">

### Wikidata <-> iNaturlist
* Sweden [SPARQL](https://w.wiki/8gW9) - wikidata nature reserves already connected with iNaturalist places

<img width="1075" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/ce6785fa-f930-4698-9da9-a40d7696c305">

### Misc
* [Best practise att hålla reda på förändringar med Naturvårdsreservat - 2018NV38321](https://phabricator.wikimedia.org/T205847)

 
#### Wikidata <-> Mix-and-match <-> iNaturalist places
 tool to match 

 * [mix-n-match.toolforge.org/#/catalog/3900](https://mix-n-match.toolforge.org/#/catalog/3900) 

<img width="1030" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/edfe3aaf-a41e-4f58-85f3-ce072ab2fd07">

<img width="1030" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/04e5d695-25d0-4c0c-81fc-7b69f59b0546"> 

* [mobile UI](https://mix-n-match.toolforge.org/mobile_game.html?catalog=3900)

 <img width="1215" alt="image" src="https://github.com/salgo60/geojsonKML/assets/14206509/f2cace46-855b-4605-a197-8be801abc3e0">
