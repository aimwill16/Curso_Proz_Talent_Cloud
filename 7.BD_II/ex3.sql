DELIMITER //
CREATE PROCEDURE relatorio ()
BEGIN
	SELECT 
    	DATE(data_compra) AS datas,
        produto_id,
        SUM(quantidade) AS quantidade_total
    FROM vendas
END //
DELIMITER;
    