/*Usando os conceitos aprendidos nesse módulo, e sem alterar o arquivo index.html, adicione um título simples ao site com o id 'titulo', e um elemento que represente um produto à venda. O produto precisa incluir pelo menos o nome, a descrição e o preço. Pode incluir outros "elementos filhos" se achar necessário como, por exemplo, uma imagem. Procure usar o método simples e o método complexo, ensinados neste tópico.*/

let body = document.body;
let tituloSite = document.createElement("h1");

tituloSite.innerText = "PS4 a venda!"
tituloSite.id = "titulo"
body.appendChild(tituloSite)

let produtoVenda = document.createElement("ol");
produtoVenda.innerHTML = `
<li>Nome do produto</li>
<li>Descrição do produto</li>
<li>Preço do produto</li>
`

body.appendChild(produtoVenda)