import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
from collections import namedtuple
from functools import wraps

# ============ UTILITY ============

PanelData = namedtuple("PanelData", ["daya_puncak", "efisiensi", "luas_panel", "irradiasi"])

def logger(cls):
    original_calc = cls.calculate

    @wraps(cls.calculate)
    def new_calc(*args, **kwargs):
        print(f"[LOG] Kalkulasi {cls.__name__} dengan args={args[1:]}") 
        return original_calc(*args, **kwargs)

    cls.calculate = new_calc
    return cls

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# ============ MODEL ============

class DataStore(metaclass=Singleton):
    panel_data = None

    @classmethod
    def set_panel_data(cls, daya_puncak, efisiensi, luas_panel, irradiasi):
        cls.panel_data = PanelData(daya_puncak, efisiensi, luas_panel, irradiasi)

class Calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass

@logger
class EnergyCalculator(Calculator):
    def calculate(self, panel_data: PanelData):
        return (panel_data.daya_puncak / 1000) * (panel_data.efisiensi / 100) * panel_data.irradiasi * panel_data.luas_panel

class CalculatorFactory:
    @staticmethod
    def get_calculator(calc_type):
        if calc_type == "energy":
            return EnergyCalculator()
        else:
            raise ValueError("Tipe kalkulator tidak dikenali")

# ============ VIEW & CONTROLLER ============

class BaseFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(bg="#f0f0f0")

class MainMenu(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        container = tk.Frame(self, bg="#f0f0f0")
        container.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(container, text="SimPL - Menu Utama", font=("Helvetica", 20), bg="#f0f0f0").pack(pady=10)

        tk.Button(container, text="Simulasi Daya Panel Surya",
                  width=30,
                  command=lambda: controller.show_frame(InputPanelForm)).pack(pady=5)

        tk.Button(container, text="About SimPL", width=30, command=self.show_about).pack(pady=5)

        tk.Button(container, text="Exit", width=30, command=controller.root.quit, fg="white", bg="red").pack(pady=20)

    def show_about(self):
        messagebox.showinfo("Tentang SimPL",
            "SimPL (Simulasi Energi PLTS)\n\n"
            "Versi: 1.0\nProyek Akhir - Pemrograman Berbasis Objek\n\n"
            "Dibuat oleh: Gradien Saputra\n"
            "Fitur:\n- Simulasi Daya Panel Surya\n- Simulasi Kebutuhan Listrik\n"
            "- Estimasi ROI\n- Edukasi Panel Surya\n")

class InputPanelForm(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        container = tk.Frame(self, bg="#f0f0f0")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Input Data Panel Surya", font=("Helvetica", 18), bg="#f0f0f0").pack(pady=10)

        self.daya_var = tk.DoubleVar()
        self.efisiensi_var = tk.DoubleVar()
        self.luas_var = tk.DoubleVar()
        self.irradiasi_var = tk.DoubleVar()

        self.create_field(container, "Daya Puncak (Wp):", self.daya_var)
        self.create_field(container, "Efisiensi (%):", self.efisiensi_var)
        self.create_field(container, "Luas Panel (m²):", self.luas_var)
        self.create_field(container, "Irradiasi Harian (kWh/m²):", self.irradiasi_var)

        tk.Button(container, text="Hitung", width=20, command=self.calculate_energy).pack(pady=10)
        tk.Button(container, text="Kembali", width=20, command=lambda: controller.show_frame(MainMenu)).pack()

    def create_field(self, parent, label, variable):
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(pady=5, fill="x")

        tk.Label(frame, text=label, width=25, anchor="w", bg="#f0f0f0").pack(side="left", padx=5)
        tk.Entry(frame, textvariable=variable, width=10).pack(side="right", padx=5)

    def calculate_energy(self):
        try:
            DataStore.set_panel_data(self.daya_var.get(), self.efisiensi_var.get(),
                                     self.luas_var.get(), self.irradiasi_var.get())
            energi = CalculatorFactory.get_calculator("energy").calculate(DataStore.panel_data)
            messagebox.showinfo("Hasil Simulasi", f"Energi dihasilkan: {energi:.2f} kWh/hari")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ============ CONTROLLER APLIKASI ============

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("SimPL - Simulasi Energi PLTS")
        self.root.geometry("600x400")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (MainMenu, InputPanelForm):
            frame = F(root, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)
        self.show_welcome_message()

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def show_welcome_message(self):
        messagebox.showinfo("Selamat Datang",
            "Selamat datang di aplikasi SimPL.\nSimulasi sederhana panel surya berbasis Python GUI.")

# ============ MAIN ============

if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()
