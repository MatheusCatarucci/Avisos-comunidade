// AVISO PISCANDO
const titulo = document.getElementById('titulo')

setInterval(() => {
  titulo.classList.toggle('aviso');
}, 250);
// Atribuindo algumas variáveis
const lista = document.getElementById('lista')
const input_tarefa = document.getElementById('tarefa')

// FUNÇÃO ADICIONAR
function adicionar_lista(item) {
  const novo_item = document.createElement('li')
  novo_item.classList.add('itens')

  const paragrafo = document.createElement('p')
  paragrafo.textContent = item

  novo_item.append(paragrafo)
  lista.append(novo_item)
}

// FUNÇÃO REMOVER
function remover_lista() {
    lista.lastElementChild.remove()
}

// BOTÃO ADICIONAR
const btn_add = document.getElementById('btn-add')
btn_add.addEventListener('click', () => {
  const texto = input_tarefa.value.trim()
  adicionar_lista(texto)
})

// BOTÃO REMOVER
const btn_remove = document.getElementById('btn-remove')
btn_remove.addEventListener('click', () => {
  remover_lista()
})
