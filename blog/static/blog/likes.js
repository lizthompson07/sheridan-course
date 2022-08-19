/* Example likes request */

const pre = document.querySelector('pre');

function likeHandler(event) {
	event.preventDefault();

  // Get the element that was clicked on. It's the event
  // currentTarget property.
  const element = event.currentTarget;
  // This is an <a> tag and has a readable href property

  // Print out the result
  pre.textContent = 'URL:  ' + element.href + '\n';

}

// Select multiple classes: both like & dislike buttons
document.querySelectorAll('.like, .dislike')
	.forEach(function (link) {
		link.addEventListener('click', likeHandler);
	});

const element = event.currentTarget
const url = element.href

fetch(url, {
    method: 'POST',
    // Set the CSRF token header
    headers: { 'X-CSRFToken': csrftoken },
});

//};