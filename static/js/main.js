// ── HAMBURGER MENU ───────────────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

if (hamburger && mobileNav) {
  hamburger.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
  });
}

// ── PROFILE DROPDOWN ─────────────────────────────────────────────
const profileBtn      = document.getElementById('profileBtn');
const profileDropdown = document.getElementById('profileDropdown');

if (profileBtn && profileDropdown) {
  profileBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = profileDropdown.classList.toggle('open');
    profileBtn.setAttribute('aria-expanded', isOpen);
  });

  // close when clicking anywhere else on the page
  document.addEventListener('click', () => {
    profileDropdown.classList.remove('open');
    profileBtn.setAttribute('aria-expanded', 'false');
  });

  // prevent closing when clicking inside the dropdown
  profileDropdown.addEventListener('click', (e) => {
    e.stopPropagation();
  });
}