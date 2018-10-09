// pseudo code - change as needed

(function($) {
    $(function() {
        var selectField = $('#id_selectField'),
            verified = $('#id_verified');

        function toggleVerified(value) {
            value == 'value2' ? verified.show() : verified.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);