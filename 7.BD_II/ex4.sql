-- Criação da função
CREATE OR REPLACE FUNCTION contar_clientes_cadastrados(data_consulta DATE)
RETURNS INTEGER AS $$
DECLARE
    total_clientes INTEGER;
BEGIN
    -- Soma o número de clientes cadastrados na data especificada
    SELECT COUNT(*)
    INTO total_clientes
    FROM clientes
    WHERE DATE(data_cadastro) = data_consulta;

    -- Retorna o total de clientes cadastrados na data
    RETURN total_clientes;
END;
$$ LANGUAGE plpgsql;
