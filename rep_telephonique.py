from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def menu():
    """renvoie la page html du menu"""
    return render_template("menu.html")


@app.route('/ajout_num', methods=["get","post"])
def ajout_num():
    """renvoie la page html d'ajout de nom et garde en mémoire le contact ajouté"""
    if request.method== "POST":
        x= request.form["nom"]
        y= request.form["numtel"]
        with open('repertoire.txt','a') as f : #ouvre le document txt contenant les contacts déjà ajoutés
            f.write(x)
            f.write("\n")
            f.write(y)
            f.write("\n")
            f.write("\n")
            #écriture du contact dans le fichier texte
        #print("nom:", nom, "numtel:", numtel)

        return render_template("ajout_num_fait.html", numtel=y, nom=x)

    else:
        return render_template("ajout_num.html")


@app.route('/recherche_num', methods=['GET', 'POST'])
def recherche_num():
    """renvoie la page html de la recherche de numéro et garde en mémoir le nom à chercher ainsi que son numéro associé"""
    if request.method== "POST":
        z= request.form["nomrecherche"]
        repertoire=[] #création d'un tableau contenant les contacts
        with open('repertoire.txt','r') as f :
            for ligne in f:
                ligne=ligne.replace("\n","")
                repertoire.append(ligne)
        nblignes=len(repertoire)
        i=0
        while i !=nblignes : #parcourt le tableau afin de trouver le contact reccherché
            j=repertoire[i]
            if j ==z :
                numtrouve=repertoire[i+1] #le numéro associé au contact se trouve après celui-ci
                #return render_template("recherche_num_oui.html", nomrecheche=z,numtrouve=numtrouve,repertoire=repertoire,nblignes=nblignes)
                return render_template("recherche_num_oui.html", nomrecheche=z,numtrouve=numtrouve)

            else :
                i=i+1
        return render_template("recherche_num_non.html", nomrecheche=z)
    else:
        return render_template("recherche_num.html")


app.run(debug=True)
