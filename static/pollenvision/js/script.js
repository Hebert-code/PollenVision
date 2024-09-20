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