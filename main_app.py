import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer
import collections
from PIL import Image

st.set_page_config(page_title="ワードクラウド")

logo1 = Image.open("Images/logo1.png")
logo2 = Image.open("Images/logo2.png")
st.image(logo1)
st.image(logo2)
bg = st.radio('BackGround Color',('white','black'))
textcolor = st.selectbox('Text Color',('cool',"Greys","Blues","Reds"))
st.divider()
text = st.text_area('⬇️⬇️paste your text here⬇️⬇️')
submit_btn = st.button('make')
st.write('除外中の言葉')
jyogai = ('ある','する','ん','の','れる','てる','こと',
                                                                              'これ','いる','なる','よう','られる','思う',
                                                                              'いう','みたい','何','書く')
st.write(jyogai)


st.divider()
def analyze_text(text: str):
    t = Tokenizer()
    freq_of_words = collections.Counter(
        token.base_form for token in t.tokenize(text)
        if token.part_of_speech.split(',')[0] in['名詞','動詞','形容詞'])

    return freq_of_words




def generate_wordcloud(analyze_result: str):
    dic_result = dict(analyze_result)


    generatedWordCloud = WordCloud(background_color=bg,
                          font_path='Fonts/ZenMaruGothic-Black.ttf',
                          prefer_horizontal=1,
                          min_font_size=10,
                          max_words=75,
                          font_step=1,
                          colormap=textcolor,
                          width=700,
                          height=500).fit_words(dic_result)

    return generatedWordCloud



if submit_btn:

    freq_of_words = analyze_text(text)
    freq_of_words= {k: v for k, v in freq_of_words.items() if not k.endswith(('ある','する','ん','の','れる','てる','こと',
                                                                              'これ','いる','なる','よう','られる','思う',
                                                                              'いう','みたい','何','書く'))}
    generatedWordCloud = generate_wordcloud(freq_of_words)

    # WordCloud 表示
    fig, ax = plt.subplots()
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(generatedWordCloud, interpolation='bilinear')
    st.pyplot(fig)
