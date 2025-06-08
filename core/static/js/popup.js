const termsPop = document.getElementById('terms-popup');
const termsBtn = document.getElementById('terms-btn');
const closeBtn = document.getElementById('close-btn');

termsBtn.addEventListener('click', () => {
    termsPop.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    termsPop.style.display = 'none';
});

window.addEventListener('click', (e) => {
    if (e.target === termsPop) {
        termsPop.style.display = 'none';
    }
});


  document.addEventListener('DOMContentLoaded', function() {
    const aboutBtn = document.getElementById('aboutBtn');
    const aboutDropdown = document.getElementById('aboutDropdown');

    aboutBtn.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent default link behavior to stay on the page or handle your own navigation
      if (aboutDropdown.style.display === 'block') {
        aboutDropdown.style.display = 'none';
      } else {
        aboutDropdown.style.display = 'block';
      }
    });

    // Optional: Close dropdown if clicked outside
    document.addEventListener('click', function(event) {
      if (!aboutBtn.contains(event.target) && !aboutDropdown.contains(event.target)) {
        aboutDropdown.style.display = 'none';
      }
    });
  });

