//REG
var reg = {
	codes_post: function(){
		var name = $('#name').val();
		var lastname = $('#lastname').val();
		var email = $('#email').val();
		var new_pass = $('#new_pass').val();
		var new_pass2 = $('#new_pass2').val();
		var rndval = new Date().getTime(); 
		
		if(name != 0){
			if(isValidName(name)){
				if(lastname != 0){
					if(isValidName(lastname)){
						if(email != 0 && isValidEmailAddress(email)){
							if(new_pass != 0 && new_pass.length >= 6){
								if(new_pass == new_pass2){
									reg_cc('', 3000);
									$('#val_sec_code').focus();
								} else {
									error_pass2_sys('', 3000);							
								}
							} else {
								error_pass_sys('', 3000);							
							}
						} else {
							error_email_sys('', 3000);
						}
					} else {
						error_name_lastname('', 3000);
					}
				} else {
					error_name_lastnameClos('', 3000);
				}
			} else {
				error_name_lastname('', 3000);
			}
		} else {
			error_name_lastnameClos('', 3000);
		}
	},
	send: function(sec_code){
		var email = $('#email').val();
		var new_pass = $('#new_pass').val();
		var new_pass2 = $('#new_pass2').val();
		var name = $('#name').val();
		var lastname = $('#lastname').val();
		var val_sec_code = $("#val_sec_code").val();
		var sex = $("#sex").val();
		var day = $("#day").val();
		var month = $("#month").val();
		var year = $("#year").val();
		var country = $("#country").val();
		var city = $("#select_city").val();
		$.post('/index.php?go=register', {
				name: name,
				lastname: lastname,
				email: email,
				sex: sex,
				day: day,
				month: month,
				year: year,
				country: country,
				city: city,
				password_first: new_pass,
				password_second: new_pass2,
				sec_code: sec_code
			}, function(d){
			var exp = d.split('|');
			if(exp[0] == 'ok'){
				window.location = '/settings';
			} else if(exp[0] == 'err_mail'){
				var tim = 1;
				setTimeout("$('.privacy_err').fadeOut('fast')", tim);
				error_email_nove('', 3000);							
			} else {
				var tim = 1;
				setTimeout("$('.privacy_err').fadeOut('fast')", tim);
				setErrorInputMsg('sec_code');
				error_post_nove('', 3000);							
			}
		});
	}
}


function isValidName(xname){
	var pattern = new RegExp(/^[a-zA-Zа-яА-Я]+$/);
 	return pattern.test(xname);
}
function isValidEmailAddress(emailAddress) {
 	var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
 	return pattern.test(emailAddress);
}
function updateCode(){
	var rndval = new Date().getTime(); 
	$('#sec_code').html('<img src="/css/antibot/css/antibot.php?rndval=' + rndval + '" alt="" title="Показать другой код" width="120" height="50" />');
}
function checkCode(){
	var val_sec_code = $("#val_sec_code").val();
	$('#code_loading').html('<img src="'+template_dir+'/images/loading_mini.gif" style="margin-top:21px" />');
	$.get('/css/antibot/sec_code.php?user_code='+val_sec_code, function(data){
		if(data == 'ok'){
			reg.send(val_sec_code);
		} else {
			updateCode();
			$('#code_loading').html('<input type="text" id="val_sec_code" class="inpst" maxlength="6" style="margin-top:10px;width:110px" />');
			$('#val_sec_code').val('');
			$('#val_sec_code').focus();
		}
	});
}