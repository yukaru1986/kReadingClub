import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer
import collections
from PIL import Image
st.set_page_config(page_title="形容詞er")

logo1 = Image.open("Images/logo1.png")
logo2 = Image.open("Images/logo2.png")
st.image(logo1)
st.image(logo2)
bg_color = st.radio(
    "BackGround Color?",
    ('white', 'black'))
text_color = st.selectbox(
    'Text Color?',
    ('Blues', 'Oranges', 'Greys','cool'))


# gist_rainbow,cool,Greys,Blues,Oranges,gist_earth

text = st.text_area('⬇️⬇️paste your text here⬇️⬇️')
submit_btn = st.button('submit')
def analyze_text(text: str):
    t = Tokenizer()

    # 頻出単語を取得
    freq_of_words = collections.Counter(
        token.base_form for token in t.tokenize(text)
        # if token.part_of_speech.startswith('名詞'))
        if token.part_of_speech.split(',')[0] in ['形容詞', '形容動詞'])
    return freq_of_words


def generate_wordcloud(analyze_result: str):
    dic_result = dict(analyze_result)


    wordcloud = WordCloud(background_color=bg_color,
                          font_path='Fonts/ZenAntique-Regular.ttf',
                          prefer_horizontal=1,
                          min_font_size=1,
                          max_words=400,
                          font_step=1,
                          colormap=text_color,
                          width=800,
                          height=800).fit_words(dic_result)

    return wordcloud


if submit_btn:
    freq_of_words = analyze_text(text)
    wordcloud = generate_wordcloud(freq_of_words)
    # Wordcloud描画時の警告を非表示にするため
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # WordCloud 表示
    plt.rcParams['font.family'] = 'MS Gothic'
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(wordcloud, interpolation='bilinear')
    image_path = wordcloud
    st.pyplot()

    share_btn = st.button('share on Twitter')

    if share_btn:
        twitter_url = f"https://twitter.com/intent/tweet?text=Check%20out%20this%20image!&url={image_path}&hashtags=MyImage"
        twitter_button = f'<a href="{twitter_url}" target="_blank"><img src="https://www.iconfinder.com/data/icons/social-messaging-productivity-6/128/twitter-512.png" alt="Share on Twitter" height="50"></a>'
        st.write(twitter_button, unsafe_allow_html=True)
