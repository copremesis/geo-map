import folium
import random

from top_ips_dict import coordinates

#invert the dictionary so we can now append ips to the popup
#this way we can have one dot to many ips
geo_dict = {}
for ip in coordinates:
    geo_coord = coordinates[ip]
    geo_dict[geo_coord] = [] if geo_coord not in geo_dict else geo_dict[geo_coord]
    geo_dict[geo_coord].append(ip)

#pick random location
ip, coord = random.choice(list(coordinates.items()))
m = folium.Map(location=[coord[0],coord[1]], zoom_start=10)

# Add markers for each geo coordinate with ip popups
popup_css='opacity: 0.8; background: #333; color: yellow; border-radius: 3px; cursor: pointer;'
for coord in geo_dict:
    ul = ["<ul>"]
    for ip in geo_dict[coord]:
        html = f"""<li onclick="annotate(this, {coord[0]}, {coord[1]})"
                      class="ip-address"
                      style="{popup_css}">{ip}</li>"""
        ul.append(html)
    ul.append("</ul>")
    folium.Circle(radius=1000,
                  fill_color="teal",
                  fill_opacity=0.5,
                  color="#666",
                  weight=5,
                  popup="".join(ul),
                  location=[coord[0], coord[1]]).add_to(m)

#add sidebar css
m.get_root().header.add_child(folium.CssLink('css/style.css'))
m.get_root().html.add_child(folium.CssLink('css/leaflet.css')) #override with my changes to cached file
#add sidebar element to DOM
m.get_root().html.add_child(folium.Element("""
  <div id="sidebar">
    click on a map marker then click on an ip address in tooltip to obtain ISP, frquency & open ports
  </div>
"""))
#add javascript
m.get_root().html.add_child(folium.JavascriptLink('js/events.js'))
m.save("dist/map-with-popups.html")
