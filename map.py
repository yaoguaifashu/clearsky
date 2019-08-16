import folium
# from IPython.display import display

m = folium.Map(
    location=[34.7,135.2],
    # tiles='OpenStreetMap',
    tiles='Stamen Toner',
    zoom_start=13
)
folium.Marker([34.6937378, 135.5021651,], popup='Kansai').add_to(m)
m.save('osm.html')
