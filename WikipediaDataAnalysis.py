import requests
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

nltk.download('punkt')
nltk.download('stopwords')

url = 'https://en.wikipedia.org/wiki/Boris_Johnson'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

text = soup.get_text()

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

word_counts = Counter(filtered_words)

common_words = word_counts.most_common(15)

root = tk.Tk()
root.title('Gráfico Wikipedia de Data Analysis')

words, counts = zip(*common_words)
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(words, counts)
ax.set_xlabel('Frequência')
ax.set_title('15 Palavras Mais Usadas na Página da Wikipedia sobre Boris Johnson')
ax.invert_yaxis()

for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(counts[i]), ha='left', va='center')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
