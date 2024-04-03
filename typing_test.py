import tkinter as tk
from tkinter import messagebox
import time
import random
import string

class TypingTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")
        
        self.typing_game = TypingTest()
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to the typing test!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.difficulty_label = tk.Label(self.root, text="Select Difficulty:", font=("Helvetica", 12))
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("beginner")  
        self.difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "beginner", "amateur", "pro")
        self.difficulty_menu.pack()

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=5)

        self.typing_area_label = tk.Label(self.root, text="Type the given text:", font=("Helvetica", 12))
        self.typing_area_label.pack_forget()  

        self.sentence_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.sentence_label.pack_forget()  

        self.typing_area = tk.Entry(self.root, font=("Helvetica", 12), width=50)
        self.typing_area.pack_forget()  

        self.typing_area.bind("<Return>", self.process_input)  

    def start_typing_test(self):
        self.difficulty_label.pack_forget() 
        self.difficulty_menu.pack_forget()  
        self.start_button.pack_forget()  
        self.typing_area_label.pack() 

        
        sentence = self.typing_game.get_random_sentence(self.difficulty_var.get())
        self.sentence_label.config(text=sentence)
        self.sentence_label.pack()  

        self.typing_area.pack()  
        self.typing_area.delete(0, tk.END)  
        self.typing_area.focus()  

       
        self.typing_game.start_time = time.time()

    def process_input(self, event):
        user_input = self.typing_area.get()

        
        elapsed_time, wpm, accuracy = self.typing_game.calculate_results(user_input, self.sentence_label.cget("text"))

        
        result_message = f"Time taken: {elapsed_time:.2f} seconds\n"
        result_message += f"Words per minute: {wpm:.2f} WPM\n"
        result_message += f"Accuracy: {accuracy:.2f}%"
        messagebox.showinfo("Results", result_message)

        
        self.difficulty_label.pack()  
        self.difficulty_menu.pack() 
        self.start_button.pack()  
        self.typing_area_label.pack_forget()  
        self.sentence_label.pack_forget()  
        self.typing_area.pack_forget()  

class TypingTest:
    def __init__(self):
        self.sentences = {
            "beginner": [
                "The quick brown fox jumps over the lazy dog.",
                "Jackdaws love my big sphinx of quartz.",
                "How razorback-jumping frogs can level six piqued gymnasts!",
                "Pack my box with five dozen liquor jugs.",
                "The five boxing wizards jump quickly.",
                "Jinxed wizards pluck ivy from the big quilt."
            ],
            "amateur": [
                "Amazingly few discotheques provide jukeboxes.",
                "Sixty zippers were quickly picked from the woven jute bag.",
                "Crazy Frederick bought many very exquisite opal jewels.",
                "Back in June we delivered oxygen equipment of the same size.",
                "My girl wove six dozen plaid jackets before she quit.",
                "Quizzical twins proved my hijack-bug fix."
            ],
            "pro": [
                "Big July earthquakes confound zany experimental vow.",
                "The five boxing wizards jump quickly.",
                "Jackdaws love my big sphinx of quartz.",
                "Crazy Frederick bought many very exquisite opal jewels.",
                "Woven silk pyjamas exchanged for blue quartz.",
                "Jumbled haze of TV quiz show gives no warmth."
            ]
        }

    def get_random_sentence(self, difficulty):
        return random.choice(self.sentences[difficulty])

    def calculate_results(self, user_input, text):

        elapsed_time = time.time() - self.start_time

        
        words_typed = len(user_input.split())
        wpm = words_typed / (elapsed_time / 60)

        
        correct_characters = sum(1 for x, y in zip(user_input, text) if x == y)
        accuracy = (correct_characters / len(text)) * 100

        return elapsed_time, wpm, accuracy

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestGUI(root)
    root.mainloop()
