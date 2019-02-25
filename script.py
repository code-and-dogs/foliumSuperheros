import folium

#create map object
#different tiles (map styles) can be used, like 'Stamen Toner', 'Stamen Terrain', ...
m = folium.Map(location=[46.961580, -102.560670], tiles='Mapbox Bright', zoom_start=4)

#create city markers and add them to map object
folium.Marker(location=[47.606209, -122.332069],popup='Seattle',icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[37.774929, -122.419418],popup='San Fransisco',icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[41.878113, -87.629799],popup='Chicago',icon=folium.Icon(color='red', icon='envelope')).add_to(m)

#create superhero icons from images
iconSpiderman = folium.features.CustomIcon('./images/spiderman.png', icon_size=(100,100))
iconHulk = folium.features.CustomIcon('./images/hulk.png', icon_size=(100,100))
iconWolverine = folium.features.CustomIcon('./images/wolverine.png', icon_size=(100,100))

#create superhero popup descriptions
popupSpiderman = "<strong>Spiderman</strong><br>Realname: Peter Parker<br>City of birth: Forest Hills, Queens, New York, USA"
popupHulk = "<strong>Hulk</strong><br>Realname: Bruce Banner<br>City of birth: Dayton, Ohio, USA"
popupWolverine = "<strong>Wolverine</strong><br>Realname: James Howlett (Logan)<br>City of birth: Cold Lake, Alberta, Canada"

#create superhero markers and add them to map object
folium.Marker([40.743720, -73.822030], tooltip="Spiderman", popup=popupSpiderman, icon=iconSpiderman).add_to(m)
folium.Marker([39.760979, -84.192200], tooltip="Hulk", popup=popupHulk, icon=iconHulk).add_to(m)
folium.Marker([54.464180, -110.182259], tooltip="Wolverine", popup=popupWolverine, icon=iconWolverine).add_to(m)

#generate map and save as local file
m.save('index.html')
