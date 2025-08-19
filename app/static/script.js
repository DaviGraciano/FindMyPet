document.getElementById("cadastroForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const fone = document.getElementById("fone").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:8000/cadastro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name, email, fone, password })
  })
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.error("Erro:", error));;

  const result = await response.json();
  document.getElementById("msg").innerText = result.msg || "Erro ao cadastrar!";
});
