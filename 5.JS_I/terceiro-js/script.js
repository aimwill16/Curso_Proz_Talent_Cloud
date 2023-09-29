let elementoH1 = document.querySelector("#titulo")
let elementoA = document.querySelector("a")
let elementoList = document.querySelector("#lista-ordenada")
let elementoListUl = document.querySelector("ul")

elementoH1.innerText = "Novo texto com JS";
elementoA.innerText = "Esse é um link criado pelo JS"
elementoList.innerHTML = `
    <li><a href="http://www.google.com.br">Google</a></li>
    <li><a href="http://www.bing.com.br">Bing</a></li>
    <li><a href="http://www.brave.com.br">Navegador Brave</a></li>
`
elementoListUl.innerHTML = `
<li> JS item 1</li>
<li> JS item 2</li>
<li> JS item 3</li>
`