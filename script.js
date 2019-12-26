function changeColor(id1, id2) {
	elem1 = document.getElementById(id1);
	elem2 = document.getElementById(id2);

	elem1.style.color = 'rgb(204, 237, 228)';
	elem1.style.backgroundColor = 'rgb(26, 177, 136)';
	elem2.style.color = 'rgb(255, 255, 255)';
	elem2.style.backgroundColor = 'rgb(67, 82, 88)';
}

let square1 = document.getElementById('square1');

square1.addEventListener('click', function() {
	this.style.transition = "opacity 5s ease-in";
	this.style.opacity = 0;
});

let square2 = document.getElementById('square2');

square2.addEventListener('click', function() {
	let maxWidth = this.parentElement.clientWidth - 250;
	let pos1 = 20;
	let pos2 = 0;
	let pos3 = maxWidth;
	let id = setInterval(frame, 5);

	function frame() {
		if (pos1 == 0)
			if (pos2 == maxWidth)
				if (pos3 == 20)
					clearInterval(id);
				else {
					pos3--;
					square2.style.marginLeft = pos3 + "px";
				}
			else {
				pos2++;
				square2.style.marginLeft = pos2 + "px";
			}
		else {
			pos1--;
			square2.style.marginLeft = pos1 + "px";
		}
	}
});

let square3 = document.getElementById('square3');

square3.addEventListener('click', function() {
	this.style.transition = "all 2s";
	this.style.borderRadius = 50 + "%";
});

let square4 = document.getElementById('square4');
let choise = true;
let pos4 = 20;
let id4;

square4.addEventListener("mouseover", function() {
	id4 = setInterval(frame, 5);
	function frame() {
		if (choise == true) {
			pos4++;
			square4.style.marginLeft = pos4 + "px";
			if (pos4 == square4.parentElement.clientWidth - 250)
				choise = false;
		} else {
			pos4--;
			square4.style.marginLeft = pos4 + "px";
			if (pos4 == 0)
				choise = true;
		}
	}
});

square4.addEventListener("mouseout", function() {
	clearInterval(id4);
});
