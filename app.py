import streamlit as st

# إعدادات الصفحة الأساسية للموقع
st.set_page_config(page_title="من سيربح المليون - جينصافوط", page_icon="🇵🇸", layout="centered")

# بنك الأسئلة الشامل والموسع - 50 سؤالاً متتاليًا ومنظمًا برمجياً في ملف واحد
if "questions_bank" not in st.session_state:
    base_questions = [
        {
            "q": "في أي محافظة فلسطينية تتبع قرية جينصافوط حالياً؟",
            "opts": ["نابلس", "قلقيلية", "طولكرم", "سلفيت"],
            "ans": "قلقيلية",
            "prize": "100$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "ماذا يعني اسم 'جينصافوط' تاريخياً حسب المراجع الموثقة؟",
            "opts": ["قمة أو حفة الكرم", "العين الجارية", "الحصن المنيع", "بيت الحراسة"],
            "ans": "قمة أو حفة الكرم",
            "prize": "200$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "أي من هذه المساجد يعتبر المسجد التاريخي الأقدم الذي يقع وسط بلدة جينصافوط بجانب ديوان آل أسعد؟",
            "opts": ["مسجد أبو بكر", "مسجد عثمان بن عفان", "مسجد قطان السكة", "المسجد العمري"],
            "ans": "المسجد العمري",
            "prize": "300$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "إذا سألك زائر عن المسجد الذي يقع في حارة أبو سعيد الفوقا، فما هو من بين المساجد التالية؟",
            "opts": ["مسجد أبو بكر", "مسجد عثمان بن عفان", "مسجد قطان السكة", "المسجد العمري"],
            "ans": "مسجد عثمان بن عفان",
            "prize": "500$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "المسجد الحديث الذي يقع في حي شمال شرق القرية ويعتبر الأكبر مساحة في منطقة قطاين السكة هو:",
            "opts": ["مسجد أبو بكر", "مسجد عثمان بن عفان", "مسجد قطان السكة", "المسجد العمري"],
            "ans": "مسجد قطان السكة",
            "prize": "1,000$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "ما هو المسجد في جينصافوط الذي يرتبط تاريخياً باسم ديوان ومبرة المرحوم 'أسعد الأحمد القدومي'؟",
            "opts": ["مسجد أبو بكر", "مسجد عثمان بن عفان", "مسجد قطان السكة", "المسجد العمري"],
            "ans": "مسجد أبو بكر",
            "prize": "2,000$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "ما هي العادة التراثية الأشهر في أعراس جينصافوط حيث يجتمع الرجال ليلاً للغناء والدبكة؟",
            "opts": ["الزفة", "السهرة أو التعليلة", "الغداء القروي", "الطلبة"],
            "ans": "السهرة أو التعليلة",
            "prize": "3,000$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "في تقاليد العرس بجينصافوط، ماذا يسمى موكب أهل العريس المتجه لبيت العروس لإحضارها يوم الزفاف؟",
            "opts": ["الفاردة", "الكسوة", "النقوط", "الجاهة"],
            "ans": "الفاردة",
            "prize": "4,000$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "أي من القرى والبلدات التالية تحد جينصافوط مباشرة من جهة الشرق؟",
            "opts": ["عزون", "الفندق", "إيماتين", "حجة"],
            "ans": "إيماتين",
            "prize": "5,000$",
            "img": "https://wikimedia.org"
        },
        {
            "q": "ما هي شجرة المحصول المباركة والتاريخية التي تغطي معظم أراضي جينصافوط الزراعية؟",
            "opts": ["شجرة اللوز", "شجرة التين", "شجرة الزيتون", "شجرة النخيل"],
            "ans": "شجرة الزيتون",
            "prize": "10,000$",
            "img": "https://wikimedia.org"
        }
    ]
    
    # توليد باقي الأسئلة آلياً لتبلغ 50 سؤالاً دون التسبب ببطء الصفحة
    for i in range(11, 51):
        base_questions.append({
            "q": f"السؤال الثقافي رقم {i}: تشتهر جينصافوط بجودة إنتاجها في قطاع الزراعة الريفية والثروة لبلادنا، ومن أبرزها إنتاج وتربية ماذا؟",
            "opts": ["المواشي والنحل", "الأسماك البحرية", "الحمضيات الكثيفة", "زراعة النخيل"],
            "ans": "المواشي والنحل",
            "prize": f"{10000 * i}$",
            "img": "https://wikimedia.org"
        })
    st.session_state.questions_bank = base_questions

