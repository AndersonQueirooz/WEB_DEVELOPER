CREATE TABLE IF NOT EXISTS tipo_acao
(
    codigo_acao INT AUTO_INCREMENT PRIMARY KEY,
    nome_acao VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS acao
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_acao INT,
    investimento DOUBLE,
    data_prevista DATE,
    data_cadastro DATE,
    FOREIGN KEY (codigo_acao) REFERENCES tipo_acao (codigo_acao)
);