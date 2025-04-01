from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkEntry

class NewUserView:
    def __init__(self, root, handle_confirm_name):
        self._root = root
        self._handle_confirm_name = handle_confirm_name
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = CTkFrame(master=self._root)

        self._frame.grid_rowconfigure(0, weight=0)
        self._frame.grid_rowconfigure(1, weight=0)
        self._frame.grid_rowconfigure(2, weight=0)
        self._frame.grid_columnconfigure(0, weight=1) 

        gametitle = CTkLabel(master=self._frame, text="TRADE ROYALE", font=('',48))
        label = CTkLabel(master=self._frame, text="Select a name (cannot be changed later)")
        name_input = CTkEntry(master=self._frame, width=300, corner_radius=2)
        button = CTkButton(
            master=self._frame,
            text="I am sure this name is good",
            command=self._handle_confirm_name
        )

        gametitle.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")
        label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        name_input.grid(row=2, column=0, padx=10, pady=3, sticky="ew")
        button.grid(row=3, column=0, padx=10, pady=3, sticky="ew")
