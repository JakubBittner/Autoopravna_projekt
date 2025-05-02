
function showSection(sectionId) {
  // Skrytí všech sekcí
  const sections = document.querySelectorAll('.content-section');
  sections.forEach(section => section.classList.add('hidden'));

  // Zobrazení vybrané sekce
  const target = document.getElementById(sectionId);
  if (target) {
    target.classList.remove('hidden');
  }

  // Odebrání 'active' z odkazů
  const links = document.querySelectorAll('.sidebar a');
  links.forEach(link => link.classList.remove('active'));

  // Přidání 'active' aktuálnímu odkazu
  const activeLink = document.getElementById(sectionId + '-link');
  if (activeLink) {
    activeLink.classList.add('active');
  }
}

// Zachycení kliknutí na odkazy a zamezení reloadu
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
    });
  });
});

