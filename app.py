# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


from flask import Flask, render_template, request, redirect, url_for, json
app = Flask(__name__)

message = {

}
recepty = "data/recepty.json"

def save():
    with open(recepty, "w", encoding="UTF-8") as f:
        json.dump(message, f, indent=4)

def load():
    with open(recepty, "r", encoding="UTF-8") as f:
        return json.load(f)


@app.route("/")
def vitej():
    return render_template("vitej.html")

    


@app.route("/form", methods=['GET', 'POST'])

def form():
    
    # if request.method == 'POST'

    nvm = "nvm"
    login = request.args.get("login")
    recept = request.form.get("recept")
    
    if login == nvm:
        print("autor byl příliš líný na napsání receptu")

    if login and recept:
        save()
        return redirect(url_for(login = login, recept = recept))
        

    return render_template("form.html")

# cursor.execute("???")
# if request.method == "POST"



if __name__ == "__main__": #je název souboru je "__main__" , defaultně je právě tento název
    message = load()
    app.run(debug=True) # umožňuje vidět error kódu 