// In your Javascript (external .js resource or <script> tag)
$(document).ready(function() {
    $(".js-example-basic-single").select2({
        placeholder: "{{position}}",
        allowClear: true,
    });
});