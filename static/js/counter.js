
  $(document).ready(function() {
      var text_max = $('#id_description').attr('maxlength');
      $('#chars_counter').html(text_max);

      $('#id_description').keyup(function() {
          var text_length = $('#id_description').val().length;
          var text_remaining = text_max - text_length;

          $('#chars_counter').html(text_remaining);
      });
  });
