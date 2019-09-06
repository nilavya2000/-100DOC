import folium
import pandas
data = pandas.read_csv("v.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
ele = list(data["ELEV"])
def color(c):
    if c < 1000:
        return 'green'
    elif 1000<c<3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Stamen Terrain")

fgv = folium.FeatureGroup(name="volcanoes")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, nm, el in zip(lat, lon, name, ele):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(nm)+" "+str(el)+" m", fill_color = color(el), color = 'grey', fill_opacity = 0.7 ))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map2.html")
