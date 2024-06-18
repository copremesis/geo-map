import folium
import random
import sys
from pprint import pprint


#from top_ips_dict import coordinates
from python_dict import coordinates

#invert the dictionary so we can now append ips to the popup
#this way we can have one dot to many ips
geo_dict = {}
for ip in coordinates:
    geo_coord = coordinates[ip]
    geo_dict[geo_coord] = [] if geo_coord not in geo_dict else geo_dict[geo_coord]
    geo_dict[geo_coord].append(ip)
#pprint(geo_dict)

#sys.exit()


#pick random location
#ip, coord = random.choice(list(coordinates.items()))

coord = coordinates[list(coordinates)[0]]
#focus on highest attacker
m = folium.Map(location=[coord[0],coord[1]], zoom_start=10)
#m = folium.Map(location=[0,60], zoom_start=1) #origin compare

folium.TileLayer('cartodbdark_matter').add_to(m)
#folium.TileLayer('cartodbpositron').add_to(m)

# Add markers for each geo coordinate with ip popups
popup_css='opacity: 0.8; background: #333; color: cyan; border-radius: 3px; cursor: pointer;'
color=random.choice(["red", "cyan", "chartreuse", "yellow"])
for coord in geo_dict:
    try:
      ul = ["<ul>"]
      for ip in geo_dict[coord]:
          html = f"""<li onclick="annotate(this, {coord[0]}, {coord[1]})"
                        class="ip-address"
                        style="{popup_css}">{ip}</li>"""
          ul.append(html)
      ul.append("</ul>")
      folium.Circle(radius=1000,
                    fill_color=color,
                    fill_opacity=0.3,
                    color="#FF4433",
                    weight=1,
                    popup="".join(ul),
                    location=[coord[0], coord[1]]).add_to(m)
    except Exception as err:
      pprint(coord)

#add sidebar css
m.get_root().header.add_child(folium.CssLink('css/style.css'))
m.get_root().html.add_child(folium.CssLink('css/leaflet.css')) #override with my changes to cached file
#so similar add the toolbelt
#which will be a read in file

f = open("templates/source-select.html", "r");
m.get_root().html.add_child(folium.Element(f.read()))

#add sidebar element to DOM
m.get_root().html.add_child(folium.Element("""
  <div id="sidebar">
    click on a map marker then click on an ip address in tooltip to obtain ISP, frquency & open ports
  </div>
  <div id="banner"></div>
"""))
#add javascript
m.get_root().html.add_child(folium.JavascriptLink('js/events.js'))
m.save("dist/map-with-popups.html")
