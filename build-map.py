import folium

# Create a map centered at a specific location
m = folium.Map(location=[56.33,44.00], zoom_start=5)

coordinates = [
    (0.5375,123.0625),
    (10.3,76.35),
    (10.5048,-66.9208),
    (10.8142,106.6438),
    (-10.8333,-61.9667),
    (-12.0433,-77.0283),
    (-12.5,18.5),
    (1.2929,103.8547),
    (12.9833,77.5833),
    (13.0843,80.2805),
    (1.3667,103.8),
    (13.75,100.4667),
    (13.7594,100.4889),
    (14.4336,120.4853),
    (14.5955,120.9721),
    (14.6313,-90.5277),
    (14.6644,121.0175),
    (14.9167,79.9833),
    (1.55,110.3333),
    (-15.597,-56.0958),
    (16.0685,108.2215),
    (16,106),
    (16.3,80.45),
    (-16.5002,-68.1493),
    (17.25,80.15),
    (17.3172,79.408),
    (17,-4),
    (17.4334,78.4111),
    (-17,-65),
    (17.7127,-91.6518),
    (-17.8,-63.1667),
    (18.2983,99.5072),
    (18.4615,-97.3928),
    (18.4657,-69.894),
    (18.5332,73.8626),
    (18.9721,72.8246),
    (19.0833,74.7333),
    (19.3308,-98.9427),
    (19.4342,-99.1386),
    (19.4371,-99.0111),
    (19.4501,-70.6998),
    (19.5667,74.2167),
    (19.7155,-101.2062),
    (-20.2833,57.55),
    (20.6668,-103.3926),
    (20,77),
    (20.8561,106.6822),
    (21.0313,105.8516),
    (21,57),
    (22.15,113.55),
    (22.1667,114.25),
    (22.25,114.1667),
    (22.2769,113.5678),
    (22.2909,114.15),
    (22.3167,114.2167),
    (22.3,73.2),
    (22.4,113.9833),
    (22.4333,87.3333),
    (22.5333,114.1333),
    (22.572,88.367),
    (2.2582,102.3555),
    (-22.7173,-42.0422),
    (-22.7592,-43.4319),
    (22.8167,70.8333),
    (-22.8305,-43.2192),
    (-22.8718,-47.2118),
    (-22.8876,-45.46),
    (-22.8951,-47.0439),
    (-22.9095,-47.0674),
    (22.9908,120.2133),
    (-23.0667,-52.4667),
    (23.0833,70.1333),
    (23.1167,113.25),
    (-23.4497,-49.7014),
    (23.5,121),
    (-23.5582,-46.9774),
    (-23.63,-46.6322),
    (23.7117,90.4463),
    (-23.7423,-46.8555),
    (23.771,90.3611),
    (23.7,90.375),
    (23.8,86.45),
    (-2.4358,-54.6887),
    (24.3644,88.6049),
    (24.4798,118.0819),
    (24,54),
    (24.6537,46.7152),
    (24.8065,120.9706),
    (25.0389,102.7183),
    (25.0478,121.5318),
    (2.5,112.5),
    (25,17),
    (25.2633,55.3087),
    (-25.5991,-54.5736),
    (26.1833,91.7333),
    (-26.2309,28.0583),
    (-26.8742,-49.1023),
    (-2,-77.5),
    (27.8833,78.0833),
    (28.0997,-15.4134),
    (28.1783,113.1117),
    (28.4333,77.3167),
    (28.4666,77.0309),
    (28.669,77.222),
    (28,84),
    (28.9684,50.8385),
    (-29,24),
    (29.5333,75.0167),
    (29.5569,106.5531),
    (29.6865,-95.4337),
    (-2.9764,104.75),
    (29.772,-95.3644),
    (29.8324,-95.472),
    (29.841,-82.6156),
    (30.0355,31.223),
    (30.1426,-81.5727),
    (30.1583,76.1931),
    (30.294,120.1619),
    (30.3229,78.0317),
    (30.5856,114.2665),
    (30.6667,104.0667),
    (30,70),
    (31.0449,121.4012),
    (31.3041,120.5954),
    (31.5322,75.9172),
    (31.6308,121.3925),
    (31.7736,119.954),
    (31.8639,117.2808),
    (32.0617,118.7778),
    (32.2499,34.9174),
    (32,35.25),
    (32.4907,119.9081),
    (32,-5),
    (32.5817,-97.1399),
    (32.6333,-16.9),
    (32.6572,51.6776),
    (32.9,115.8167),
    (33.0391,-97.0764),
    (-33.3667,-70.75),
    (-33.4378,-70.6503),
    (33,44),
    (33.4532,-112.0749),
    (33.455799999999996,126.5393),
    (-33.494,143.2104),
    (33.5446,-86.9292),
    (33.6013,-111.8867),
    (33.6975,73.0146),
    (33.7485,-84.3871),
    (33.7553,-84.3886),
    (-33.7608,150.9933),
    (34.0544,-118.244),
    (34.0549,-118.2578),
    (34.0584,-118.278),
    (-34.1708,-70.7444),
    (34.1919,135.1899),
    (3.4384,-76.5232),
    (34.5711,126.5989),
    (-34.6021,-58.3845),
    (-34.6033,-58.3817),
    (34.6679,-86.5603),
    (34.6836,113.5325),
    (34.7606,127.6621),
    (34.7725,113.7266),
    (34.8128,126.3918),
    (34,9),
    (-34.9314,-57.9489),
    (-35.0152,138.7364),
    (35.1003,129.0442),
    (35,105),
    (35.1762,136.9292),
    (35.1928,128.0847),
    (35.2719,128.8402),
    (35,38),
    (35.405,116.5814),
    (35.4297,139.6026),
    (35.4993,-80.8486),
    (35.5711,-5.3724),
    (35.6592,139.7057),
    (35.6882,139.7532),
    (35.69,139.69),
    (35.6961,51.4231),
    (35.7261,51.3304),
    (36.057,103.8399),
    (36.0986,120.3719),
    (36.1685,-115.1164),
    (36.6092,127.2919),
    (36.6167,101.7667),
    (36.6621,117.0104),
    (36.7256,3.0933),
    (36.7642,3.1468),
    (-3.7196,-38.5257),
    (37.2336,127.201),
    (37.2539,-122.0638),
    (37.2859,127.0099),
    (37.2974,-121.7562),
    (37.3388,-121.8914),
    (37.3417,-121.9753),
    (37.3424,126.9222),
    (37.4043,-122.0748),
    (37.4562,126.7288),
    (37.5112,126.97409999999999),
    (37.5333,121.4),
    (37.5517,-122.33),
    (37.5985,126.9783),
    (37.6405,127.2171),
    (37.6465,-84.7747),
    (37.7429,-0.954),
    (37.751,-97.822),
    (37.761,126.7727),
    (37.7751,-122.4193),
    (-37.8071,144.9516),
    (-37.8333,-58.25),
    (37.9842,23.7353),
    (38.4681,106.2731),
    (38.6583,-77.2481),
    (38.7048,-90.4617),
    (38.7095,-78.1539),
    (38.7174,-9.1321),
    (38.768,-121.3349),
    (39.3516,-76.629),
    (39.7277,-104.9815),
    (39.9288,116.3889),
    (39.9289,116.3883),
    (39.9914,-105.2392),
    (40.0574,-75.4017),
    (40.1817,44.5099),
    (40,45),
    (40.4856,-74.6265),
    (40.5511,-74.4606),
    (-40.5667,-73.15),
    (40.6443,-8.6455),
    (40.7157,-74),
    (40.7308,-73.9975),
    (40.7513,-73.8244),
    (40.7609,-73.9115),
    (40.793,-74.0247),
    (40.8106,111.6522),
    (40.8364,-74.1403),
    (40.8949,-74.011),
    (40.9069,-74.1209),
    (41.018,28.9745),
    (41.0214,28.9948),
    (41.1167,122.05),
    (41.1399,-104.8193),
    (41.3167,69.25),
    (41.6006,-93.6112),
    (41.6742,2.7904),
    (41,75),
    (41.7806,123.4312),
    (41.8483,-87.6517),
    (41.8904,12.5124),
    (42.3502,-3.6753),
    (42.509,-71.1984),
    (42.5418,-83.213),
    (42.6,-5.5703),
    (42.683,23.3175),
    (42.7,23.3333),
    (42.8864,-78.8781),
    (42.8864,-78.8784),
    (43.0334,-89.4512),
    (43.1479,12.1097),
    (43.35,-81.4833),
    (43.6319,-79.3716),
    (43.6655,-79.4204),
    (43.6833,24.8333),
    (43.6909,-79.3098),
    (43.801,87.6005),
    (43.88,125.3228),
    (44.8325,-0.6338),
    (44.9034,-93.374),
    (44.9528,-93.4372),
    (44.9572,34.1108),
    (45.0355,38.975),
    (45.1667,15.5),
    (45.3161,-73.8736),
    (45.4299,10.9844),
    (45.5063,-73.5794),
    (45.5397,-122.9638),
    (45.6,15.6),
    (45.6169,38.9453),
    (45.748,4.85),
    (4.5981,-74.0758),
    (46,105),
    (4.6114,101.1043),
    (46.4775,30.7326),
    (4.6493,-74.0617),
    (46.8147,-92.1998),
    (4.6985,103.3568),
    (47.0741,7.3065999999999995),
    (47.1449,8.1551),
    (47.2214,38.9094),
    (47.2833,-2.2),
    (47.6092,-122.3314),
    (47.6109,-122.3303),
    (48.5887,10.2058),
    (48,68),
    (48.7269,2.283),
    (48.8582,2.3387000000000002),
    (48.8607,2.3281),
    (49.294200000000004,8.345),
    (49.3667,7.6333),
    (49.405,11.1617),
    (49.8383,24.0232),
    (49.982,36.2566),
    (50.1155,8.6842),
    (50.4012,2.8625),
    (50.4333,30.5167),
    (50.45,30.5233),
    (50.4547,30.5238),
    (50.4924,2.9582),
    (50.6974,3.178),
    (50.9465,3.1227),
    (51.1564,-114.0566),
    (51.2637,6.5473),
    (51.2993,9.491),
    (51.3875,7.3928),
    (51.4964,-0.1224),
    (51.5088,-0.126),
    (51.5164,-0.093),
    (51.5353,-0.6658),
    (51.5406,46.0086),
    (51.5987,16.1677),
    (51.6592,39.2269),
    (52.0613,8.7341),
    (-5.2158,-41.5574),
    (52.2394,21.0362),
    (52.25,21),
    (52.2977,4.9562),
    (52.2978,104.2964),
    (52.352,4.9392),
    (52.3534,4.9087),
    (52.3552,4.8789),
    (52.3824,4.8995),
    (53.0167,158.65),
    (53,28),
    (53.9,27.5667),
    (54.3333,48.4),
    (54.6881,38.3292),
    (54.7065,20.511),
    (54.7889,56.0481),
    (-54.8,-68.3),
    (55.041,82.9428),
    (55.6125,11.7703),
    (55.7123,12.0564),
    (55.7386,37.6068),
    (55.7527,37.6172),
    (55.7666,49.1686),
    (56,24),
    (56.3283,44.0019),
    (58.753,17.0079),
    (58.9125,11.9253),
    (59.3247,18.056),
    (59.8981,30.2619),
    (59.95,10.75),
    (60.2797,15.9886),
    (6.0568,100.3876),
    (-6.1741,106.8296),
    (-6.175,106.8286),
    (6.2529,-75.5646),
    (7.1,100.4167),
    (-8.0102,-34.9503),
    (8,38),
    (8,-5),
    (8,-66),
    (9.1766,7.1751),
    (9,-80),
    (9.9295,-84.0884),
]

# Add markers for each geo coordinate
for coord in coordinates:
    #folium.Marker(location=[coord[0], coord[1]], popup="Marker").add_to(m)
    folium.Circle(radius=1000, 
                  fill_color="red",
                  fill_opacity=0.5,
                  color="#666",
                  weight=5,
                  popup=folium.Popup("127.0.0.1", parse_html=True, max_width=100),
                  location=[coord[0], coord[1]]).add_to(m)


# Save the map to an HTML file
m.save("map.html")