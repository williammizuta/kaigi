$('a.past_meeting').click(function(event) {
    $('.meeting_notes').load($(this).attr('href') + ' article');
    event.preventDefault();
});
