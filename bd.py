import sqlite3
import os

def conectar():
    conn = sqlite3.connect("score.db")
    return conn

def desconectar(conn):
  conn.close()
  
def criar_tabela(conn):
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS score_jogo (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      pontuacao INTEGER NOT NULL
    )
  """)
  conn.commit()

def inserir_dados(nome, pontuacao):
  conn = conectar()
  cursor = conn.cursor()
  cursor.execute("""
    INSERT INTO score_jogo (nome, pontuacao)
    VALUES (?, ?)
  """, (nome, pontuacao))
  conn.commit()
  desconectar(conn)

def listar_dados():
  conn = conectar()
  cursor = conn.cursor()
  cursor.execute("""
    SELECT * FROM score_jogo
    ORDER BY pontuacao DESC
  """)
  dados = cursor.fetchall()
  conn.commit()
  return dados