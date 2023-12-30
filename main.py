import os
import fiona
from fiona import collection
fiona.drvsupport.supported_drivers['kml'] = 'rw' # enable KML support which is disabled by default
fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default

# Ange sökvägar för in- och utkataloger
input_directory = 'in'
output_directory = 'kml'

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
