import os
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# ========= إعدادات البوت =========
التوكن = os.environ.get("TELEGRAM_BOT_TOKEN")
ايدي_المالك = int(os.environ.get("TELEGRAM_OWNER_ID", "0"))
يوزر_المالك = os.environ.get("TELEGRAM_OWNER_USERNAME", "wailabuMohammed").lower().replace("@","")

def هل_هو_المالك(المستخدم):
    if ايدي_المالك!= 0 and المستخدم.id == ايدي_المالك:
        return True
    if المستخدم.username and المستخدم.username.lower() == يوزر_المالك:
        return True
    if المستخدم.username and المستخدم.username.lower() == "wailabumohammed":
        return True
    return False

logging.basicConfig(level=logging.INFO)

# ========= بيانات القرآن =========
السور = ["الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس","هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه","الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجدة","الأحزاب","سبأ","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة","الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج","نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبأ","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات","القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الإخلاص","الفلق","الناس"]
القراء = ["مشاري راشد العفاسي","ماهر المعيقلي","عبدالرحمن السديس","محمود خليل الحصري","ياسر الدوسري","أحمد العجمي","سعد الغامدي","عبدالباسط عبدالصمد"]
الايات = ["﴿ إِنَّ مَعَ الْعُسْرِ يُسْرًا ﴾","﴿ وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا ﴾","﴿ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ ﴾","﴿ فَإِنِّي قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ الدَّاعِ إِذَا دَعَانِ ﴾","﴿ وَاصْبِرْ فَإِنَّ اللَّهَ لَا يُضِيعُ أَجْرَ الْمُحْسِنِينَ ﴾","﴿ لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا ﴾"]
الاذكار = "📿 **الأذكار اليومية**\n\n🌅 أذكار الصباح:\n• سبحان الله وبحمده 100 مرة\n• لا إله إلا الله وحده لا شريك له\n• حسبي الله لا إله إلا هو\n\n🌙 أذكار المساء:\n• آية الكرسي\n• سورة الإخلاص والفلق والناس 3 مرات\n• اللهم بك أمسينا وبك أصبحنا\n\n🤲 أذكار عامة:\n• سبحان الله\n• الحمد لله\n• لا إله إلا الله\n• الله أكبر\n• لا حول ولا قوة إلا بالله\n• أستغفر الله"

العاب_مؤقتة = {}

# ========= لوحة المفاتيح الرئيسية عربية 100% =========
def لوحة_الرئيسية():
    return ReplyKeyboardMarkup(
        [["📖 القرآن الكريم 🧠 دردشة ذكية"],["🎮 الألعاب 📥 التحميل"],["👑 لوحة المالك"]],
        resize_keyboard=True
    )

# ========= رسالة البداية =========
async def البداية(update: Update, context: ContextTypes.DEFAULT_TYPE):
    المستخدم = update.effective_user
    مالك = هل_هو_المالك(المستخدم)
    if مالك:
        رسالة = f"👋 أهلاً وسهلاً يا مالك البوت الأسطوري!\n\n🔥 البوت شغال 100% وبكل قوته!\n🆔 آيديك: {المستخدم.id}\n👤 معرفك: @{المستخدم.username}\n\n👇 اختر من القائمة الأسطورية:"
    else:
        رسالة = f"👋 أهلاً وسهلاً يا {المستخدم.first_name}!\n\n🌟 مرحباً بك في البوت الأسطوري - البوت العربي الشامل\n\n📖 قرآن كريم بصوت أجمل القراء\n🧠 دردشة ذكية تفهمك\n🎮 ألعاب ممتعة\n📥 تحميل من كل المنصات\n\n👇 اختر من القائمة:"
    await update.message.reply_text(رسالة, reply_markup=لوحة_الرئيسية())

