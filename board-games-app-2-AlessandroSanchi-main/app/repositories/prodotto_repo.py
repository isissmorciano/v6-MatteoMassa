from app.db import get_db

#1
def get_all_products():
    """Recupera tutti i giochi dalla tabella `giochi`.

    Restituisce una lista di dizionari con le colonne principali.
    """
    db = get_db()
    query = """
        SELECT id, nome
        FROM prodotti
        ORDER BY nome
    """
    games = db.execute(query).fetchall()
    return [dict(g) for g in games]

#2
def get_product_by_category(product_id):
    
    db = get_db()

    query = """
        SELECT id, nome
        FROM prodotti
        WHERE id = ?
    """

    game = db.execute(query,(product_id,)).fetchone()
    if game:
     return game
    else:

     return None






#3
def get_product_by_id(product_id):
    
    db = get_db()

    query = """
        SELECT product_id
        FROM prodotti
        WHERE gioco_id = ?
    """

    prodotto = db.execute(query,(product_id,)).fetchall()
    if prodotto:
     return prodotto
    else:

     return None
    
#numero 4
def create_product(category_id, nome, prezzo):
    """Crea una nuova partita."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO partite (category_id, nome, prezzo) VALUES (?, ?, ?)", (category_id, nome, prezzo)
    )
    db.commit()
    return cursor