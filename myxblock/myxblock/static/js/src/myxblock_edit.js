function MyXBlockEditAside(runtime, element, block_element, init_args) {
    console.log('here');
    return new MyXBlockEditBlock(runtime, element);
}

function MyXBlockEditBlock(runtime, element) {
    console.log('there');
    $(element).find('.save-button').bind('click', function() {
	var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
	var data = {
	    link_url = $(element).find('input[name=link_url]').val(),
	    link_name = $(element).find('input[name=link_name]').val(),
	    description = $(element).find('input[name=description]').val()
	};
	runtime.notify('save', {state: 'start'});
	$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
	    runtime.notify('save', {state: 'end'});
	});
    });

    $(element).find('.cancel-button').bind('click', function() {
	runtime.notify('cancel', {});
    });
}