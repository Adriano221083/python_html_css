DROP TABLE IF EXISTS entradas;
CREATE TABLE entradas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo string NOT NULL,
    texto string NOT NULL,
    criado_em DATETIME DEFAULT NOW
);