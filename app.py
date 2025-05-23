from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory dummy data
movies_db = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan"},
    {"id": 2, "title": "The Matrix", "director": "The Wachowskis"}
]

reviews_db = []

# Route: Get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    # TODO: Return the list of all movies as JSON
    pass
    return jsonify([])  # Placeholder return

# Route: Add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    # TODO: Add a new movie to the database
    pass
    return jsonify({"message": "Movie added"}), 201  # Placeholder return

# Route: Get a specific movie by ID
@app.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    # TODO: Return the movie details for the given ID
    pass
    return jsonify({"error": "Movie not found"}), 404  # Placeholder return

# Route: Login form and submission
@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Render login form on GET, validate on POST
    if request.method == 'POST':
        pass
        return "Logged in successfully", 200  # Placeholder for successful login
    else:
        pass
        return render_template("login.html")  # Placeholder return

# Route: Post a review (only for movie_id == 1)
@app.route('/api/reviews', methods=['POST'])
def post_review():
    # TODO: Accept review for movie_id == 1 only
    pass
    return jsonify({"message": "Review submitted"}), 201  # Placeholder return

# Route: Home page
@app.route('/')
def home():
    # TODO: Render home page with movies
    pass
    return "Placeholder: Render the movie rating template here"  # Placeholder return

# Route: Show reviews
@app.route('/reviews')
def review_list():
    # TODO: Render all reviews
    pass
    return "Placeholder: Render the movie rating template here"  # Placeholder return

# Route: Rate movies page
@app.route('/rate', methods=['GET'])
def rate_movies():
    # TODO: Render the rating form










    pass
    return "Placeholder: Render the movie rating template here"

# Route: Submit rating
@app.route('/submit_rating', methods=['POST'])
def submit_rating():
    # TODO: Validate rating and submit
    pass
    return "Rating submitted", 201  # Placeholder return

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
