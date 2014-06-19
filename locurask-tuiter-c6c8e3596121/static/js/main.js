
/**
* Esta funcion se va a encargar de manejar los click
* que le damos al boton eliminar tuit!..
*/
function eliminar_tuit(ele){

	var id_tuit = $(this).attr('data-tuit');
	
	var url = "/core/eliminar_tuit/"+id_tuit+"/";
	
	$.post(url, function( resp ) {

  		if(resp.success){
  			$("#id_contenedor_tuit_"+id_tuit).fadeOut("slow");
  			$("#id_profile_cantidad_de_tuits").html(resp.cant_tuits);
  		}else{
  			alert("Disculpa, no se pudo eliminar el tuit! :( ");
  		}
	});

	return false;	
};



$(function(){

	$(".eliminar-tuit").bind('click', eliminar_tuit);	

});

