CREATE DATABASE comunidade;
-- ----------------------------------------------------------------
USE comunidade;
-- ----------------------------------------------------------------
CREATE TABLE convivencias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    descricao VARCHAR(100),
    local VARCHAR(20)
);
