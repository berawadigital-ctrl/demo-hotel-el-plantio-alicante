# Contenido de la demo El Plantio Golf Resort (Alicante) (es/ca/en/fr). Hechos de elplantio.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','ca':' Les imatges són il·lustracions i no mostren els apartaments reals.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.'}
H={'es':['Apartamento de 2 habitaciones','Apartamento de 3 habitaciones','Terrazas con vistas al golf'],'ca':['Apartament de 2 habitacions','Apartament de 3 habitacions','Terrasses amb vistes al golf'],'en':['Two-bedroom apartment','Three-bedroom apartment','Terraces overlooking the golf course'],'fr':['Appartement 2 chambres','Appartement 3 chambres','Terrasses avec vue sur le golf']}
RD={
'es':['Espacioso y luminoso, de 104,5 m², con cocina, salón, comedor, aire acondicionado, calefacción, TV de pantalla plana, caja fuerte, lavadora y secadora.','De 118,3 m², con el mismo equipamiento completo: cocina, salón, comedor, climatización, caja fuerte, lavadora y secadora.','Las terrazas de los apartamentos ofrecen vistas al campo de golf, entre palmeras y lagos.'],
'ca':['Espaiós i lluminós, de 104,5 m², amb cuina, saló, menjador, aire condicionat, calefacció, TV de pantalla plana, caixa forta, rentadora i assecadora.','De 118,3 m², amb el mateix equipament complet: cuina, saló, menjador, climatització, caixa forta, rentadora i assecadora.','Les terrasses dels apartaments ofereixen vistes al camp de golf, entre palmeres i llacs.'],
'en':['Spacious and bright, 104.5 m², with kitchen, living room, dining room, air conditioning, heating, flat-screen TV, safe, washing machine and dryer.','118.3 m², with the same full equipment: kitchen, living room, dining room, air conditioning, safe, washing machine and dryer.','The apartment terraces overlook the golf course, among palm trees and lakes.'],
'fr':['Spacieux et lumineux, de 104,5 m², avec cuisine, salon, salle à manger, climatisation, chauffage, TV écran plat, coffre-fort, lave-linge et sèche-linge.','De 118,3 m², avec le même équipement complet : cuisine, salon, salle à manger, climatisation, coffre-fort, lave-linge et sèche-linge.','Les terrasses des appartements donnent sur le parcours de golf, entre palmiers et lacs.']}
ART={
'hero':('hills',9701,['#e3eee6','#f0e9cf','#e9b96f','#9fc09a','#6f9c7d','#46705a']),
'intro':('waves',9702,['#24566a','#efc183','#f7e0b7','#347489','#24566a','#14394a']),
'r1':('columns',9711,['#edf1ee','#f6f8f6','#b9703a','#5c3a1e','#3a2412']),
'r2':('arches',9712,['#f1ebdf','#e2c08e','#be7438','#5c3a1e','#3a2412']),
'r3':('hills',9713,['#e6efe8','#f2ecd5','#efc17d','#a5c3a0','#79a184','#507a62']),
'g1':('waves',9721,['#20506a','#eebe80','#f6ddb3','#306f86','#20506a','#123547']),
'g2':('hills',9722,['#e1ece4','#eee7cd','#e7b76c','#9cbd97','#6c997a','#436d57']),
'g3':('skyline',9723,['#5c3a1e','#e4a463','#f5d49f','#1c4d5e','#174050','#0f2b36']),
'g4':('arches',9724,['#efe8db','#dfbc8a','#bb7135','#5c3a1e','#3a2412']),
'g5':('columns',9725,['#ebf0ec','#f5f7f5','#b66d37','#5c3a1e','#3a2412']),
'g6':('waves',9726,['#1c4a62','#ecbb7c','#f5daaf','#2c6a81','#1c4a62','#103142'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='El Plantío Golf Resort · Apartamentos junto al golf en Alicante',see_rooms='Ver apartamentos',hero_k='Alicante',hero_t='Apartamentos entre palmeras, lagos y golf',hero_s='Apartamentos de 2 y 3 habitaciones con terraza y vistas al campo, dos campos de golf y dos piscinas abiertas todo el año.',
 intro_t='Un resort con dos campos de golf',intro_p1='El Plantío dispone de un campo de 18 hoyos par 72 championship y otro de 9 hoyos par 27, en armonía con el medio ambiente.',
 intro_p2='Escuela de golf desde 1993, driving range de 350 metros, restaurante de cocina mediterránea y Casa Club, en la Antigua Carretera Alicante-Elche, km 3.',
 stats=['Golf 18 + 9 hoyos','2 piscinas todo el año','Parking cubierto','Escuela de golf'],nav_rooms='Apartamentos',rooms_t='Apartamentos',rooms_s='Apartamentos de 2 y 3 habitaciones con cocina completa, salón y comedor. Reservando en su web: parking cubierto gratuito y late checkout a las 14 h.',
 svcs=['2 piscinas exteriores con solárium','Gimnasio','Restaurante y Casa Club','Campo de golf de 18 hoyos y Par 3','Escuela de golf','Campo de fútbol','Ping pong, petanca y putting green','Salones para bodas y eventos'],
 loc_p='Antigua Carretera Alicante-Elche, km 3 · 03114 Alicante.',
 chips=['¿Cómo son los apartamentos?','¿Tiene piscina?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='El Plantío Golf Resort · Apartaments al costat del golf a Alacant',see_rooms='Veure apartaments',hero_k='Alacant',hero_t='Apartaments entre palmeres, llacs i golf',hero_s='Apartaments de 2 i 3 habitacions amb terrassa i vistes al camp, dos camps de golf i dues piscines obertes tot l\'any.',
 intro_t='Un resort amb dos camps de golf',intro_p1='El Plantío disposa d\'un camp de 18 forats par 72 championship i un altre de 9 forats par 27, en harmonia amb el medi ambient.',
 intro_p2='Escola de golf des del 1993, driving range de 350 metres, restaurant de cuina mediterrània i Casa Club, a l\'Antiga Carretera Alacant-Elx, km 3.',
 stats=['Golf 18 + 9 forats','2 piscines tot l\'any','Pàrquing cobert','Escola de golf'],nav_rooms='Apartaments',rooms_t='Apartaments',rooms_s='Apartaments de 2 i 3 habitacions amb cuina completa, saló i menjador. Reservant al seu web: pàrquing cobert gratuït i late checkout a les 14 h.',
 svcs=['2 piscines exteriors amb solàrium','Gimnàs','Restaurant i Casa Club','Camp de golf de 18 forats i Par 3','Escola de golf','Camp de futbol','Ping-pong, petanca i putting green','Salons per a casaments i esdeveniments'],
 loc_p='Antigua Carretera Alicante-Elche, km 3 · 03114 Alacant.',
 chips=['Com són els apartaments?','Té piscina?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='El Plantío Golf Resort · Golf apartments in Alicante',see_rooms='See the apartments',hero_k='Alicante',hero_t='Apartments among palm trees, lakes and golf',hero_s='Two- and three-bedroom apartments with terraces overlooking the course, two golf courses and two pools open all year round.',
 intro_t='A resort with two golf courses',intro_p1='El Plantío has an 18-hole par 72 championship course and a 9-hole par 27 course, in harmony with the environment.',
 intro_p2='Golf school since 1993, a 350-metre driving range, a Mediterranean restaurant and Club House, on the old Alicante-Elche road, km 3.',
 stats=['Golf 18 + 9 holes','2 pools all year','Covered parking','Golf school'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='Two- and three-bedroom apartments with full kitchen, living and dining room. Booking on its website: free covered parking and late checkout at 14:00.',
 svcs=['2 outdoor pools with sun terrace','Gym','Restaurant and Club House','18-hole golf course and Par 3','Golf school','Football pitch','Table tennis, pétanque and putting green','Rooms for weddings and events'],
 loc_p='Antigua Carretera Alicante-Elche, km 3 · 03114 Alicante.',
 chips=['What are the apartments like?','Is there a pool?','Is there parking?','How do I book?']),
'fr':dict(title='El Plantío Golf Resort · Appartements au bord du golf à Alicante',see_rooms='Voir les appartements',hero_k='Alicante',hero_t='Appartements entre palmiers, lacs et golf',hero_s='Appartements de 2 et 3 chambres avec terrasse et vue sur le parcours, deux parcours de golf et deux piscines ouvertes toute l\'année.',
 intro_t='Un resort avec deux parcours de golf',intro_p1='El Plantío dispose d\'un parcours de 18 trous par 72 championship et d\'un autre de 9 trous par 27, en harmonie avec l\'environnement.',
 intro_p2='École de golf depuis 1993, driving range de 350 mètres, restaurant de cuisine méditerranéenne et Club House, sur l\'ancienne route Alicante-Elche, km 3.',
 stats=['Golf 18 + 9 trous','2 piscines toute l\'année','Parking couvert','École de golf'],nav_rooms='Appartements',rooms_t='Appartements',rooms_s='Appartements de 2 et 3 chambres avec cuisine complète, salon et salle à manger. En réservant sur son site : parking couvert gratuit et départ tardif à 14h.',
 svcs=['2 piscines extérieures avec solarium','Salle de sport','Restaurant et Club House','Parcours de 18 trous et Par 3','École de golf','Terrain de football','Ping-pong, pétanque et putting green','Salles pour mariages et événements'],
 loc_p='Antigua Carretera Alicante-Elche, km 3 · 03114 Alicante.',
 chips=['Comment sont les appartements ?','Y a-t-il une piscine ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://plantiogolf.backhotelite.com/es/bookcore/availability/tomorrow/plantiogolf'; REN='https://plantiogolf.backhotelite.com/en/bookcore/availability/tomorrow/plantiogolf'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':REN})
D=dict(name='El Plantío Golf Resort',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Antigua Carretera Alicante-Elche, km 3 · 03114 Alicante',phones=['+34 965 115 049'],emails=['reservas@elplantio.com'],maps='El Plantío Golf Resort, Alicante',t=T)
META=dict(repo='demo-hotel-el-plantio-alicante',name='El Plantío Golf Resort',legal_name='Pay and Play, S.L.',registry_ids=['CIF B53479457','Registro Mercantil de Alicante, tomo 2340, folio 152, hoja A59344','Licencia turística AA-646'],
 url='https://www.elplantio.com/',domain='elplantio.com',municipality='Alicante',province='Alicante',sector='apartamentos turísticos en un resort de golf en Alicante',
 read_at='2026-10-29T15:01:00+01:00',created_at='2026-10-29T15:01:00+01:00',built_at='2026-10-29T15:10:00+01:00',audit_date='2026-10-29T15:00:31+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T12:16:29+01:00',url='https://www.google.com/maps/place/El+Plant%C3%ADo+Golf+Resort/@38.3096893,-0.5401117,17z/data=!4m9!3m8!1s0xd62350a85e21ea9:0x8d8b21185c3e0d30!5m2!4m1!1i2!8m2!3d38.3096893!4d-0.5401117!16s%2Fg%2F1v42h419'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del resort (plantiogolf.backhotelite.com, el mismo enlace de su boton RESERVA AHORA; version /en/ para ingles y frances); la demo no construye ningun motor.'),
 first_of_type='no aplica: apartamentos turisticos con precedente en demos anteriores')
QS={
'es':[('¿Cómo son los apartamentos?','K01'),('¿Qué tiene el apartamento de 3 habitaciones?','K02'),('¿Dónde está?','K03'),('¿Tiene piscina?','K04'),('¿Hay parking?','K05'),('¿Tiene restaurante?','K06'),('¿Hay campo de golf?','K07'),('¿Tienen escuela de golf?','K08'),('¿Hay gimnasio?','K09'),('¿Organizan bodas?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay un apartamento libre mañana','K11'),('¿Tienen spa?',None),('¿Admiten mascotas?',None)],
'ca':[('Com són els apartaments?','K01'),('Què té l\'apartament de 3 habitacions?','K02'),('On és?','K03'),('Té piscina?','K04'),('Hi ha pàrquing?','K05'),('Té restaurant?','K06'),('Hi ha camp de golf?','K07'),('Teniu escola de golf?','K08'),('Hi ha gimnàs?','K09'),('Organitzeu casaments?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha un apartament lliure demà','K11'),('Teniu spa?',None),('Admeteu mascotes?',None)],
'en':[('What are the apartments like?','K01'),('What does the three-bedroom apartment have?','K02'),('Where is it?','K03'),('Is there a pool?','K04'),('Is there parking?','K05'),('Is there a restaurant?','K06'),('Is there a golf course?','K07'),('Do you have a golf school?','K08'),('Is there a gym?','K09'),('Do you host weddings?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free apartment tomorrow','K11'),('Do you have a spa?',None),('Are pets allowed?',None)],
'fr':[('Comment sont les appartements ?','K01'),('Qu\'a l\'appartement de 3 chambres ?','K02'),('Où est-il ?','K03'),('Y a-t-il une piscine ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il un restaurant ?','K06'),('Y a-t-il un parcours de golf ?','K07'),('Avez-vous une école de golf ?','K08'),('Y a-t-il une salle de sport ?','K09'),('Organisez-vous des mariages ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a un appartement libre demain','K11'),('Avez-vous un spa ?',None),('Les animaux sont-ils admis ?',None)]}
