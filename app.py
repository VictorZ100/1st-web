import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path

#---PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

#find more emojis here: https://www.iemoji.com/emoji-cheat-sheet/smileys-people
st.set_page_config(page_title="Huckleberry派", page_icon="tada", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/20133996-1f36-47b3-8337-6df7eabb0171/dyGPAmJPAf.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("爱你哦 :kissing_heart:")
    st.title("依依宝贝")
    st.write("看我学会编网站啦！哈哈哈哈哈")

# ----More Writing----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("讲故事啦～")
        st.write("##")
        st.write(
            """
            “总有一天我的Huckleberry 派会是全世界最好吃的” 兔子边说边喝着她的葡萄汁。狐狸温馨地看着兔子点了点头。“看着我笑干嘛, 你呢？你的梦想是什么？” 
            兔子边问边喝完了她的葡萄汁。 “我吗？我想有一天逃出这个无聊的狐狸窝，去环游世界”狐狸看着洞外回答道。 “外面的世界吗，你的意思是离开这个森林”兔子被狐狸刚才的回答下了一跳。
            狐狸能看出来兔子在担心他，因为每次她那两只雪白色的耳朵都会蹦起来。看着兔子可爱又担心的表情狐狸笑了，说道：“我听过别的动物有说外面的世界有多么危险，但外面也有有趣的东西呀”。
            “比如说呢？” 兔子一脸不信的说道. “外面有传说中一望无边的盐水，金黄色的大陆，和五颜六色的高楼。夏天能吃的雪，还有能使动物疯狂的饮料”，狐狸越说越兴奋。
            看到狐狸的大尾巴摆来摆去，兔子看得出狐狸很对外面的事物是多么的激动。但是兔子还是不以为然，说道：“你就为了这些就要丢下你现在拥有的一切吗？”。
            “我现在所拥有的一切？除了一个这个每次下雨都会变得潮湿无比的窝以外，我还有什么啊。我真是受够了”狐狸抱怨道。看到狐狸的尾巴没了刚才的摇摆兔子赶紧说道：
            “你有清晨的花香，夜空的繁星，还有我……”兔子试着安慰狐狸但到后面害羞了起来，所以最后一点她是咕哝着说的。“最后一部分说的是什么？”狐狸想问兔子但是兔子用着她的大耳朵捂着那早已红的像个西红柿的脸，
            结巴地说道：“不早了我要回家了”。说完兔子就飞速地溜回了家，狐狸跟她说声再见的机会都没有，只能傻里吧唧地在原地挠头，脑子里尝试去搞清楚刚才兔子咕哝的话。

            随着时间慢慢的流失，我们终于等到了狐狸准备好的那天。在他离开当天，附近的小动物们都来向他告别，当然我们的朋友兔子也包括在内。兔子带了一块她亲手做的Huckleberry派，遗憾的是派没有她想象中的那么好。
            狐狸笑了笑并把派放在了背包里留给旅途上吃，然后狐狸给了兔子一个温暖的拥抱。兔子在狐狸的怀抱里向狐狸表了白，希望狐狸能留下来继续跟她过着简单快乐的森林生活。狐狸听完亲吻了兔子的额头… 

            “所以他最后真的亲你了？”，松鼠边问着兔子边挑了一个Huckleberry派。“真是不敢相信他亲吻完后还是走了”山猫补充道。兔子忙着面包店里的工作，不想接他们话。
            自从狐狸离开有一段时间了，兔子在狐狸不在的时间里不仅完善了她的Huckleberry派还开了一家面包店。“说实话那个告别吻还挺自私的”松鼠又说。“够了！”兔子终于忍不住说道。
            “如果你们想买派就买派，别在我店里八卦这个事，我不想聊这个事。”兔子边讲边竖起了耳朵。“是啊，那个吻的确挺自私的” 突然一个熟悉的声音从店外传了进来，紧接着入店铃声响起。兔子不敢相信她的眼睛，但她的身体做出了本能的反应。
            “狐狸！”兔子立马跳到了狐狸的面前，给狐狸来了个大大的拥抱。山猫和松鼠也自觉的把要买的Huckleberry派放了回去，说明天再来买。离开面包店时还帮兔子把打烊的牌子放道了门外。“我以为再也见不到你了！”兔子说着说着眼里的泪水就打起了转儿“。
            狐狸摸着兔子的头安慰道：“傻瓜，我怎么会不回来呢”。 兔子揉了揉本来就红的眼睛问狐狸：“是什么让你决定提前回来的呀”。狐狸看着兔子，笑着说道：“我走遍了外面的世界，看到了许多我无法想象的东西；一望无边的盐水，金黄色的大陆，和五颜六色的高楼。
            吃了夏天能吃的雪，喝了能使我疯狂的饮料，但归根结底我还是更喜欢你亲手做的Huckleberry派”。 

            """
        )
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
#LOAD CSS
with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
    
