import customtkinter as ctk

# Appearance mode and default color theme
ctk.set_appearance_mode("Dark") # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("CTkThemes/marsh.json") # Default themes: "blue" (standard), "green", "dark-blue"

# Default pack settings
# Frame and label
PADY = 20
PADX = 20
FILL = "both"
EXPAND = True

# Radio
RADIO_PADY = 5

class StyledFrame(ctk.CTkFrame):
    """Styled container frame with consistent default sizing and style."""
    def __init__(self, master, width=200, height=200):
        super().__init__(
            master=master,
            width=width,
            height=height
        )


class StyledLabel(ctk.CTkLabel):
    """Styled label with consistent default sizing and style."""
    def __init__(self, master, text):
        super().__init__(
            master=master,
            text=text
        )


class RadioOption(ctk.CTkRadioButton):
    """Styled radio option with consistent default sizing and style."""
    def __init__(self, master, text, variable, value):
        self.variable = variable
        super().__init__(
            master=master,
            text=text,
            command=self.radiobutton_event,
            variable=variable,
            value=value
        )

    def radiobutton_event(self):
        print(f"Selected option: {self.variable.get()}")


class StylizedButton(ctk.CTkButton):
    """Styled button with consistent default sizing and style."""
    def __init__(self, master, text, command=None, width=120, height=32, hover=True):
        if command is None:
            self.command = self.button_callback
        else:
            self.command = command

        super().__init__(
            master=master,
            text=text,
            command=self.command,
            width=width,
            height=height,
            hover=hover
        )

    def button_callback(self):
        print("Button clicked")


class StyledEntry(ctk.CTkEntry):
    """Styled entry with consistent default sizing and style."""
    def __init__(self, master, placeholder_text, width=200, height=30):
        super().__init__(
            master=master,
            placeholder_text=placeholder_text,
            width=width,
            height=height
        )

    def get_text(self):
        text = self.get()
        print(f"Entry contains: {text}")   # Test
        return text


# Create main window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dr. Mai's Nutritional Calculator Lite")
        self.geometry("800x800")    # Window size
        self.resizable(width=True, height=True)  # Allow resizing

        # Create main frame
        main_frame = StyledFrame(self)
        main_frame.pack(pady=PADY, padx=PADX, fill=FILL, expand=EXPAND)

        # Create and store labeled child frames
        frame_labels = {"species": "Species", "weight": "Current weight in pounds", "bcs": "Body Condition Score (BCS)", "calc": None}
        frames = {}
        labels = {}

        for frame_name, label_text in frame_labels.items():
            frames[frame_name] = StyledFrame(main_frame)
            frames[frame_name].pack(pady=PADY, padx=PADX, fill=FILL, expand=EXPAND)

            if label_text:
                labels[frame_name] = StyledLabel(frames[frame_name], label_text)
                labels[frame_name].pack(pady=PADY)

        print(frames)   # Test
        print(labels)   # Test

        # Create species radio
        radio_species = ctk.StringVar(value="")

        species_dog = RadioOption(master=frames["species"], text="Dog", variable=radio_species, value="dog")
        species_dog.pack(pady=RADIO_PADY)

        species_cat = RadioOption(master=frames["species"], text="Cat", variable=radio_species, value="cat")
        species_cat.pack(pady=RADIO_PADY)

        # Create weight entry
        entry_weight = StyledEntry(master=frames["weight"], placeholder_text="lbs..")
        entry_weight.pack(pady=10)

        # Test weight entry
        # button_weight = StylizedButton(master=frames["weight"], text="Enter weight", command=entry_weight.get_text)
        # button_weight.pack(pady=5)

        # Create BCS radio
        radio_bcs = ctk.IntVar(value=0)

        bcs_values = []
        for num in range(9):
            bcs_values.append(RadioOption(master=frames["bcs"], text=str(num + 1), variable=radio_bcs, value=num + 1))
            #bcs_values[num].grid(row=num, column=num, padx=5, pady=5, sticky="nsew")
            bcs_values[num].pack(pady=RADIO_PADY)
        # Test
        for index, value in enumerate(bcs_values):
            print(index, value)

        # Create calculate button
        calculate = StylizedButton(master=frames["calc"], text="Calculate")
        calculate.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

