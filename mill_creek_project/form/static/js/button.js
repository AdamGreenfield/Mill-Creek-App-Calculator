function ready3(check1, check2, check3){
	if(document.getElementById(check1).checked == true || document.getElementById(check2).checked == true || document.getElementById(check3).checked == true){
		document.getElementById('submit').src="/static/img/next-ready.png";
		document.getElementById('submit').disabled = false;
	}
	else{
		document.getElementById('submit').src="/static/img/next-notready.png";
		document.getElementById('submit').disabled = true;
	}
}

function ready2(check1, check2){
	if(document.getElementById(check1).checked == true || document.getElementById(check2).checked == true){
		document.getElementById('submit').src="/static/img/next-ready.png";
		document.getElementById('submit').disabled = false;
	}
	else{
		document.getElementById('submit').src="/static/img/next-notready.png";
		document.getElementById('submit').disabled = true;
	}
}

function ready6(check1, check2, check3, check4, check5, check6){
	if(document.getElementById(check1).checked == true || document.getElementById(check2).checked == true || document.getElementById(check3).checked == true || document.getElementById(check4).checked == true || document.getElementById(check5).checked == true || document.getElementById(check6).checked == true){
		document.getElementById('submit').src="/static/img/next-ready.png";
		document.getElementById('submit').disabled = false;
	}
	else{
		document.getElementById('submit').src="/static/img/next-notready.png";
		document.getElementById('submit').disabled = true;
	}
}