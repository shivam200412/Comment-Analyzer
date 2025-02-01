# **YouTube Comment Analyzer**

A web application that analyzes the sentiment of YouTube video comments and generates a word cloud for visualization.

![image](https://github.com/user-attachments/assets/332194b7-daae-448f-ba74-d38ad88f91a2)


## **Table of Contents**

1. Overview
2. Features
3. Technologies Used
4. Usage
5. API Key Setup
6. License


## **Overview**

The YouTube Comment Analyzer is a Flask-based web application that allows users to input a YouTube video URL and analyze the sentiment of its comments. The application:
- Fetches comments using the YouTube Data API.
- Performs sentiment analysis using TextBlob.
- Generates a word cloud to visualize the most frequent words in the comments.
  
This project is ideal for understanding user engagement, identifying trends, and gaining insights from YouTube comments.


## **Features**

**Sentiment Analysis:**
- Categorizes comments as Positive, Negative, or Neutral.
- Displays the distribution of sentiments in a clean, card-based layout.

**Word Cloud Generation:**
- Generates a word cloud from the comments for quick visualization of frequent words.

**User-Friendly Interface:**
- Simple and intuitive design powered by Bootstrap.
- Responsive layout that works on all devices.

**YouTube Data API Integration:**
- Fetches comments directly from YouTube videos.


## **Technologies Used**

**Backend:**
- Python
- Flask (Web Framework)
- TextBlob (Sentiment Analysis)
- WordCloud (Word Cloud Generation)
- Matplotlib (Plotting)
- YouTube Data API (Comment Fetching)

**Frontend:**
- HTML, CSS, JavaScript
- Bootstrap (Styling)

**Deployment:**
- Heroku, Vercel, or any Flask-compatible hosting service.


## **Usage:**

- Enter a YouTube Video URL:
- On the home page, paste the URL of the YouTube video you want to analyze.
- View Sentiment Analysis:
- The application will display the sentiment distribution (Positive, Negative, Neutral) in a card-based layout.
- Explore the Word Cloud:
- A word cloud will be generated to visualize the most frequent words in the comments.

## **API Key Setup:**

1. To fetch comments from YouTube, you need a YouTube Data API key. Here’s how to get one:
2. Go to the Google Cloud Console.
3. Create a new project.
4. Enable the YouTube Data API v3 for your project.
5. Generate an API key under Credentials.
6. Add the API key to the .env file as described in the Installation section.


## **License:**

This project is licensed under the MIT License. See the LICENSE file for details.


## **Acknowledgments:**

YouTube Data API for providing access to YouTube comments.
TextBlob for sentiment analysis.
WordCloud for generating word clouds.
Bootstrap for the frontend design.

Enjoy analyzing YouTube comments! 🚀
