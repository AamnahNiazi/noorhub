# 🌙 NoorHub — Minimalist Islamic Knowledge Web Application

An elegant, high-end Islamic Hub built entirely in **100% Pure Python** using the **Reflex** framework. This application blends clean engineering principles with a premium, minimalist design system, combining fluid interaction physics with robust state-driven backend logic.

---

## ✨ Features

### 1. Interactive Quiz Engine
- **State-Driven Progression:** Managed via a robust backend Python state controller (`QuizState`) ensuring seamless state tracking without manual page refreshes.
- **Instant Visual Validation:** Dynamic UI color shifting upon selection—glowing **Sage Green** for correct answers and **Soft Pastel Pink** for incorrect selections.
- **Dynamic Score Tracking:** Real-time analytics displaying cumulative scores, progression percentages, and a comprehensive performance summary upon completion.

### 2. Daily Verse & Hadith Module
- **Fluid Revelation:** Clean, typography-focused display cards presenting daily curated Quranic verses and authentic Hadiths.
- **Interactive Copy & Share:** Seamless clipboard integrations for sharing text elegantly.

### 3. Modular Prayer Times Utility
- **Grid Layout Architecture:** Crisp, thin-bordered modular panels tracking daily prayer timings.
- **Real-time Status Highlight:** Visual indicator showing the active or upcoming prayer based on systemic tracking.

---

## 🎨 Design System & Aesthetics

The application adheres to a high-end, premium minimalist aesthetic inspired by modern layout designs.

- **Canvas Base:** Deep Charcoal/Black (`#121212`) to allow pastel highlights to radiate with maximum contrast.
- **Primary Accent (Soft Pastel Pink - `#F3C6C6`):** Applied to high-intent actions, interactive nodes, active selection states, and error indicators.
- **Secondary Accent (Sage/Light Green - `#A9DFBF`):** Applied to progression bars, successful validations, and peaceful calming indicators.
- **Borders:** Ultra-thin, low-opacity borders (`1px solid rgba(255, 255, 255, 0.08)`) establishing a crisp, modern grid appearance with absolute layout consistency.
- **Motion Dynamics:** Utilizes Reflex's advanced transition properties to achieve buttery-smooth `scale`, `opacity`, and `transform` behaviors, mimicking premium GSAP/Framer Motion timelines.

---

## 🚀 Technical Stack

- **Frontend & Backend Framework:** [Reflex](https://reflex.dev/) (Pure Python web framework compiling directly to a highly optimized Next.js/React frontend application)
- **Styling Engine:** Tailwind-driven inline parameters exposed natively via Reflex UI primitives
- **State Management:** Native Reflex Delta-state reflection engine

---

## 📂 Project Architecture

The codebase follows a strictly modular, decoupled architectural pattern ensuring structural clean code and testability:

```text
noorhub/
│
├── assets/                  # Static assets, custom local SVGs, fonts
├── noorhub/
│   ├── __init__.py          # Project initialization
│   ├── components/          # Reusable structural UI primitives
│   │   ├── navbar.py        # Minimal header configuration
│   │   ├── prayer_panel.py  # Grid layout for prayer tracking
│   │   └── verse_card.py    # Typographic display panels
│   │
│   ├── states/              # Core business logic and state engines
│   │   └── quiz_state.py    # Pure Python logic handling quiz telemetry
│   │
│   ├── views/               # Major layout view definitions
│   │   └── quiz_view.py     # Main interactive quiz interface
│   │
│   └── noorhub.py           # Core application root and page routing
│
└── rxconfig.py              # Reflex ecosystem configuration file
🛠️ Installation & Setup
Ensure you have Python 3.8+ installed on your system.

1. Clone the Repository
Bash
git clone [https://github.com/yourusername/noorhub.git](https://github.com/yourusername/noorhub.git)
cd noorhub
2. Set Up a Virtual Environment
Bash
# Windows
python -m venv venv
.\\venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install --upgrade pip
pip install reflex
4. Initialize and Run the Application
Bash
# Initialize Reflex project configurations
reflex init

# Boot the development server (runs backend and compiles Next.js frontend)
reflex run
Once compilation finishes, navigate to http://localhost:3000 inside your web browser to interact with the application.

🧪 Engineering Highlights
Declarative Python State Control
The dynamic quiz feedback logic bypasses raw DOM manipulation entirely, utilizing Reflex reactive assignments:

Python
import reflex as rx

class QuizState(rx.State):
    questions: list[dict] = [
        {
            "question": "What is the first month of the Islamic calendar?",
            "options": ["Ramadan", "Muharram", "Shawwal", "Rabi al-Awwal"],
            "correct": 1
        }
    ]
    current_index: int = 0
    selected_option: int = -1
    score: int = 0
    is_answered: bool = False

    def select_answer(self, option_index: int):
        if self.is_answered:
            return
        self.selected_option = option_index
        self.is_answered = True
        if option_index == self.questions[self.current_index]["correct"]:
            self.score += 1

    def next_question(self):
        self.selected_option = -1
        self.is_answered = False
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1
📝 License
Distributed under the MIT License. See LICENSE for more information.