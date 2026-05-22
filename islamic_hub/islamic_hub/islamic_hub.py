"""
Islamic Knowledge Hub - Reflex Web Application
A pure Python full-stack application utilizing the Reflex framework.
Compiles to a high-end, responsive Next.js frontend with robust state tracking.
"""

import reflex as rx

# ==========================================
# MOCK DATA CONFIGURATIONS
# ==========================================

QUIZ_DATA = [
    {
        "question": "In which Islamic month was the Holy Qur'an first revealed to Prophet Muhammad (PBUH)?",
        "options": ["Dhul-Hijjah", "Muharram", "Ramadan", "Rajab"],
        "correct": "Ramadan",
        "explanation": "The Qur'an was first revealed in the month of Ramadan during the Night of Decree (Laylat al-Qadr)."
    },
    {
        "question": "Which Prophet is known for his immense patience during severe illness and hardships?",
        "options": ["Prophet Yusuf (AS)", "Prophet Ayyub (AS)", "Prophet Yunus (AS)", "Prophet Musa (AS)"],
        "correct": "Prophet Ayyub (AS)",
        "explanation": "Prophet Ayyub (Alayhi al-Salam) is renowned in Islamic tradition for his paradigm-shifting patience and unwavering faith through profound loss and illness."
    },
    {
        "question": "What is the primary spiritual objective of fasting (Sawm) as explicitly stated in Surah Al-Baqarah?",
        "options": ["To experience hunger", "To attain Taqwa (God-consciousness)", "To practice physical detox", "To unite the community"],
        "correct": "To attain Taqwa (God-consciousness)",
        "explanation": "Surah Al-Baqarah (2:183) states that fasting is prescribed so that you may attain Taqwa (righteousness/God-consciousness)."
    }
]

DAILY_REFLECTIONS = {
    "verse_arabic": "إِنَّ مَعَ الْعُسْرِ يُسْرًا",
    "verse_english": "For indeed, with hardship [will be] ease.",
    "verse_reference": "Surah Ash-Sharh [94:6]",
    "hadith_text": "\"The strong believer is better and more beloved to Allah than the weak believer, while there is good in both. Cherish that which gives you benefit, and seek help from Allah and do not lose heart.\"",
    "hadith_reference": "Sahih Muslim"
}

PRAYER_DATA = [
    {"name": "Fajr", "time": "04:12 AM", "status": "Completed"},
    {"name": "Dhuhr", "time": "12:24 PM", "status": "Completed"},
    {"name": "Asr", "time": "03:54 PM", "status": "Completed"},
    {"name": "Maghrib", "time": "07:12 PM", "status": "Current"},
    {"name": "Isha", "time": "08:42 PM", "status": "Upcoming"},
]


# ==========================================
# APPLICATION STATE MANAGEMENT (PYTHON RECONCILIATION)
# ==========================================

class AppState(rx.State):
    """Manages full application reactivity, quiz indices, user answers, and scoring metrics."""
    
    # Quiz State Variables
    current_index: int = 0
    score: int = 0
    selected_option: str = ""
    is_answered: bool = False
    quiz_complete: bool = False
    
    @rx.var
    def current_question(self) -> dict:
        """Dynamically computes and fetches the active question payload."""
        if self.current_index < len(QUIZ_DATA):
            return QUIZ_DATA[self.current_index]
        return {"question": "", "options": [], "correct": "", "explanation": ""}

    @rx.var
    def total_questions(self) -> int:
        """Returns total question ceiling."""
        return len(QUIZ_DATA)

    def handle_select_option(self, option: str):
        """Processes the user's choice and locks the interactive state."""
        if not self.is_answered:
            self.selected_option = option
            self.is_answered = True
            if option == self.current_question["correct"]:
                self.score += 1

    def next_question(self):
        """Advances the application state index or routes to final tally board."""
        if self.current_index + 1 < len(QUIZ_DATA):
            self.current_index += 1
            self.selected_option = ""
            self.is_answered = False
        else:
            self.quiz_complete = True

    def reset_quiz(self):
        """Flushes state tree values back to initial baseline configurations."""
        self.current_index = 0
        self.score = 0
        self.selected_option = ""
        self.is_answered = False
        self.quiz_complete = False


