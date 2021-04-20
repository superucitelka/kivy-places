from classes.database import *

db = Database(dbtype='sqlite', dbname='../places.db')

#db = Database(dbtype='mysql', username='root', password='', dbname='places')

category = Category()
category.name = "vzdělávání"
db.create_category(category)

category = Category()
category.name = "kultura"
db.create_category(category)

category = Category()
category.name = "historie"
db.create_category(category)

category = Category()
category.name = "příroda"
db.create_category(category)

rows = [
   Place(
      name = "SŠPU Opava",
      description = "Budova opavské Střední školy průmyslové a umělecké je mnohem starší než instituce, která v ní sídlí od padesátých let dvacátého století. Byla vybudována Slezským zemským úřadem na sklonku šedesátých let devatenáctého století jako německé gymnázium s tradicí slavného humanistického a jezuitského učiliště, jež sídlilo v sousedství dnešního kostela sv. Vojtěcha na Dolním náměstí.",
      latitude = 49.937433,
      longitude = 17.9069078,
      category_id = 1,
      rate = 3.7,
      url = "https://www.sspu-opava.cz/",
      photos = [Photo(title="Hlavní budova školy", url="https://www.sspu-opava.cz/media/cms_page_media/80/skola1.jpg", type="barevná"),
                Photo(title="Tělocvična", url="https://www.sspu-opava.cz/media/cms_page_media/80/telocvicna.jpg", type="barevná"),
                ]
   ),
    Place(
        name="Slezské muzeum",
        description="Slezské zemské muzeum je pomyslnou branou do Slezska. Jeho zájem vychází od živé i neživé přírody přes prehistorii, historii až k dějinám umění, a to především v oblasti českého Slezska, severní a severovýchodní Moravy. Slezské zemské muzeum je příspěvkovou organizací Ministerstva kultury ČR. Je nejstarším veřejným muzeem na území dnešní České republiky, jeho historie sahá do roku 1814. Zároveň je se svými 2 400 000 sbírkovými předměty třetím největším muzeem v ČR.",
        latitude=49.9374949,
        longitude=17.9084434,
        category_id=3,
        rate=4.7,
        url="https://www.szm.cz/",
        photos=[Photo(title="Slezské muzeum: čelní pohled", url="https://www.opava-city.cz/images/gallery/tic/cz/mesto-opava/pamatky-zajimavosti/muzea-galerie/slezske-zemske-muzeum/u-muzea-03-p.jpg",
                      type="barevná"),
                Photo(title="Slezské muzeum: exponáty", url="https://www.infocesko.cz/Images/clanek/abstrakce_26/7080/52085zoom.jpg",
                      type="barevná"),
                ]
    ),
    Place(
        name="Ptačí vrch",
        description="Park na Ptačím vrchu v Opavě zdobí kinetické sochy ptáků od Kurta Gebauera. Sochám za šera svítí oči a dokáží otáčet hlavou. V parku se konají také promenádní koncerty a různé kulturní akce.",
        latitude=49.935475,
        longitude=17.903591,
        category_id=4,
        rate=4.6,
        url="https://www.szm.cz/",
        photos=[Photo(title="Opavský Ptáčák",
                      url="https://galerie.digiarena.zive.cz/data/516/ptacak2.jpg",
                      type="barevná"),
                Photo(title="Ptačí vrch: sochy",
                      url="https://foto.turistika.cz/foto/34385/69482/full_62c038_20001mismasstarychveci020.jpg",
                      type="barevná"),
                ]
    ),
    Place(
        name="Stříbrné jezero",
        description="Stříbrné jezero vzniklo na místě bývalého lomu, ve kterém se těžil sádrovec. Sádrovec se na Opavsku těží od roku 1849, v okolí Stříbrného jezera probíhala těžba až do začátku šedesátých let (více viz historie). Poté byl tento důl zatopen vodou. Plocha jezera je dnes přibližně 6,6 hektarů. Délka jezera je skoro 600 metrů, maximální šířka 200 metrů. Nadmořská výška vodní hladiny Stříbrného jezera je 250 m n.m., nejvýše položeným bodem v okolí je vrcholová plošina velké haldy severně od jezera (276 m n.m.). Největší hloubka v jezeře je přibližně 15 metrů.",
        latitude=49.9552537,
        longitude=17.8948503,
        category_id=4,
        rate=4.3,
        url="http://op4u.cz/old/old.opava-city.cz/scripts/detail82af.html?id=19695",
        photos=[Photo(title="Stříbrné jezero: letecký pohled",
                      url="http://op4u.cz/old/old.opava-city.cz/assets/zx/zivotni/s_-_ortofoto.jpg",
                      type="barevná"),
                Photo(title="Stříbrné jezero: pláž",
                      url="http://op4u.cz/old/old.opava-city.cz/assets/zx/zivotni/s_-_pohled_ze_zapadu.jpg",
                      type="barevná"),
                Photo(title="Stříbrné jezero: sádrovcová skalka",
                      url="http://op4u.cz/old/old.opava-city.cz/assets/zx/zivotni/s_-_sadrovcova_skalka.jpg",
                      type="barevná"),
                ]
    ),
    Place(
        name="Kostel svatého Vojtěcha",
        description="Dnešní barokní chrám sv. Vojtěcha na východní straně Dolního náměstí nahradil v druhé polovině 17. století původní gotický kostel. Nejstarší zmínka o kostelu sv. Vojtěcha existuje sice až z roku 1429, je však pravděpodobné, že vznikl někdy před rokem 1350. V období reformace v 16. století začalo být stále častěji užíváno pojmenování svatostánku jako kostela sv. Jiří. V kostele, který byl určen českému obyvatelstvu, již v roce 1532 působil luteránský duchovní. Po ukončení prvního dějství třicetileté války došlo i v Opavě k rekatolizačním omezením. Byli vypovězeni protestantští kněží a do města byl povolán jezuitský řád, kterému byl předán právě kostel sv. Jiří. Staviteli a zřejmě i autory jejich konečné architektonické podoby byli bratři italského původu Mikuláš a Jakub Braschové. Z doby výstavby nového kostela pocházel první mariánský sloup umístěný na Dolním náměstí před průčelím budovy.",
        latitude=49.939289,
        longitude=17.8947989,
        category_id=3,
        rate=4.6,
        url="https://cs.wikipedia.org/wiki/Kostel_svat%C3%A9ho_Vojt%C4%9Bcha_(Opava)",
        photos=[Photo(title="Kostel svatého Vojtěcha: jižní strana",
                      url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Kostel_sv._Vojt%C4%9Bcha_a_Zemsk%C3%BD_archiv.jpg",
                      type="barevná"),
                Photo(title="Kostel svatého Vojtěcha: průčelí",
                      url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Opava_%28Troppau%29_-_kostel_svat%C3%A9ho_Vojt%C4%9Bcha.jpg/1280px-Opava_%28Troppau%29_-_kostel_svat%C3%A9ho_Vojt%C4%9Bcha.jpg",
                      type="barevná"),
                Photo(title="Kostel svatého Vojtěcha: interiér",
                      url="https://1gr.cz/fotky/idnes/11/101/cl5/JOG3e3c67_kniha3.jpg.JPG",
                      type="barevná"),
                ]
    ),
    Place(
        name="Slezské divadlo",
        description="Slezské divadlo Opava patří k nejstarším v České republice. Původní německá scéna byla slavnostně otevřena 1. října 1805, čímž byla započata nepřetržitá existence divadla, které působí v Opavě více než dvě stě let.",
        latitude=49.939067,
        longitude=17.901189,
        category_id=2,
        rate=4.6,
        url="http://www.divadlo-opava.cz/",
        photos=[Photo(title="Slezské divadlo",
                      url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Slezske-divadlo-opava.jpg",
                      type="barevná"),
                Photo(title="Slezské divadlo (1993)",
                      url="https://cronobook.com/st/l/8f2b4ef8-3ae0-4f69-b02a-6f9a35b2462d.jpg",
                      type="černobílá"),
                ]
    ),
]

"""
place = Place()
place.name = "SŠPU Opava"
place.description = "Střední odborná škola"
place.category_id = 1

photo1 = Photo()
photo1.title = "Hlavní budova školy"
photo1.url = "https://www.sspu-opava.cz/media/cms_page_media/80/skola1.jpg"
db.create_photo(photo1)

photo2 = Photo()
photo2.title = "Tělocvična"
photo2.url = "https://www.sspu-opava.cz/media/cms_page_media/80/telocvicna.jpg"
db.create_photo(photo2)
"""
db.create_places(rows)
