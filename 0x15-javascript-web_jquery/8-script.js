$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    type: "GET",
    success: function(data) {

        $.each(data.results, function(index, movie) {
          // 'index' is the current array index (0, 1, 2, ...)
          // 'movie' is the current movie object at the given index

          $('ul#list_movies').append("<li>" + movie.title + "</li>");
        });
      },
      error: function() {

        alert("Failed to fetch movie titles.");
      }
    });

