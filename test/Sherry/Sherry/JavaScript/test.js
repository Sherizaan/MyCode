function changeColor(){
	//fill in the missing ID
	var newColor = document.getElementById('change_button_color').value;
	//set the background color of the button to newColor
	document.getElementById('btn_id').style.backgroundColor=newColor;

}

function showMessage(){
	//fill in the missing ID
	var message = document.getElementById('display_text').value;
	alert(message);
	//alert message
	
}