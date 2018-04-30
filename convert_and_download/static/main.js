// Add new exporter

define([
    'jquery',
    'base/js/namespace',
    'tree/js/notebooklist',
    'base/js/utils'
], function(
    $,
    Jupyter,
    NotebookList,
    utils
) {
    // "use strict";

    // var action = {
    //         icon: 'fa-comment-o', // a font-awesome class used on buttons, etc
    //         help    : 'Convert to PDF and Download',
    //         help_index : 'zz',
    //         handler : convert_and_download
    //     };

    function load_ipython_extension() {

        convert_and_download = function() {
            var selected = [];
            $('.list_item :checked').each(function(index, item) {
                var parent = $(item).parent().parent();
                selected.push({
                    name: parent.data('name'),
                    path: parent.data('path'),
                    type: parent.data('type')
                });
            });
            var url = utils.url_path_join(utils.get_body_data("baseUrl"), 'dlconvert', 'pdf');
            for (var i in selected) {
                var item = selected[i];
                url = utils.url_path_join(url, utils.encode_uri_components(item.path));
            }
            url = url + '?download=true';
            var w = window.open('', Jupyter._target);
            w.location = url;
        };

        $('<button/>')
            .addClass('convert-download-button btn btn-default btn-xs')
            .attr('title', 'Convert and Download selected')
            .attr('aria-label', 'Convert and Download selected')
            .text('Convert and Download selected')
            .insertBefore('.shutdown-button')
            .on('click', convert_and_download);

    };

    return {
        load_ipython_extension: load_ipython_extension
    };
});
