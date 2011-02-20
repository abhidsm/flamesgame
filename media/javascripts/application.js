$(document).ready(function(){
	$("#flames-form").submit(function(){
		$.post($("#flames-form").attr('action'),
		       $("#flames-form").serialize(),
		       function(data){
			   response = JSON.parse(data);
			   $('#result h3').html(response.flames.result);
			   resetResultClass();
			   $('#result').addClass(response.flames.status);
		       }	      
		       );
		return false;
	    });
    });

function resetResultClass(){
    $('#result').removeClass();
    $('#result').addClass('center');
    $('#result').addClass('span-11');
    $('#result').addClass('last');
    $('#result').show();
}