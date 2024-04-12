from flask import Flask, render_template

app = Flask(__name__)

title = ('Fasteignahúsið',
         'Frábært úrval fasteigna',
         'Fasteignir á góðu verði',
         'Valin fasteign',
         'Vefsíðan finnst ekki')


menu = [
        ['/','Forsíða'], 
        ['/flokkur/einbyli','Einbýlishús'],
        ['/flokkur/radhus','Raðhús'],
        ['/flokkur/fjolbyli','Fjölbýlishús']
        ] #listi

hus =  [
        {
            "id": 0,
            "address": "Aðalstræti 1",
            "mynd": "hus0.PNG",
            "verd":160000000,
            "nanar":{"pnr":101, "lysing":"Falleg eign í hjarta Reykjavíkur"},
            "flokkur":"einbyli"
        },
        {
            "id": 1,
            "address": "Túngata 2",
            "mynd": "hus1.PNG",
            "verd":140000000,
            "nanar":{"pnr":450, "lysing":"Rólegur og fallegur staður við sjávarsíðuna"},
            "flokkur":"einbyli"
        },
        {
            "id": 2,
            "address": "Sigtún 3",
            "mynd": "hus2.PNG",
            "verd":145000000,
            "nanar":{"pnr":102, "lysing":"Fjölskylduvæn eign á góðum stað, nálægt allri þjónustu"},
            "flokkur":"einbyli"
        },
        {
            "id": 3,
            "address": "Skagabraut 3",
            "mynd": "hus3.PNG",
            "verd":65000000,
            "nanar":{"pnr":110, "lysing":"Fallegt og nýlega endurnýjað raðhús fyrir fólk á uppleið í lífinu"},
            "flokkur":"radhus"
        },
                {
            "id": 4,
            "address": "Háteigsgata 4",
            "mynd": "hus4.PNG",
            "verd":75000000,
            "nanar":{"pnr":200, "lysing":"Þeir segja að það sé gott að búa í Kópavogi..."},
            "flokkur":"radhus"
        },
        {
            "id": 5,
            "address": "Skagahlíð 55",
            "mynd": "hus5.PNG",
            "verd":30000000,
            "nanar":{"pnr":250, 
                     "lysing":"Lítil og falleg íbúð í glænýju fjölbýli á rótgrónum stað í sveitinni"},
            "flokkur":"fjolbyli"
        }
    ]

@app.route("/")
def index():
    return render_template("index.html", t=title, m=menu, h=hus)

@app.route("/ibud/<id>")
def ibud(id):
   valinibud = hus[int(id)] # route/id > ibud (id): vainibud = hus (id) listinn tekinn saman
   # > færibreytan v send í ibud.html 

   return render_template('ibud.html', m=menu, t=title, v=valinibud)

@app.route("/flokkur/<fl>")
def flokkur(fl): # f = fl -> f og h send í flokkur.html ásamt t og m
   return render_template("flokkur.html", m=menu, t=title, f=fl, h=hus)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("404.html", t=title, m=menu), 404

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  