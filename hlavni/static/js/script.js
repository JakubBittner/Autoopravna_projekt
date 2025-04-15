// Toggle mobilního menu
document.getElementById("mobile-menu").addEventListener("click", function () {
    const navLinks = document.getElementById("nav-links");
    navLinks.classList.toggle("active");
  });
  
  // Jemná animace pozadí v hlavičce
  document.addEventListener("DOMContentLoaded", () => {
    const hero = document.querySelector(".hero");
  
    let x = 0;
    setInterval(() => {
      x += 0.5;
      hero.style.backgroundPosition = `${x}px ${x}px`;
    }, 50);
  });
  
  // Animace při scrollu - sekce se zjeví hladce
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    {
      threshold: 0.1,
    }
  );
  
  document.querySelectorAll("section").forEach((section) => {
    observer.observe(section);
  });
  