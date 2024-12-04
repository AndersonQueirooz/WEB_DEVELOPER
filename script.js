const form = document.getElementById("verbasForm");
const acaoInput = document.getElementById("acao");
const dataPrevistaInput = document.getElementById("dataPrevista");
const investimentoInput = document.getElementById("investimento");
const tabelaVerbas = document.getElementById("tabelaVerbas");
const adicionarBtn = document.getElementById("adicionar");

let verbas = [];

function adicionarVerba() {
  if (!acaoInput.value || !dataPrevistaInput.value || !investimentoInput.value) {
    alert("Por favor, preencha todos os campos.");
    return;
  }

  const novaVerba = {
    id: Date.now(), 
    acao: acaoInput.value,
    dataPrevista: dataPrevistaInput.value,
    investimento: parseFloat(investimentoInput.value).toFixed(2),
  };

  verbas.push(novaVerba);

  atualizarTabela();

  form.reset();
}

function atualizarTabela() {

  tabelaVerbas.innerHTML = "";

  verbas.forEach((verba) => {
    const linha = document.createElement("tr");
    linha.innerHTML = `
      <td>${verba.acao}</td>
      <td>${verba.dataPrevista}</td>
      <td>R$ ${verba.investimento}</td>
      <td><button class="btn btn-warning btn-sm" onclick="editarVerba(${verba.id})">Editar</button></td>
      <td><button class="btn btn-danger btn-sm" onclick="excluirVerba(${verba.id})">Excluir</button></td>
    `;
    tabelaVerbas.appendChild(linha);
  });
}

function editarVerba(id) {

  const verba = verbas.find((item) => item.id === id);

  if (!verba) {
    alert("Registro não encontrado.");
    return;
  }

  acaoInput.value = verba.acao;
  dataPrevistaInput.value = verba.dataPrevista;
  investimentoInput.value = verba.investimento;

  excluirVerba(id);
}

function excluirVerba(id) {

  verbas = verbas.filter((item) => item.id !== id);

  atualizarTabela();
}

adicionarBtn.addEventListener("click", adicionarVerba);
