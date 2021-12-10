$(document).ready(function(){
  $("#botonFormularioCliente").click(function(){
    $('#Paso1').removeClass("is-active");
    $('#Paso2').addClass("is-active");
    $('#FormularioCliente').removeClass("is-active");
    $('#FormularioMesa').addClass("is-active");
  });

  $("#botonRetroceder").click(function(){
    $('#Paso1').addClass("is-active");
    $('#Paso2').removeClass("is-active");
    $('#FormularioCliente').addClass("is-active");
    $('#FormularioMesa').removeClass("is-active");
  });
  
  $("#EliminarDatosFormularioReserva").click(function(){
    document.getElementById("FormularioComprobarReserva").reset();
  });
   
});
  





