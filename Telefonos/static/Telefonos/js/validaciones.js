/* Validacion Boostrap */
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

/* VALIDACION JQUERY */

/* VALIDACION JQUERY */
$("#bRegistro").click(function (event) {
  /* Variables */
  var password1 = $("#inputPassword").val();
  var password2 = $("#inputPassword2").val();
  var usuario = $("#inputUsuario").val();
  var expr = /^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+).+([a-zA-Z0-9]{2,4})+$/;
  var correo = $("#inputCorreo").val();

  /*Validar Contraseñas Iguales */

  if (password2 == "" || password2 !== password1) {
    $("#inputPassword2").focus();
    $("#error4").fadeIn();
    $("#inputPassword2").css({ 'borderColor': '#fa1b1b' });
    event.preventDefault();
  } else {
    $("#error4").hide();
    $("#inputPassword2").css({ 'borderColor': '#008000' });
  }

  /*Validar Contraseña*/

  if (password1 == "") {
    $("#inputPassword").focus();
    $("#error3").fadeIn();
    $("#inputPassword").css({ 'borderColor': '#fa1b1b' });
    event.preventDefault();
  } else {
    $("#error3").hide();
    $("#inputPassword").css({ 'borderColor': '#008000' });
  }

  /*Validar Correo*/

  if (correo == "" || !expr.test(correo)) {
    $("#inputCorreo").focus();
    $("#error2").fadeIn();
    $("#inputCorreo").css({ 'borderColor': '#fa1b1b' });
    event.preventDefault();
  } else {
    $("#error2").hide();
    $("#inputCorreo").css({ 'borderColor': '#008000' });
  }

  /* Validar Usuario*/

  if (usuario == "") {
    $("#inputUsuario").focus();
    $("#error1").fadeIn();
    $("#inputUsuario").css({ 'borderColor': '#fa1b1b' });
    event.preventDefault();

  } else {
    $("#error1").hide();
    $("#inputUsuario").css({ 'borderColor': '#008000' });
  }
});

