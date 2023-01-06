-- 1
/*DESAFIOA  2
 equipe de marketing precisa fazer uma pesquisa sobre nomes mais comuns de seus clientes, 
e precisa do nome e sobrenome dos clientes que estao cadastrados no sistema
SELECT DISTINCT --- elemina nomes duplicados
Quantos sobrenomes unicos temos em nossa tabela person.person?
/* 

 #WHERE
 SELECT *
 FROM person.person;
 WHERE Lastname = 'Miller' and Firstname = 'Anna'

#Busca todas as cores menos o vermelho
 WHERE color <> 'red' 

 #Busca por valores, ira mostrar valores entre 1500 e 3000 apenas 
 WHERE ListPrice > 1500 and ListPrice < 3000

 -- QUESTAO 1
 /*A eqeuipe de produção de produtos precisa do nome de todas as peças que pesam mais de 500kg
 mas não mais que 700kg para a inspeção
 -- weight

-- QUESTAO 2
 Foi pedido pelo marketing uma relação de todos os empregados  (employees)
 e quem são casados (single=solteiro, married=casados) e são asalariados (salaried)

  -- QUESTAO 1
 /*A eqeuipe de produção de produtos precisa do nome de todas as peças que pesam mais de 500kg
 mas não mais que 700kg para a inspeção
 -- weight
*/

SELECT Name
FROM Production.Product
WHERE Weight > 500 and  Weight <= 700 

--QUESTAO 2
 /*Foi pedido pelo marketing uma relação de todos os empregados  (employees)
 e quem são casados (single=solteiro, married=casados) e são asalariados (salaried)*/

-- desafio 3
SELECT *
FROM person.person
WHERE FirstName = 'Peter' and LastName = 'Krebs'

-- ORDER BY, ordem crescer ou decrescente
 SELECT *
 FROM Person.Person
 ORDER BY FirstName asc

 -- DESAFIO 1
 /* Obter o ProductID dos 10 produtos mais caros no sistema , listando do mais caro para o mais barato
 dicas: - Você terá que usar a tabela Product.product
 - Você tera que usar o ORDER BY e TOP
 - E para ordenar tera que usar o ORDER BY ASC ou DESC dependendo do resultado que esta buscando
*/

SELECT TOP 10 ProductID
FROM Production.product
ORDER BY ListPrice desc 

SELECT TOP 4 name, ProductNumber
FROM Production.product
ORDER BY ProductID asc

