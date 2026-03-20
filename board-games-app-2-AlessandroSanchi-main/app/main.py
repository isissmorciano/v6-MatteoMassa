from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repo, prodotto_repo

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)

@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    games: list[dict] = categoria_repo.get_all_categories()

    # 2. Passiamo la variabile 'games' al template
    return render_template("index.html", games=games)


@bp.route("/game/<int:id>")
def game_detail(id):

    game = categoria_repo.get_category_by_id(id)

    return render_template("game_detail.html", game=game)


@bp.route("/create", methods=("GET", "POST"))
def category_create():
        
    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["categoria"]
        error = None


        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            categoria_repo.create_category(nome)
            return redirect(url_for("main.index"))

        return render_template("game_create.html")




    return render_template("game_create.html")      

@bp.route("/game<int:id>/partite", methods=("GET", "POST"))
def get_partita(id):
    partita = prodotto_repo.get_prodotto_by_id(id)
    if partita is None:
        abort(404, f"Partita con id {id} non trovata.")
    return render_template("partita_detail.html", partita=partita)


@bp.route("/game<int:id>/partite/create", methods=("GET", "POST"))
def prodotto_create(category_id, nome, prezzo):
        
    if request.method == "POST":
    
        error = None
        category_id = id



        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            prodotto_repo.create_prodotto(category_id, nome, prezzo)
            return redirect(url_for("main.index"))

        return render_template("partita_create.html")
    return render_template("partita_create.html")