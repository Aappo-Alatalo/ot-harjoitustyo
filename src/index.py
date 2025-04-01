from customtkinter import CTk
from views.NewUserView import NewUserView

class App:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_new_user_view()
    
    def _handle_name_confirm(self):
        print("User wants to confirm name")

    def _show_new_user_view(self):
        self._current_view = NewUserView(
            self._root,
            self._handle_name_confirm
        )
        self._current_view.pack()

window = CTk()
window.title("Trade Royale")
window.geometry("800x600")

app = App(window)
app.start()

window.mainloop()