# ==========================================
# STYLE DEFINITIONS & DESIGN SYSTEM
# ==========================================

STYLES = {
    "canvas_bg": "#121214",
    "card_bg": "#1A1A1E",
    "accent_pink": "#F3C6C6",
    "accent_sage": "#A9DFBF",
    "border_subtle": "1px solid rgba(255, 255, 255, 0.08)",
    "text_muted": "rgba(255, 255, 255, 0.6)",
    "transition_smooth": "all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)"
}


def card_wrapper(*children, **kwargs) -> rx.Component:
    """Design System Layout Primitive for standard structural content grids."""
    return rx.vstack(
        *children,
        background_color=STYLES["card_bg"],
        border=STYLES["border_subtle"],
        border_radius="16px",
        padding="24px",
        width="100%",
        align_items="stretch",
        spacing="4",
        **kwargs
    )


# ==========================================
# REUSABLE FRONTEND COMPONENTS
# ==========================================

def header_component() -> rx.Component:
    """Renders the global application navigation and branding landscape."""
    return rx.flex(
        rx.vstack(
            rx.heading("ILM HUB", size="6", color="#FFFFFF", font_weight="800", letter_spacing="0.1em"),
            rx.text("Islamic Knowledge & Daily Reflection Portal", color=STYLES["accent_pink"], font_size="13px", font_weight="500"),
            spacing="1"
        ),
        rx.badge(
            "AL-KHAWARIZMI V1.0",
            variant="outline",
            color_scheme="pink",
            border_radius="8px",
            padding_x="12px",
            padding_y="4px"
        ),
        width="100%",
        justify="between",
        align="center",
        border_bottom=STYLES["border_subtle"],
        padding_y="20px",
        margin_bottom="12px"
    )


def prayer_panel() -> rx.Component:
    """Renders modular tracking grid for daily prayer sequences."""
    return card_wrapper(
        rx.hstack(
            rx.icon("clock", color=STYLES["accent_pink"], size=20),
            rx.heading("Prayer Timings & Daily Track", size="4", color="#FFFFFF", font_weight="600"),
            spacing="2",
            margin_bottom="8px"
        ),
        rx.grid(
            *[
                rx.flex(
                    rx.text(p["name"], font_weight="600", color="#FFFFFF", font_size="14px"),
                    rx.text(p["time"], font_size="13px", color=STYLES["text_muted"]),
                    rx.badge(
                        p["status"],
                        color_scheme="green" if p["status"] == "Completed" else ("pink" if p["status"] == "Current" else "gray"),
                        variant="soft" if p["status"] == "Current" else "surface",
                        size="1"
                    ),
                    direction="column",
                    justify="between",
                    align="start",
                    background_color="rgba(255, 255, 255, 0.02)",
                    border=f"1px solid {STYLES['accent_pink']}40" if p["status"] == "Current" else STYLES["border_subtle"],
                    padding="16px",
                    border_radius="12px",
                    height="110px",
                    transition=STYLES["transition_smooth"],
                    _hover={"transform": "translateY(-2px)", "background_color": "rgba(255, 255, 255, 0.04)"}
                )
                for p in PRAYER_DATA
            ],
            columns=rx.breakpoints(initial="2", sm="3", md="5"),
            spacing="4",
            width="100%"
        )
    )


