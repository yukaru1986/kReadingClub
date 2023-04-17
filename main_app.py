import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer
import collections
from PIL import Image

logo1 = Image.open("Images/logo1.png")
logo2 = Image.open("Images/logo2.png")
st.image(logo1)
st.image(logo2)


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

    wordcloud = WordCloud(background_color='white',
                          font_path='C:/Windows/Fonts/HGRSGU.TTC',
                          width=800,
                          height=800).fit_words(dic_result)
    return wordcloud


if submit_btn:
    freq_of_words = analyze_text(text)
    wordcloud = generate_wordcloud(freq_of_words)
    st.title('あなたの使う形容詞')
    print(text)

    # Wordcloud描画時の警告を非表示にするため
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # WordCloud 表示
    plt.rcParams['font.family'] = 'MS Gothic'
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(wordcloud, interpolation='bilinear')
    st.pyplot()
