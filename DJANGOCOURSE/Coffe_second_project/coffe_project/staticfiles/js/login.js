document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('login-form');
  const loginBtn = document.getElementById('login-btn');
  const btnText = document.getElementById('btn-text');
  const btnSpinner = document.getElementById('btn-spinner');

  if (form && loginBtn) {
    form.addEventListener('submit', function() {
      // Cambia el texto y muestra el spinner al hacer submit
      btnText.textContent = 'Loading...';
      btnSpinner.classList.remove('hidden');
      loginBtn.disabled = true;

      // Después de 5 segundos, reactivamos el botón por si hubo error
      setTimeout(() => {
        btnText.textContent = 'Login';
        btnSpinner.classList.add('hidden');
        loginBtn.disabled = false;
      }, 5000); // Puedes ajustar el tiempo
    });
  }
});