# ========= قسم القرآن =========
async def قائمة_القرآن(update: Update, context: ContextTypes.DEFAULT_TYPE):
    لوحة = [
        [InlineKeyboardButton("🎧 الاستماع للسور", callback_data="قرآن_استماع"),
         InlineKeyboardButton("📖 قراءة القرآن", callback_data="قرآن_قراءة")],
        [InlineKeyboardButton("🎙️ القراء", callback_data="قرآن_قراء"),
         InlineKeyboardButton("📅 آية اليوم", callback_data="قرآن_آية")],
        [InlineKeyboardButton("📿 الأذكار", callback_data="قرآن_اذكار"),
         InlineKeyboardButton("🔍 البحث", callback_data="قرآن_بحث")],
        [InlineKeyboardButton("🤲 أدعية", callback_data="قرآن_ادعية")]
    ]
    await update.message.reply_text("📖 **قسم القرآن الكريم - البوت الأسطوري**\n\nاختر ما تريد سماعه أو قراءته:", reply_markup=InlineKeyboardMarkup(لوحة), parse_mode="Markdown")

async def ازرار_القرآن(update: Update, context: ContextTypes.DEFAULT_TYPE):
    استعلام = update.callback_query
    await استعلام.answer()
    البيانات = استعلام.data

    if البيانات == "قرآن_استماع":
        ازرار = [[InlineKeyboardButton(f"{i+1}. {اسم}", callback_data=f"تشغيل_{i+1}")] for i, اسم in enumerate(السور[:15])]
        ازرار.append([InlineKeyboardButton("➡️ المزيد من السور", callback_data="قرآن_المزيد1")])
        ازرار.append([InlineKeyboardButton("🔙 رجوع", callback_data="رجوع_قرآن")])
        await استعلام.edit_message_text("🎧 **اختر السورة للاستماع المباشر:**\nبصوت مشاري العفاسي", reply_markup=InlineKeyboardMarkup(ازرار))

    elif البيانات.startswith("قرآن_المزيد"):
        رقم = int(البيانات.replace("قرآن_المزيد","")) if البيانات.replace("قرآن_المزيد","").isdigit() else 1
        بداية = رقم * 15
        نهاية = بداية + 15
        ازرار = [[InlineKeyboardButton(f"{i+1}. {اسم}", callback_data=f"تشغيل_{i+1}")] for i, اسم in enumerate(السور[بداية:نهاية], start=بداية)]
        ازرار.append([InlineKeyboardButton("➡️ المزيد", callback_data=f"قرآن_المزيد{رقم+1}"), InlineKeyboardButton("⬅️ السابق", callback_data=f"قرآن_المزيد{رقم-1}")])
        await استعلام.edit_message_text(f"🎧 **السور {بداية+1} - {نهاية}:**", reply_markup=InlineKeyboardMarkup(ازرار))

    elif البيانات.startswith("تشغيل_"):
        رقم_السورة = البيانات.split("_")[1]
        رابط = f"https://server8.mp3quran.net/afs/{رقم_السورة.zfill(3)}.mp3"
        اسم_السورة = السور[int(رقم_السورة)-1]
        await استعلام.message.reply_audio(audio=رابط, caption=f"📖 سورة {اسم_السورة}\n🎙️ القارئ: مشاري العفاسي\n🤲 تقبل الله منا ومنكم")
        await استعلام.message.reply_text(f"✅ يتم الآن تشغيل سورة {اسم_السورة}\n\nهل تريد سورة أخرى؟", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎧 اختيار سورة أخرى", callback_data="قرآن_استماع")]]))

    elif البيانات == "قرآن_قراء":
        نص = "🎙️ **أشهر قراء العالم الإسلامي:**\n\n"
        for i, قارئ in enumerate(القراء, 1):
            نص += f"{i}. {قارئ}\n"
        نص += "\nاختر القارئ للاستماع (قريباً)"
        await استعلام.edit_message_text(نص)

    elif البيانات == "قرآن_آية":
        await استعلام.edit_message_text(f"📅 **آية اليوم:**\n\n{random.choice(الايات)}\n\n🌟 صدق الله العظيم")

    elif البيانات == "قرآن_اذكار":
        await استعلام.edit_message_text(الاذكار, parse_mode="Markdown")

    elif البيانات == "قرآن_بحث":
        await استعلام.edit_message_text("🔍 **البحث في القرآن الكريم**\n\nأرسل لي كلمة تريد البحث عنها في القرآن\nمثال: الصبر - الرحمة - الجنة")

    elif البيانات == "قرآن_ادعية":
        ادعية = "🤲 **أدعية مختارة:**\n\n• اللهم إنك عفو تحب العفو فاعف عنا\n• ربنا آتنا في الدنيا حسنة وفي الآخرة حسنة وقنا عذاب النار\n• اللهم اهدني وسددني\n• يا حي يا قيوم برحمتك أستغيث\n• اللهم ارزقني علماً نافعاً ورزقاً طيباً"
        await استعلام.edit_message_text(ادعية)

    elif البيانات == "رجوع_قرآن":
        await قائمة_القرآن_تعديل(استعلام)

async def قائمة_القرآن_تعديل(استعلام):
    لوحة = [
        [InlineKeyboardButton("🎧 الاستماع للسور", callback_data="قرآن_استماع"),
         InlineKeyboardButton("📖 قراءة القرآن", callback_data="قرآن_قراءة")],
        [InlineKeyboardButton("🎙️ القراء", callback_data="قرآن_قراء"),
         InlineKeyboardButton("📅 آية اليوم", callback_data="قرآن_آية")],
        [InlineKeyboardButton("📿 الأذكار", callback_data="قرآن_اذكار"),
         InlineKeyboardButton("🔍 البحث", callback_data="قرآن_بحث")]
    ]
    await استعلام.edit_message_text("📖 **قسم القرآن الكريم**\nاختر ما تريد:", reply_markup=InlineKeyboardMarkup(لوحة))

# ========= التحميل =========
async def قائمة_التحميل(update: Update, context: ContextTypes.DEFAULT_TYPE):
    لوحة = [
        [InlineKeyboardButton("📺 يوتيوب", callback_data="تحميل_يوتيوب"), InlineKeyboardButton("🎵 تيك توك", callback_data="تحميل_تيك")],
        [InlineKeyboardButton("📸 انستقرام", callback_data="تحميل_انستا"), InlineKeyboardButton("👍 فيسبوك", callback_data="تحميل_فيس")],
        [InlineKeyboardButton("🐦 تويتر", callback_data="تحميل_تويتر")]
    ]
    await update.message.reply_text(
        "📥 **مركز التحميل العالمي - البوت الأسطوري**\n\n🚀 حمّل من أي منصة بضغطة زر:\n\n• 📺 يوتيوب - فيديو وصوت\n• 🎵 تيك توك - بدون علامة مائية\n• 📸 انستقرام - صور وفيديو وستوري\n• 👍 فيسبوك - فيديوهات\n• 🐦 تويتر - فيديوهات\n\n👇 **فقط أرسل رابط الفيديو الآن وسأحمله لك فوراً!**",
        reply_markup=InlineKeyboardMarkup(لوحة)
    )

# ========= الألعاب =========
async def قائمة_الالعاب(update: Update, context: ContextTypes.DEFAULT_TYPE):
    لوحة = [
        [InlineKeyboardButton("❌⭕ لعبة XO", callback_data="لعبة_xo"), InlineKeyboardButton("🔢 خمن الرقم", callback_data="لعبة_تخمين")],
        [InlineKeyboardButton("🧩 الألغاز", callback_data="لعبة_لغز"), InlineKeyboardButton("🎲 حظك اليوم", callback_data="لعبة_حظ")],
        [InlineKeyboardButton("⚔️ تحدي المعلومات", callback_data="لعبة_معلومات"), InlineKeyboardButton("🎯 ألعاب أكثر", callback_data="لعبة_المزيد")]
    ]
    await update.message.reply_text("🎮 **صالة الألعاب الأسطورية**\n\nاختر لعبتك المفضلة واستمتع!", reply_markup=InlineKeyboardMarkup(لوحة))

async def ازرار_الالعاب(update: Update, context: ContextTypes.DEFAULT_TYPE):
    استعلام = update.callback_query
    await استعلام.answer()
    البيانات = استعلام.data
    ايدي = استعلام.from_user.id

    if البيانات == "لعبة_تخمين":
        رقم = random.randint(1, 100)
        العاب_مؤقتة[ايدي] = رقم
        await استعلام.edit_message_text("🔢 **لعبة خمن الرقم**\n\nخمنت رقم من 1 إلى 100\nحاول تخمن الرقم! أرسل تخمينك في الشات 👇\n\n💡 سأقول لك أكبر أو أصغر")

    elif البيانات == "لعبة_لغز":
        الالغاز = [
            ("ما هو الشيء الذي كلما أخذت منه كبر؟ 🤔", "الحفرة"),
            ("ما هو الشيء الذي يمشي بلا رجلين ويبكي بلا عينين؟ 😢", "السحابة"),
            ("له وجه ولا يبكي، وله يد ولا يصفق؟ 🕐", "الساعة"),
            ("ما هو الشيء الذي له أسنان ولا يعض؟ 🪮", "المشط"),
            ("كلما زاد نقص؟ 🕳️", "العمر")
        ]
        سؤال, جواب = random.choice(الالغاز)
        العاب_مؤقتة[f"لغز_{ايدي}"] = جواب
        await استعلام.edit_message_text(f"🧩 **لغز أسطوري:**\n\n{سؤال}\n\n✍️ أرسل إجابتك في الشات!")

    elif البيانات == "لعبة_xo":
        لوحة = [[InlineKeyboardButton("⬜", callback_data=f"xo_{i}_{j}") for j in range(3)] for i in range(3)]
        await استعلام.edit_message_text("❌⭕ **لعبة XO الأسطورية**\n\nدورك ❌ - اختر مكان:", reply_markup=InlineKeyboardMarkup(لوحة))

    elif البيانات == "لعبة_حظ":
        نسبة = random.randint(1,100)
        رسائل = ["يومك أسطوري ومليء بالنجاح! 🌟","فرصة ذهبية قادمة لك اليوم! 💰","انتبه لقراراتك اليوم! ⚠️","شخص يفكر فيك الآن! 💭","ستسمع خبر سعيد قريباً! 🎉"]
        await استعلام.edit_message_text(f"🎲 **حظك اليوم:**\n\nنسبة الحظ: {نسبة}%\n{random.choice(رسائل)}\n\nجرب مرة أخرى غداً!")

    elif البيانات == "لعبة_معلومات":
        اسئلة = [
            ("ما هي عاصمة اليمن؟ 🇾🇪", "صنعاء"),
            ("كم عدد سور القرآن؟ 📖", "114"),
            ("ما هي أطول سورة في القرآن؟", "البقرة")
        ]
        س, ج = random.choice(اسئلة)
        العاب_مؤقتة[f"معلومة_{ايدي}"] = ج
        await استعلام.edit_message_text(f"⚔️ **تحدي المعلومات:**\n\n{س}\n\nأرسل إجابتك!")

    elif البيانات.startswith("xo_"):
        await استعلام.edit_message_text("❌ لعبت! دوري ⭕ الآن... قريباً سأضيف ذكاء اصطناعي يلعب ضدك! 🤖")

# ========= المالك =========
async def لوحة_المالك(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not هل_هو_المالك(update.effective_user):
        await update.message.reply_text("⛔ عذراً، هذه المنطقة مخصصة لمالك البوت فقط @wailabuMohammed")
        return
    لوحة = [
        [InlineKeyboardButton("📊 الإحصائيات", callback_data="مالك_احصائيات"), InlineKeyboardButton("📢 إذاعة للكل", callback_data="مالك_اذاعة")],
        [InlineKeyboardButton("👥 المستخدمين", callback_data="مالك_مستخدمين"), InlineKeyboardButton("⚙️ الإعدادات", callback_data="مالك_اعدادات")],
        [InlineKeyboardButton("🔄 إعادة تشغيل", callback_data="مالك_اعادة"), InlineKeyboardButton("📝 سجل", callback_data="مالك_سجل")]
    ]
    await update.message.reply_text("👑 **لوحة تحكم المالك الأسطوري - وائل أبو محمد**\n\nمرحباً بك يا مالك! تحكم كامل بالبوت:", reply_markup=InlineKeyboardMarkup(لوحة), parse_mode="Markdown")

# ========= معالجة الرسائل =========
async def معالج_النصوص(update: Update, context: ContextTypes.DEFAULT_TYPE):
    النص = update.message.text.strip()
    ايدي = update.effective_user.id

    if ايدي in العاب_مؤقتة and isinstance(العاب_مؤقتة[ايدي], int):
        الهدف = العاب_مؤقتة[ايدي]
        try:
            تخمين = int(النص)
            if تخمين == الهدف:
                await update.message.reply_text(f"🎉 ممتاز! إجابة صحيحة!\nالرقم كان {الهدف} يا أسطورة! 🔥")
                del العاب_مؤقتة[ايدي]
            elif تخمين < الهدف:
                await update.message.reply_text("🔼 الرقم أكبر! حاول مرة ثانية يا بطل!")
            else:
                await update.message.reply_text("🔽 الرقم أصغر! حاول مرة ثانية!")
            return
        except:
            pass

    for مفتاح in [f"لغز_{ايدي}", f"معلومة_{ايدي}"]:
        if مفتاح in العاب_مؤقتة:
            الجواب = العاب_مؤقتة[مفتاح]
            if الجواب.lower() in النص.lower() or النص.lower() in الجواب.lower():
                await update.message.reply_text("✅ إجابة صحيحة يا أسطورة! 🎉🔥\nأنت ذكي جداً!")
                del العاب_مؤقتة[مفتاح]
            else:
                await update.message.reply_text(f"❌ إجابة خاطئة! حاول مرة ثانية\n💡 تلميح: يبدأ بـ {الجواب[0]}...")
            return

    if "http" in النص or "tiktok.com" in النص or "youtu" in النص or "instagram.com" in النص or "facebook.com" in النص or "fb.watch" in النص:
        await update.message.reply_text(
            f"⏳ **تم استلام الرابط!**\n\n🔗 {النص}\n\n🚀 جاري التحميل بأعلى جودة...\n\nفي النسخة الحالية يتم تجهيز التحميل. تأكد من إضافة yt-dlp في ملف المتطلبات وسيتم الإرسال تلقائياً!\n\n📥 قريباً سأرسل لك الفيديو مباشرة بدون علامة مائية!"
        )
        return

    if "قرآن" in النص or "القران" in النص:
        await قائمة_القرآن(update, context)
    elif "تحميل" in النص:
        await قائمة_التحميل(update, context)
    elif "ألعاب" in النص or "العاب" in النص or "لعبة" in النص:
        await قائمة_الالعاب(update, context)
    elif "المالك" in النص or "لوحة" in النص:
        await لوحة_المالك(update, context)
    elif "دردشة" in النص:
        await update.message.reply_text("🧠 **الدردشة الذكية الأسطورية**\n\nأهلاً! أنا البوت الأسطوري، ذكاء اصطناعي يمني عربي 100%\nاسألني أي شيء وسأجيبك! 💬\n\nمثال: كيف حالك؟ - ما هي عاصمة اليمن؟ - احكي لي نكتة")
    else:
        ردود = [
            f"فهمتك يا غالي! قلت: {النص} 🧠\nأنا البوت الأسطوري جاهز أساعدك!",
            f"كلام جميل: {النص} 😊\nكيف أقدر أساعدك أكثر؟",
            f"يا هلا! {النص} - تفضل، أنا معك!",
            "أنا البوت الأسطوري العربي 100% 🇾🇪\n📖 قرآن - 🎮 ألعاب - 📥 تحميل - 🧠 دردشة\nاختر من القائمة تحت!",
        ]
        await update.message.reply_text(random.choice(ردود), reply_markup=لوحة_الرئيسية())

# ========= التشغيل الرئيسي =========
def تشغيل():
    if not التوكن:
        print("❌ خطأ: التوكن غير موجود! ضع TELEGRAM_BOT_TOKEN في Secrets")
        return
    تطبيق = Application.builder().token(التوكن).build()
    تطبيق.add_handler(CommandHandler("start", البداية))
    تطبيق.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, معالج_النصوص))
    تطبيق.add_handler(CallbackQueryHandler(ازرار_القرآن, pattern="^قرآن_|^تشغيل_|^رجوع_"))
    تطبيق.add_handler(CallbackQueryHandler(ازرار_الالعاب, pattern="^لعبة_|^xo_"))
    تطبيق.add_handler(CallbackQueryHandler(ازرار_القرآن, pattern="^تحميل_"))

    print("🚀 البوت الأسطوري العربي 100% اشتغل بنجاح!")
    print(f"👑 المالك: @wailabuMohammed")
    تطبيق.run_polling()

if __name__ == "__main__":
    تشغيل()
