document.addEventListener('DOMContentLoaded', function() {
  const loginBtn = document.getElementById('login-btn');
  const btnText = document.getElementById('btn-text');
  const btnSpinner = document.getElementById('btn-spinner');

  if (loginBtn) {
    loginBtn.disabled = false;
    btnText.textContent = 'Login';
    btnSpinner.classList.add('hidden');


    loginBtn.addEventListener('click', function() {
      console.log('Botón clickeado');
      
      btnText.textContent = 'Loading...';
      btnSpinner.classList.remove('hidden');
      loginBtn.disabled = true;
    });
  }
});


