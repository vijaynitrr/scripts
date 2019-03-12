HOMEPAGE_NAME = "GeeksforGeeks | A computer science portal for geeks"
WIDTH = 70

pageName = document.title

if(pageName!=HOMEPAGE_NAME) {
	document.getElementById('secondary').remove();
	document.getElementsByClassName('leftSideBarParent')[0].remove();
	document.getElementById('menu-top').remove();
	document.getElementById('MasterHead').remove();
	body = document.getElementsByClassName('site-content')[0];
	body.style.width = WIDTH+"%";
	body.style.float='none';
	body.style.margin='auto';
}
