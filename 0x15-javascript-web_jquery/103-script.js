$('document').ready(function () {
	$('input#btn_translate').click(translate);
	$('input#language_code').focus(function () {
		$(this).keydown(function (e) {
			if (e.keycode === 13) {
				translate();
			}
		});
	});
});

function translate () {
	const url = 'https://www.fourtonfish.com/hellosalut/hello/';
	$.get(url + $.param({ lang: $('input#language_code').val() }), function (data) {
		$('div#hello').html(data.hello);
	});
}
