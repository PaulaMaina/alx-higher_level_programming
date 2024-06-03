let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data) {
	let movies = data.results;
	for (let movie of movies) {
		$('ul#list_movies').append('<li>${movie.title}</li>');
	}
});
