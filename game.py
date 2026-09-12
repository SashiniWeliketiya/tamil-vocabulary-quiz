import random
import tkinter as tk
from tkinter import messagebox

# Tamil Words Dataset (Without Grade 1 Label)
words = [
    {"tamil": "அணில்", "en": "Squirrel", "si": "ලේනා"},
    {"tamil": "ஆடு", "en": "Goat", "si": "එළුවා"},
    {"tamil": "இலை", "en": "Leaf", "si": "කොළය"},
    {"tamil": "ஈ", "en": "Fly", "si": "මැස්සා"},
    {"tamil": "உழவு", "en": "Ploughing", "si": "හාෑම"},
    {"tamil": "ஊசி", "en": "Needle", "si": "ඉඳිකටුව"},
    {"tamil": "எலி", "en": "Mouse", "si": "මීයා"},
    {"tamil": "ஏணி", "en": "Ladder", "si": "ඉණිමඟ"},
    {"tamil": "ஐந்து", "en": "Five", "si": "පහ"},
    {"tamil": "ஒன்று", "en": "One", "si": "එක"}
]

class TamilQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic Tamil Word Quiz 🌟")
        self.root.geometry("500x520")
        self.root.config(bg="#F0F4F8")
        
        self.lang = "si"  # Default
        self.current_question = 0
        self.score = 0
        self.questions = []

        self.show_language_selection()

    def show_language_selection(self):
        # Clear frame
        for widget in self.root.winfo_children():
            widget.destroy()

        # Welcome Card
        card = tk.Frame(self.root, bg="#FFFFFF", bd=0, highlightthickness=2, highlightbackground="#CBD5E1", padx=20, pady=20)
        card.pack(expand=True, fill="both", padx=30, pady=30)

        title = tk.Label(card, text="Tamil Word Quiz🎈", font=("Arial", 18, "bold"), bg="#FFFFFF", fg="#1E293B")
        title.pack(pady=15)

        sub = tk.Label(card, text="Select Mode / මාදිලිය තෝරන්න:", font=("Iskoola Pota", 12), bg="#FFFFFF", fg="#64748B")
        sub.pack(pady=10)

        # Mode 1: Sinhala
        btn_si = tk.Button(
            card, text="🇱🇰 සිංහල Mode", font=("Iskoola Pota", 13, "bold"), 
            bg="#3B82F6", fg="white", activebackground="#2563EB", activeforeground="white",
            width=18, height=2, bd=0, cursor="hand2", command=lambda: self.start_game("si")
        )
        btn_si.pack(pady=10)

        # Mode 2: English
        btn_en = tk.Button(
            card, text="🇬🇧 English Mode", font=("Arial", 12, "bold"), 
            bg="#10B981", fg="white", activebackground="#059669", activeforeground="white",
            width=18, height=2, bd=0, cursor="hand2", command=lambda: self.start_game("en")
        )
        btn_en.pack(pady=5)

    def start_game(self, lang):
        self.lang = lang
        self.score = 0
        self.current_question = 0
        self.questions = list(words)
        random.shuffle(self.questions)

        # Clear screen for quiz
        for widget in self.root.winfo_children():
            widget.destroy()

        self.setup_quiz_ui()

    def setup_quiz_ui(self):
        # Header Bar (Score Tracker)
        self.header_frame = tk.Frame(self.root, bg="#E2E8F0", height=40)
        self.header_frame.pack(fill="x")

        self.score_label = tk.Label(
            self.header_frame, text=f"⭐ Score: {self.score}", 
            font=("Arial", 12, "bold"), bg="#E2E8F0", fg="#0F172A"
        )
        self.score_label.pack(side="right", padx=15, pady=5)

        # Back Button
        btn_back = tk.Button(
            self.header_frame, text="🏠 Home", font=("Arial", 9, "bold"),
            bg="#94A3B8", fg="white", bd=0, command=self.show_language_selection
        )
        btn_back.pack(side="left", padx=10, pady=5)

        # Question Card
        self.card = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=15, highlightthickness=1, highlightbackground="#E2E8F0")
        self.card.pack(fill="both", expand=True, padx=20, pady=15)

        self.q_num_label = tk.Label(self.card, text="", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#64748B")
        self.q_num_label.pack(anchor="w")

        self.quest_label = tk.Label(
            self.card, text="", font=("Iskoola Pota", 15, "bold"), 
            bg="#FFFFFF", fg="#1E293B", wraplength=400, pady=10
        )
        self.quest_label.pack()

        # Option Buttons Grid
        self.btn_frame = tk.Frame(self.card, bg="#FFFFFF")
        self.btn_frame.pack(pady=10)

        self.option_btns = []
        for i in range(4):
            btn = tk.Button(
                self.btn_frame, text="", font=("Nirmala UI", 15, "bold"), 
                width=16, bg="#F1F5F9", fg="#0F172A", activebackground="#CBD5E1",
                bd=1, relief="solid", cursor="hand2", pady=5,
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(pady=6)
            self.option_btns.append(btn)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            self.q_data = self.questions[self.current_question]
            
            # Format display based on language
            if self.lang == "si":
                meaning = self.q_data["si"]
                prompt = f"'{meaning}' කියන්නේ දෙමළෙන් මොකක්ද?"
            else:
                meaning = self.q_data["en"]
                prompt = f"What is '{meaning}' in Tamil?"

            self.q_num_label.config(text=f"Question {self.current_question + 1}/{len(self.questions)}")
            self.quest_label.config(text=prompt)
            self.score_label.config(text=f"⭐ Score: {self.score}")

            # Options creation
            self.options = [self.q_data['tamil']]
            while len(self.options) < 4:
                w = random.choice(words)['tamil']
                if w not in self.options:
                    self.options.append(w)
            random.shuffle(self.options)

            for i, opt in enumerate(self.options):
                self.option_btns[i].config(text=opt, state=tk.NORMAL, bg="#F1F5F9", fg="#0F172A")
        else:
            self.finish_game()

    def check_answer(self, idx):
        selected = self.options[idx]
        correct = self.q_data['tamil']

        if selected == correct:
            self.score += 10
            messagebox.showinfo("Awesome! 🎉", "✅ Correct Answer! Great Job! 🌟")
        else:
            messagebox.showerror("Oops! ❌", f"Wrong choice!\nCorrect answer was: {correct}")

        self.current_question += 1
        self.next_question()

    def finish_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        card = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        card.pack(expand=True, fill="both", padx=30, pady=30)

        lbl = tk.Label(card, text="🏆 Game Completed! 🏆", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#D97706")
        lbl.pack(pady=10)

        score_lbl = tk.Label(card, text=f"Total Score: {self.score} / 100", font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#1E293B")
        score_lbl.pack(pady=10)

        btn_restart = tk.Button(
            card, text="Play Again 🔄", font=("Arial", 11, "bold"),
            bg="#3B82F6", fg="white", bd=0, padx=15, pady=8, cursor="hand2",
            command=self.show_language_selection
        )
        btn_restart.pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = TamilQuizApp(root)
    root.mainloop()