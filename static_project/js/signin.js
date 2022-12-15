/***animation */
const inputs = document.querySelectorAll(".input");

function addcl() {
  let parent = this.parentNode.parentNode;
  parent.classList.add("focus");
}

function remcl() {
  let parent = this.parentNode.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", addcl);
  input.addEventListener("blur", remcl);
});

/*validation*/
var user = document.querySelector('#username');
user.addEventListener('keyup', function() {
        var u_times = document.querySelector('.u_times');	
		var u_check = document.querySelector('.u_check');	
		if (user.value.length == 0 ||user.value.length < 5) {
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
		if (pass.value.length == 0 ||pass.value.length < 8) {
			p_times.style.display = 'block';
			p_check.style.display = 'none';
            return false;
		} else {
			p_times.style.display = 'none';
			p_check.style.display = 'block';
		}

})
function validate () {
	if (user.value == 0 || user.value.length < 5) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	} else if (pass.value == 0 || pass.value.length < 4) {
		document.getElementById('error').innerHTML = 'من فضلك أدخل البيانات الصحيحة';
		return false;
	} else {
      return true;
	}
}