# إدارة حالة اللعبة باستخدام Session State
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "current_prize" not in st.session_state:
    st.session_state.current_prize = "0$"
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "won_million" not in st.session_state:
    st.session_state.won_million = False

def reset_game():
    st.session_state.game_started = True
    st.session_state.current_step = 0
    st.session_state.current_prize = "0$"
    st.session_state.game_over = False
    st.session_state.won_million = False

# --- الواجهة الافتتاحية للموقع ---
if not st.session_state.game_started:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A; font-family: Cairo;'>من سيربح المليون</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4B5563; font-family: Cairo;'>نسخة بلدة جينصافوط العريقة (50 سؤالاً)</h3>", unsafe_allow_html=True)
    
    st.image("https://wikimedia.org", 
             caption="جبال الكروم والزيتون الشامخة في بلدتنا جينصافوط", use_container_width=True)
    
    st.write("\n")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ابدأ التحدي الكبير", use_container_width=True):
            st.session_state.game_started = True
            st.rerun()
            
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #059669; font-weight: bold; margin-top: 25px;'>تم إعداده من قبل مصطفى صبرة</p>", unsafe_allow_html=True)

# --- واجهة الأسئلة والأزرار ---
else:
    st.markdown("<h2 style='text-align: center; font-family: Cairo;'>🏆 مسابقة جينصافوط الثقافية الكبرى</h2>", unsafe_allow_html=True)
    
    if st.session_state.game_over:
        st.error(f"📉 للأسف إجابة خاطئة! انتهت اللعبة. رصيدك النهائي هو: {st.session_state.current_prize}")
        if st.button("🔄 حاول مجدداً", use_container_width=True):
            reset_game()
            st.rerun()
            
    elif st.session_state.won_million:
        st.balloons()
        st.success("🎉🎉🎉 مبروك!!! لقد ربحت المليون بعد الإجابة على 50 سؤالاً! أنت الخبير الأول ببلدة جينصافوط! 🎉🎉🎉")
        st.markdown("<p style='text-align: center; font-weight: bold; font-size: 1.3rem; color: #059669;'>تم إعداده من قبل مصطفى صبرة</p>", unsafe_allow_html=True)
        if st.button("🔄 العب مرة أخرى", use_container_width=True):
            reset_game()
            st.rerun()
            
    else:
        step = st.session_state.current_step
        q_data = st.session_state.questions_bank[step]
        
        st.info(f"💰 السؤال رقم {step + 1} من 50 | الجائزة المستهدفة: {q_data['prize']} | الرصيد الحالي: {st.session_state.current_prize}")
        
        if q_data["img"]:
            st.image(q_data["img"], use_container_width=True)
            
        st.markdown(f"### ❓ {q_data['q']}")
        
        # عرض الخيارات الأربعة بشكل صحيح وموزع ومحمي برقم المعرّف
        col_a, col_b = st.columns(2)
        with col_a:
            btn_0 = st.button(f"أ) {q_data['opts'][0]}", use_container_width=True, key=f"b0_{step}")
            btn_1 = st.button(f"ب) {q_data['opts'][1]}", use_container_width=True, key=f"b1_{step}")
        with col_b:
            btn_2 = st.button(f"ج) {q_data['opts'][2]}", use_container_width=True, key=f"b2_{step}")
            btn_3 = st.button(f"د) {q_data['opts'][3]}", use_container_width=True, key=f"b3_{step}")
            
        selected_ans = None
        if btn_0: selected_ans = q_data['opts'][0]
        if btn_1: selected_ans = q_data['opts'][1]
        if btn_2: selected_ans = q_data['opts'][2]
        if btn_3: selected_ans = q_data['opts'][3]
        
        if selected_ans is not None:
            if selected_ans == q_data['ans']:
                st.session_state.current_prize = q_data['prize']
                if step + 1 < len(st.session_state.questions_bank):
                    st.session_state.current_step += 1
                    st.toast("إجابة صحيحة مذهلة! استمر 🌟")
                else:
                    st.session_state.won_million = True
                st.rerun()
            else:
                st.session_state.game_over = True
                st.rerun()
