function dateUnformat(date) {
	return date.slice(8,10) + "-" + date.slice(5,7) + "-" + date.slice(0, 4)
}

function dateFormat(date) {
	return date.slice(6, 10) + "-" + date.slice(3,5) + "-" + date.slice(0,2) 
}