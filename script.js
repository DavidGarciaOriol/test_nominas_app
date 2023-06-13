document.addEventListener("DOMContentLoaded", function() {
    var complementoContainer = document.getElementById("complementos-container");
    var agregarComplementoBtn = document.getElementById("agregar-complemento");
  
    agregarComplementoBtn.addEventListener("click", function() {
      var complementoInput = document.createElement("div");
      complementoInput.classList.add("complemento-input");
      
      var nombreInput = document.createElement("input");
      nombreInput.type = "text";
      nombreInput.name = "complemento-nombre[]";
      nombreInput.placeholder = "Nombre del complemento";
      nombreInput.required = true;
  
      var valorInput = document.createElement("input");
      valorInput.type = "number";
      valorInput.classList.add("complemento-valor");
      valorInput.name = "complemento-valor[]";
      valorInput.placeholder = "Valor del complemento";
      valorInput.required = true;

      var deleteButton = document.createElement("button");
        deleteButton.innerHTML = "Eliminar";
        deleteButton.classList.add("delete-button");
        deleteButton.addEventListener("click", function() {
            complementoInput.remove();
        });
  
      complementoInput.appendChild(nombreInput);
      complementoInput.appendChild(valorInput);
      complementoInput.appendChild(deleteButton);
  
      complementoContainer.appendChild(complementoInput);
    });
  });