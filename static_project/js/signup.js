const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

/******validation */
var mail = document.querySelector('#email');
mail.addEventListener('keyup', function() {
        var m_times = document.querySelector('.m_times');	
		var m_check = document.querySelector('.m_check');	
		if (mail.value.length == 0) {
			m_times.style.display = 'block';
			m_check.style.display = 'none';
            return false;
		} else {
			m_times.style.display = 'none';
			m_check.style.display = 'block';
		}

})
var user = document.querySelector('#user');
user.addEventListener('keyup', function() {
        var u_times = document.querySelector('.u_times');	
		var u_check = document.querySelector('.u_check');	
		if (user.value.length == 0 ) {
			u_times.style.display = 'block';
			u_check.style.display = 'none';
            return false;
		} else {
			u_times.style.display = 'none';
			u_check.style.display = 'block';
		}

})
var fullName = document.querySelector('#fullname');
fullName.addEventListener('keyup', function() {
        var fn_times = document.querySelector('.fn_times');	
		var fn_check = document.querySelector('.fn_check');	
		if (fullName.value.length == 0 ) {
			fn_times.style.display = 'block';
			fn_check.style.display = 'none';
            return false;
		} else {
			fn_times.style.display = 'none';
			fn_check.style.display = 'block';
		}

})
var pass = document.querySelector('#pass');
pass.addEventListener('keyup', function() {
        var p_times = document.querySelector('.p_times');	
		var p_check = document.querySelector('.p_check');	
		if (pass.value.length == 0 ) {
			p_times.style.display = 'block';
			p_check.style.display = 'none';
            return false;
		} else {
			p_times.style.display = 'none';
			p_check.style.display = 'block';
		}

})
var passConf = document.querySelector('#pass-conf');
passConf.addEventListener('keyup', function() {
        var pc_times = document.querySelector('.pc_times');	
		var pc_check = document.querySelector('.pc_check');	
		if (passConf.value.length == 0 || passConf.value!= pass.value ) {
			pc_times.style.display = 'block';
			pc_check.style.display = 'none';
            return false;
		} else {
			pc_times.style.display = 'none';
			pc_check.style.display = 'block';
		}

})

function validate () {
	if (user.value == 0 ) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	} 
	else if (fullName.value == 0) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	}
	else if (pass.value == 0 ) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;

	} else if (pass.value != passConf.value) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	}
	
	else {
      return true;
	}
}