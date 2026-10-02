import streamlit as st
import pandas as pd
import base64

# выбор места
# бюджет
# отели и маршрут
# тип отдыха (тур)

# ============================================================
# ИЗМЕНЕНО (п. 4): заменён фон fly.png -> nature_bg.png
# (своё изображение, сгенерированное специально для проекта;
#  файл nature_bg.png должен лежать в одной папке с main.py)
# ============================================================

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


try:
    bin_str = get_base64_of_bin_file('nature_bg.png')  # ИЗМЕНЕНО (п. 4)

    st.html(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .st-key-booking {{
        background-color: #ffffff !important;
        padding: 40px !important;
        border-radius: 24px !important;
        box-shadow: 0px 12px 40px rgba(0,0,0,0.25) !important;
        max-width: 600px !important;
        margin: 40px auto !important;
        border: none !important;
    }}

    .st-key-booking p,
    .st-key-booking label,
    .st-key-booking h1,
    .st-key-booking h2,
    .st-key-booking h3 {{
        color: #111827 !important;
        font-weight: 500 !important;
    }}
    </style>
    """)

except FileNotFoundError:
    st.warning("Файл с фоновым изображением не найден. Проверь имя файла.")

with st.container(border=True, key="booking"):

    st.title("🌏 Собери свое путешествие")

    # ========================================================
    # ИЗМЕНЕНО (п. 2): добавлена новая страна «Япония»
    # в список st.selectbox
    # ========================================================
    country = st.selectbox(
        "Куда поедем?",
        [
            "Франция",
            "Италия",
            "Россия",
            "Япония"          # <-- ИЗМЕНЕНО (п. 2)
        ]
    )

    # Города для каждой страны
    cities = {
        "Франция": [
            [48.8566, 2.3522],  # Париж
        ],

        "Италия": [
            [41.8919, 12.5113],  # Рим
        ],

        "Россия": [
            [55.7558, 37.6173],  # Москва
        ],

        # ИЗМЕНЕНО (п. 2): координаты Токио
        # (координаты можно скопировать на Яндекс.Картах:
        #  ПКМ по точке -> «Координаты»)
        "Япония": [
            [35.6762, 139.6503],  # Токио
        ]
    }

    map_data = pd.DataFrame(
        cities[country],
        columns=["lat", "lon"]
    )

    st.map(map_data)

    budget = st.slider(
        "Какой бюджет?",
        10000,
        500000,
        100000,
        5000
    )

    # ========================================================
    # ИЗМЕНЕНО (п. 1): добавлен новый тип отдыха «Природа»
    # в список st.selectbox
    # ========================================================
    type_of_trip = st.selectbox(
        "Кукой тип отдыха предпочитаешь?",
        [
            "Море",
            "История",
            "Еда",
            "Природа"        # <-- ИЗМЕНЕНО (п. 1)
        ]
    )

    button = st.button("Предложить путешествие")

    if button:
        if budget < 100000:
            level = "Эконом"
        elif budget > 300000:
            level = "Люкс"
        else:
            level = "Стандарт"
        st.info(f"{country} | {type_of_trip} | {level}")
        if country == "Франция":

            if type_of_trip == "Еда":
                st.success(
                    "🥐 Французская кухня: луковый суп, "
                    "утиная ножка конфи, киш Лорен, крем-брюле."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Ницца, Канны, "
                    "Лазурный берег и Биарриц."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏰 Исторический отдых: замки Луары, "
                    "Мон-Сен-Мишель и музеи Парижа."
                )

            # ИЗМЕНЕНО (п. 1): новая ветка if/elif для типа «Природа»
            elif type_of_trip == "Природа":
                st.success(
                    "🌲 Природа Франции: Прованс и лавандовые поля, "
                    "Альпы, национальный парк Вануаз и ущелье Вердон."
                )

        elif country == "Италия":

            if type_of_trip == "Еда":
                st.success(
                    "🍕 Итальянская кухня: пицца, паста "
                    "карбонара, лазанья и джелато."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Амальфитанское побережье, "
                    "Лигурия и пляжи Сардинии."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏛️ Исторический отдых: Рим, Колизей "
                    "и Флоренция."
                )

            # ИЗМЕНЕНО (п. 1): новая ветка if/elif для типа «Природа»
            elif type_of_trip == "Природа":
                st.success(
                    "⛰️ Природа Италии: Доломитовые Альпы, "
                    "озера Комо и Гарда, национальный парк Чинкве-Терре."
                )

        elif country == "Россия":

            if type_of_trip == "Еда":
                st.success(
                    "🥞 Русская кухня: блины с икрой, "
                    "пельмени, борщ и бефстроганов."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Сочи, Анапа "
                    "и побережье Калининграда."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏛️ Исторический отдых: Эрмитаж, "
                    "Москва и города Золотого кольца."
                )

            # ИЗМЕНЕНО (п. 1): новая ветка if/elif для типа «Природа»
            elif type_of_trip == "Природа":
                st.success(
                    "🏔️ Природа России: Кавказ, Алтай, "
                    "Байкал и Камчатка — гейзеры и вулканы."
                )

        # ====================================================
        # ИЗМЕНЕНО (п. 3): новый блок для страны «Япония»
        # с информацией по ВСЕМ типам отдыха
        # (Море, История, Еда, Природа)
        # ====================================================
        elif country == "Япония":

            if type_of_trip == "Еда":
                st.success(
                    "🍣 Японская кухня: суши и сашими, рамен, "
                    "окономияки, такояки и матча-десерты."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: пляжи Окинавы, "
                    "острова Амами и сёрфинг в Тибе."
                )

            elif type_of_trip == "История":
                st.success(
                    "⛩️ Исторический отдых: Киото и его храмы, "
                    "Хиросима, замок Химэдзи и старый Эдо в Токио."
                )

            elif type_of_trip == "Природа":
                st.success(
                    "🗻 Природа Японии: гора Фудзи, "
                    "бамбуковая роща Арасияма, парк Кандайко и каньон Обиоке."
                )

        st.subheader("🌟 Что дальше?")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "🏨 Подобрать отель",
                "https://ostrovok.ru/hotel/",
                use_container_width=True
            )

        with col2:
            st.link_button(
                "✈️ Подобрать маршрут",
                "https://www.aviasales.ru/",
                use_container_width=True
            )
