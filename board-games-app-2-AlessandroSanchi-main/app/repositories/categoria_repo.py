from app.db import get_db


def get_all_categories():
    """Recupera tutti i giochi dalla tabella `giochi`.

    Restituisce una lista di dizionari con le colonne principali.
    """
    db = get_db()
    query = """
        SELECT id, nome
        FROM categorie
        ORDER BY nome
    """
    games = db.execute(query).fetchall()
    return [dict(g) for g in games]

def get_category_by_id(category_id):
    
    db = get_db()

    query = """
        SELECT id, nome
        FROM categorie
        WHERE id = ?
    """

    game = db.execute(query,(category_id,)).fetchone()
    if game:
     return game
    else:

     return None
    


def create_category(nome):
    """Crea un nuovo canale."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categoria (nome) VALUES (?)", (nome)
    )
    db.commit()
    return cursor

def get_categories_stats():
   db= get_db()
   query= """
        SELECT nome
        COUNT(p.id),
        SUM(prezzo)
        
                   """
    
