var mail = document.querySelector('#email');
mail.addEventListener('keyup', function() {
        var m_times = document.querySelector('.m_times');	
		var m_check = document.querySelector('.m_check');	
		if (mail.value.length == 0 ) {
			m_times.style.display = 'block';
			m_check.style.display = 'none';
            return false;
		} else {
			m_times.style.display = 'none';
			m_check.style.display = 'block';
		}

})

var fname = document.querySelector('#fullname');
fname.addEventListener('keyup', function() {
        var fn_times = document.querySelector('.fn_times');	
		var fn_check = document.querySelector('.fn_check');	
		if (fname.value.length == 0 ) {
			fn_times.style.display = 'block';
			fn_check.style.display = 'none';
            return false;
		} else {
			fn_times.style.display = 'none';
			fn_check.style.display = 'block';
		}

})
var user = document.querySelector('#username');
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
var pass = document.querySelector('#password');
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
		if (passConf.value.length == 0  || passConf.value != pass.value) {
			pc_times.style.display = 'block';
			pc_check.style.display = 'none';
            return false;
		} else {
			pc_times.style.display = 'none';
			pc_check.style.display = 'block';
		}

})
var bio = document.querySelector('#bio');
bio.addEventListener('keyup', function() {
        var b_times = document.querySelector('.b_times');	
		var b_check = document.querySelector('.b_check');	
		if (bio.value.length == 0 ) {
			b_times.style.display = 'block';
			b_check.style.display = 'none';
            return false;
		} else {
			b_times.style.display = 'none';
			b_check.style.display = 'block';
		}

})
var contact = document.querySelector('#contact');
contact.addEventListener('keyup', function() {
        var d_times = document.querySelector('.d_times');	
		var d_check = document.querySelector('.d_check');	
		if (contact.value.length == 0 ) {
			d_times.style.display = 'block';
			d_check.style.display = 'none';
            return false;
		} else {
			d_times.style.display = 'none';
			d_check.style.display = 'block';
		}

})
var address = document.querySelector('#location');
address.addEventListener('keyup', function() {
        var l_times = document.querySelector('.l_times');	
		var l_check = document.querySelector('.l_check');	
		if (address.value.length == 0 ) {
			l_times.style.display = 'block';
			l_check.style.display = 'none';
            return false;
		} else {
			l_times.style.display = 'none';
			l_check.style.display = 'block';
		}

})
function validate () {
	if (mail.value == 0 ) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	} 
	else if (fname.value == 0) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	}
	else if (user.value == 0 ) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;

	} 
	else if (pass.value == 0) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	}
     else if (pass.value != passConf.value) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	} 
	else if (bio.value == 0) {
        document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
    } 
	else if (contact.value == 0) {
        document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
    } 
	else if (address.value == 0) {
        document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
    }
	
	else {
      return true;
	}
}