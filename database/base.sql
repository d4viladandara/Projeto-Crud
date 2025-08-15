CREATE TABLE IF NOT EXISTS doces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    descricao TEXT
);

-- Inserindo alguns doces
INSERT INTO doces (nome, preco, descricao) VALUES
('Brigadeiro', 2.50, 'Doce de chocolate com granulado'),
('Beijinho', 2.50, 'Doce de coco com leite condensado'),
('Bolo de Cenoura', 5.00, 'Com cobertura de chocolate');
