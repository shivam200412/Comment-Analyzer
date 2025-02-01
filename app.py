from flask import Flask, request, render_template
from googleapiclient.discovery import build
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' (non-interactive)
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# YouTube Data API key
API_KEY = "AIzaSyDYT6ezX34KSBzJY3yiT-jqPRI_W6BvsQU"
youtube = build("youtube", "v3", developerKey=API_KEY)

def fetch_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    print("Fetched Comments:", comments)  # Debugging
    return comments

def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity
        sentiments.append(sentiment)
    print("Sentiment Scores:", sentiments)  # Debugging
    return sentiments

def generate_wordcloud(comments):
    all_comments = " ".join(comments)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_comments)
    
    # Create an in-memory binary stream
    img = io.BytesIO()
    
    # Generate the plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    
    # Save the plot to the in-memory stream
    plt.savefig(img, format="png")
    img.seek(0)
    
    # Encode the image as base64
    return base64.b64encode(img.getvalue()).decode()

def categorize_sentiment(polarity):
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        video_id = video_url.split("v=")[1]
        comments = fetch_comments(video_id)
        sentiments = analyze_sentiment(comments)
        
        # Categorize sentiments
        sentiment_categories = [categorize_sentiment(s) for s in sentiments]
        
        wordcloud_img = generate_wordcloud(comments)
        return render_template("results.html", sentiments=sentiment_categories, wordcloud_img=wordcloud_img)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)