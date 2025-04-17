// Mobilní menu toggle
const menuToggle = document.getElementById('mobile-menu');
const navLinks = document.getElementById('nav-links');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Efekt zobrazování sekcí
const sections = document.querySelectorAll('section');

const showSection = () => {
  sections.forEach(section => {
    const rect = section.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      section.classList.add('visible');
    }
  });
};

window.addEventListener('scroll', showSection);
window.addEventListener('load', showSection);

const leveReklamy = [
  {
    src: "/static/img/michelin.png",
    url: "https://www.michelin.cz"
  },
  {
    src: "/static/img/toplac.png",
    url: "https://eshop.toplac.cz"
  }
];

const praveReklamy = [
  {
    src: "/static/img/castrol.png",
    url: "https://www.castrol.com"
  },
  {
    src: "/static/img/azpneu.png",
    url: "https://www.az-pneu.cz"
  }
];

let aktualniIndex = 0;

setInterval(() => {
  aktualniIndex = (aktualniIndex + 1) % leveReklamy.length;

  const levaImg = document.getElementById("reklama-leva");
  const levaOdkaz = document.getElementById("reklama-leva-odkaz");
  const pravaImg = document.getElementById("reklama-prava");
  const pravaOdkaz = document.getElementById("reklama-prava-odkaz");

  // Fade out
  levaImg.classList.add("fade-out");
  pravaImg.classList.add("fade-out");

  setTimeout(() => {
    // Změna obrázků a odkazů
    levaImg.src = leveReklamy[aktualniIndex].src;
    levaOdkaz.href = leveReklamy[aktualniIndex].url;

    pravaImg.src = praveReklamy[aktualniIndex].src;
    pravaOdkaz.href = praveReklamy[aktualniIndex].url;

    // Fade in
    levaImg.classList.remove("fade-out");
    pravaImg.classList.remove("fade-out");
  }, 500); // Musí odpovídat transition času v CSS

}, 30000); // Každých 30 sekund
