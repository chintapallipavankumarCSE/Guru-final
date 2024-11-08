from flask import Blueprint, request, jsonify
from .nlp_model import process_question
from .scraper import scrape_website

main = Blueprint('main', __name__)

@main.route('/query', methods=['POST'])
def query():
    data = request.json
    url = data.get('url')
    question = data.get('question')

    if not url or not question:
        return jsonify({'error': 'URL and question are required!'}), 400

    # Scrape the website content
    content = scrape_website(url)
    
    if content is None:
        return jsonify({'error': 'Failed to scrape website.'}), 500

    # Process the question with NLP
    answer = process_question(content, question)

    return jsonify({'answer': answer})
