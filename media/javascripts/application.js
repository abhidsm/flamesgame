$(document).ready(function(){
	bindFormValidation();
    });

function formSubmitAction() {
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
}

function resetResultClass(){
    $('#result').removeClass();
    $('#result').addClass('center');
    $('#result').addClass('span-11');
    $('#result').addClass('last');

    setTimeout(function(){ $('#load').hide();  $('#submit').show();     $('#result').fadeIn('slow').delay(2000).fadeOut('slow'); }, 2000);

}

function bindFormValidation() {
    $('#flames-form').validate({
	    rules: {
		your_name: "required",
		partner_name: "required"
		    },
	    messages: {
		your_name: "Please enter your name",
		partner_name: "Please enter your partner name"
		    },
		focusCleanup: true,
		submitHandler: function(form) {
		$('#load').show();
		$('#submit').hide();
		formSubmitAction();
	    }
	});
}
 