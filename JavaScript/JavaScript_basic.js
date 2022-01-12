function changeColor(){
	var code=document.getElementById('color_code').value;
	document.getElementById('canvas_demo').style.backgroundColor=code;
}
function vinny(){
	var FirstName=document.getElementById('First_name').value;
	var Surname=document.getElementById('Surname').value;
	var Age=document.getElementById('Age').value;
	var IdNumber=document.getElementById('id_Number').value;
	document.getElementById('Application_Form').innerHTML='FirstName: '+FirstName +'<br>Surname: '+Surname +'<br>Age: '+Age +'<br>id_Number: '+IdNumber;
}