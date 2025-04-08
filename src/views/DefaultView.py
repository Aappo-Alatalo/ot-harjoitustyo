from tkinter import ttk


class DefaultView:
    def __init__(self, root, show_buy_view):
        self._root = root
        self._show_buy_view = show_buy_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        viewtitle = ttk.Label(master=self._frame,
                              text="This month overview", font=('', 32))
        holdings_label = ttk.Label(master=self._frame, text="holdings")
        button = ttk.Button(
            master=self._frame,
            text="BUY",
            command=self._show_buy_view
        )

        viewtitle.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")
        holdings_label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        button.grid(row=3, column=0, padx=10, pady=3, sticky="ew")
