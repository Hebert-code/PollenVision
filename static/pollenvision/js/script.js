function toggleMenu() {
    const menu = document.getElementById("menuLateral");
    const toggleButton = document.getElementById("toggleMenu");

    
    menu.classList.toggle("menu-hidden");

    if (menu.classList.contains("menu-hidden")) {
        toggleButton.innerHTML = "&#9776;"; 
    } else {
        toggleButton.innerHTML = "&#10006;"; // para fechar
    }

}

const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("image_path");

// Função para lidar com o drop
function handleDrop(event) {
    event.preventDefault();
    const files = event.dataTransfer.files;
    
    if (files.length > 0) {
        fileInput.files = files;  // Atribui o arquivo ao input de arquivo
    }
}

// Estilo visual quando o arquivo é arrastado sobre a área
dropArea.addEventListener("dragover", () => {
    dropArea.classList.add("highlight");
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("highlight");
});