def reflection_panel() -> rx.Component:
    """Generates layout elements displaying Ayat and Hadith elements side-by-side."""
    return rx.grid(
        # Quranic Verse Container
        card_wrapper(
            rx.hstack(
                rx.icon("book-open", color=STYLES["accent_pink"], size=18),
                rx.text("DAILY QURANIC VERSE", font_size="12px", font_weight="700", letter_spacing="0.05em", color=STYLES["accent_pink"]),
                spacing="2"
            ),
            rx.text(
                DAILY_REFLECTIONS["verse_arabic"],
                font_family="Amiri, Georgia, serif",
                font_size="24px",
                color=STYLES["accent_sage"],
                text_align="right",
                width="100%",
                margin_y="8px"
            ),
            rx.text(f"\"{DAILY_REFLECTIONS['verse_english']}\"", font_size="15px", italic=True, color="#FFFFFF"),
            rx.text(DAILY_REFLECTIONS["verse_reference"], font_size="12px", color=STYLES["text_muted"], text_align="right"),
            justify_content="between"
        ),
        # Hadith Container
        card_wrapper(
            rx.hstack(
                rx.icon("heart", color=STYLES["accent_pink"], size=18),
                rx.text("PROPHETIC TRADITION (HADITH)", font_size="12px", font_weight="700", letter_spacing="0.05em", color=STYLES["accent_pink"]),
                spacing="2"
            ),
            rx.text(
                DAILY_REFLECTIONS["hadith_text"],
                font_size="14.5px",
                line_height="1.6",
                color="#FFFFFF",
                margin_y="auto"
            ),
            rx.text(DAILY_REFLECTIONS["hadith_reference"], font_size="12px", color=STYLES["text_muted"], text_align="right")
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="4",
        width="100%"
    )


def quiz_option_button(option: str) -> rx.Component:
    """Renders highly reactive, context-aware state validation choices."""
    
    # Python-side mapping translating conditional variables directly into runtime dynamic styling configurations
    is_correct_choice = (option == AppState.current_question["correct"])
    is_this_selected = (option == AppState.selected_option)
    
    border_color = rx.cond(
        AppState.is_answered,
        rx.cond(is_correct_choice, STYLES["accent_sage"], rx.cond(is_this_selected, STYLES["accent_pink"], "rgba(255, 255, 255, 0.08)")),
        rx.cond(is_this_selected, STYLES["accent_pink"], "rgba(255, 255, 255, 0.08)")
    )
    
    bg_color = rx.cond(
        AppState.is_answered,
        rx.cond(is_correct_choice, "rgba(169, 223, 191, 0.1)", rx.cond(is_this_selected, "rgba(243, 198, 198, 0.1)", "transparent")),
        "transparent"
    )

    return rx.button(
        rx.hstack(
            rx.text(option, font_weight="500", font_size="14px", color="#FFFFFF"),
            rx.spacer(),
            rx.cond(
                AppState.is_answered,
                rx.cond(
                    is_correct_choice,
                    rx.icon("check-circle-2", color=STYLES["accent_sage"], size=18),
                    rx.cond(is_this_selected, rx.icon("x-circle", color=STYLES["accent_pink"], size=18), rx.fragment())
                ),
                rx.fragment()
            ),
            width="100%",
            align_items="center"
        ),
        width="100%",
        height="54px",
        padding_x="20px",
        background_color=bg_color,
        border=f"1px solid {border_color}",
        border_radius="12px",
        cursor=rx.cond(AppState.is_answered, "not-allowed", "pointer"),
        transition=STYLES["transition_smooth"],
        _hover={
            "transform": rx.cond(AppState.is_answered, "none", "translateX(4px)"),
            "border_color": rx.cond(AppState.is_answered, border_color, STYLES["accent_pink"]),
            "background_color": rx.cond(AppState.is_answered, bg_color, "rgba(255, 255, 255, 0.02)")
        },
        on_click=AppState.handle_select_option(option)
    )


def quiz_panel() -> rx.Component:
    """Renders core quiz interface module containing runtime execution logic frames."""
    return card_wrapper(
        # Header Layer tracking active indexing metrics
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.icon("help-circle", color=STYLES["accent_pink"], size=20),
                    rx.heading("Islamic Knowledge Challenge", size="4", color="#FFFFFF", font_weight="600"),
                    spacing="2"
                ),
                rx.text(
                    f"Question {AppState.current_index + 1} of {AppState.total_questions}", 
                    color=STYLES["text_muted"], 
                    font_size="13px"
                ),
                align_items="start"
            ),
            rx.spacer(),
            rx.box(
                rx.text(f"Score: {AppState.score}/{AppState.total_questions}", color=STYLES["accent_sage"], font_weight="700", font_size="14px"),
                background_color="rgba(169, 223, 191, 0.1)",
                padding_x="14px",
                padding_y="6px",
                border_radius="8px",
                border=f"1px solid {STYLES['accent_sage']}30"
            ),
            width="100%",
            align_items="center"
        ),
        
        # Linear dynamic tracking progress element
        rx.progress(
            value=((AppState.current_index + rx.cond(AppState.is_answered, 1, 0)) / AppState.total_questions) * 100,
            color_scheme="pink",
            size="1",
            border_radius="2px",
            background_color="rgba(255, 255, 255, 0.04)"
        ),
        
        # Display Core Conditional Interactive UI Branches
        rx.cond(
            AppState.quiz_complete,
            # Complete Terminal UI Layout Block
            rx.vstack(
                rx.icon("trophy", color=STYLES["accent_sage"], size=44, stroke_width=1.5),
                rx.heading("Assessment Concluded", size="5", color="#FFFFFF"),
                rx.text(
                    f"You achieved a final metric calculation of {AppState.score} correct selections out of {AppState.total_questions} items.",
                    color=STYLES["text_muted"],
                    font_size="14px",
                    text_align="center"
                ),
                rx.button(
                    "Restart Core Quiz Engine",
                    on_click=AppState.reset_quiz,
                    background_color="transparent",
                    border=f"1px solid {STYLES['accent_pink']}",
                    color=STYLES["accent_pink"],
                    padding_x="24px",
                    height="40px",
                    border_radius="8px",
                    _hover={"background_color": f"{STYLES['accent_pink']}15", "transform": "scale(0.98)"},
                    transition=STYLES["transition_smooth"],
                    margin_top="12px"
                ),
                spacing="4",
                align_items="center",
                padding_y="32px"
            ),
            
            # Interactive Core Testing UI Layout Block
            rx.vstack(
                rx.text(
                    AppState.current_question["question"], 
                    font_size="16px", 
                    font_weight="500", 
                    color="#FFFFFF", 
                    line_height="1.5",
                    margin_y="12px"
                ),
                rx.vstack(
                    rx.foreach(
                        AppState.current_question["options"],
                        quiz_option_button
                    ),
                    width="100%",
                    spacing="3"
                ),
                # Micro-feedback explanations injected dynamically following interaction steps
                rx.cond(
                    AppState.is_answered,
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("info", size=14, color=STYLES["accent_sage"]),
                                    rx.text("Contextual Knowledge Insight", font_size="12px", font_weight="700", color=STYLES["accent_sage"], letter_spacing="0.05em"),
                                    spacing="2"
                                ),
                                rx.text(AppState.current_question["explanation"], font_size="13.5px", color="#FFFFFF", line_height="1.5"),
                                align_items="start",
                                spacing="2"
                            ),
                            background_color="rgba(255, 255, 255, 0.02)",
                            border_left=f"3px solid {STYLES['accent_sage']}",
                            padding="16px",
                            border_radius="0 12px 12px 0",
                            width="100%",
                            margin_top="8px"
                        ),
                        rx.button(
                            rx.hstack(
                                rx.text("Advance Next Challenge"),
                                rx.icon("arrow-right", size=16),
                                align_items="center"
                            ),
                            on_click=AppState.next_question,
                            background_color=STYLES["accent_pink"],
                            color=STYLES["canvas_bg"],
                            font_weight="600",
                            padding_x="24px",
                            height="44px",
                            border_radius="10px",
                            align_self="end",
                            margin_top="12px",
                            _hover={"opacity": "0.9", "transform": "translateY(-1px)"},
                            transition=STYLES["transition_smooth"]
                        ),
                        width="100%",
                        spacing="4"
                    ),
                    rx.fragment()
                ),
                width="100%",
                align_items="stretch",
                spacing="2"
            )
        )
    )


# ==========================================
# BASE ENTRY CONFIGURATIONS
# ==========================================

def index() -> rx.Component:
    """Compiles the core dashboard architecture blueprint."""
    return rx.box(
        rx.container(
            rx.vstack(
                header_component(),
                prayer_panel(),
                reflection_panel(),
                quiz_panel(),
                spacing="6",
                padding_bottom="64px",
                width="100%"
            ),
            size="3"
        ),
        background_color=STYLES["canvas_bg"],
        min_height="100vh",
        width="100%",
        font_family="system-ui, -apple-system, sans-serif"
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        radius="large"
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Amiri&display=swap"
    ]
)
app.add_page(index, route="/", title="Islamic Knowledge Hub")