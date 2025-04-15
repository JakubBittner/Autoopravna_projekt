document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("rezervace-btn");

    btn.addEventListener("mouseover", () => {
        btn.style.boxShadow = "0px 0px 20px rgba(255, 153, 0, 0.8)";
    });

    btn.addEventListener("mouseout", () => {
        btn.style.boxShadow = "none";
    });

    btn.addEventListener("click", () => {
        alert("Přesměrování na formulář rezervace (zatím nefunkční)");
    });
});
