import tkinter as tk
from tkinter import ttk, messagebox

def format_money(amount):
    return f"${amount:,.4f}"

class SysitapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SySITap - Calculadora Persona Moral")
        self.root.geometry("450x380")
        self.root.resizable(False, False)
        
        # Variables para almacenamiento
        self.val_neto_a = 0.0
        self.val_tot_a = 0.0
        self.val_sub_b = 0.0
        self.val_neto_b = 0.0

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Notebook (Pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Frame Subtotal
        self.frame_sub = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.frame_sub, text="Tengo Subtotal")
        self.setup_subtotal_tab()

        # Frame Neto
        self.frame_neto = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.frame_neto, text="Tengo Neto a Pagar")
        self.setup_neto_tab()

    def setup_subtotal_tab(self):
        ttk.Label(self.frame_sub, text="Ingrese Subtotal:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=2)
        self.entry_sub = ttk.Entry(self.frame_sub, font=('Arial', 12))
        self.entry_sub.pack(fill='x', pady=5)
        self.entry_sub.bind('<KeyRelease>', self.calc_sub)

        self.lbl_res_sub = ttk.Label(self.frame_sub, text="Subtotal: $0.00", font=('Arial', 9))
        self.lbl_res_sub.pack(anchor='w', pady=1)
        self.lbl_res_iva = ttk.Label(self.frame_sub, text="IVA (8%): $0.00", font=('Arial', 9))
        self.lbl_res_iva.pack(anchor='w', pady=1)
        self.lbl_res_tot = ttk.Label(self.frame_sub, text="Total: $0.00", font=('Arial', 9, 'bold'))
        self.lbl_res_tot.pack(anchor='w', pady=1)
        self.lbl_res_ret = ttk.Label(self.frame_sub, text="Retención (1.25%): $0.00", font=('Arial', 9))
        self.lbl_res_ret.pack(anchor='w', pady=1)
        self.lbl_res_net = ttk.Label(self.frame_sub, text="Neto a Pagar: $0.00", font=('Arial', 10, 'bold'), foreground='blue')
        self.lbl_res_net.pack(anchor='w', pady=3)

        btn_frame = ttk.Frame(self.frame_sub)
        btn_frame.pack(fill='x', pady=5)
        ttk.Button(btn_frame, text="Copiar Neto", command=lambda: self.copiar(self.val_neto_a)).pack(side='left', expand=True, fill='x', padx=2)
        ttk.Button(btn_frame, text="Copiar Total", command=lambda: self.copiar(self.val_tot_a)).pack(side='right', expand=True, fill='x', padx=2)

    def setup_neto_tab(self):
        ttk.Label(self.frame_neto, text="Ingrese Neto a Pagar:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=2)
        self.entry_neto = ttk.Entry(self.frame_neto, font=('Arial', 12))
        self.entry_neto.pack(fill='x', pady=5)
        self.entry_neto.bind('<KeyRelease>', self.calc_neto)

        self.lbl_b_net = ttk.Label(self.frame_neto, text="Neto a Pagar: $0.00", font=('Arial', 9))
        self.lbl_b_net.pack(anchor='w', pady=1)
        self.lbl_b_ret = ttk.Label(self.frame_neto, text="Retención (1.25%): $0.00", font=('Arial', 9))
        self.lbl_b_ret.pack(anchor='w', pady=1)
        self.lbl_b_tot = ttk.Label(self.frame_neto, text="Total: $0.00", font=('Arial', 9))
        self.lbl_b_tot.pack(anchor='w', pady=1)
        self.lbl_b_iva = ttk.Label(self.frame_neto, text="IVA (8%): $0.00", font=('Arial', 9))
        self.lbl_b_iva.pack(anchor='w', pady=1)
        self.lbl_b_sub = ttk.Label(self.frame_neto, text="Subtotal: $0.00", font=('Arial', 10, 'bold'), foreground='blue')
        self.lbl_b_sub.pack(anchor='w', pady=3)

        btn_frame2 = ttk.Frame(self.frame_neto)
        btn_frame2.pack(fill='x', pady=5)
        ttk.Button(btn_frame2, text="Copiar Subtotal", command=lambda: self.copiar(self.val_sub_b)).pack(side='left', expand=True, fill='x', padx=2)
        ttk.Button(btn_frame2, text="Copiar Neto", command=lambda: self.copiar(self.val_neto_b)).pack(side='right', expand=True, fill='x', padx=2)

    def calc_sub(self, event):
        try:
            b4 = float(self.entry_sub.get())
        except ValueError:
            b4 = 0.0
        c4 = b4 * 8 / 100
        d4 = b4 + c4
        e4 = b4 * 1.25 / 100
        f4 = d4 - e4
        
        self.val_tot_a = d4
        self.val_neto_a = f4

        self.lbl_res_sub.config(text=f"Subtotal: {format_money(b4)}")
        self.lbl_res_iva.config(text=f"IVA (8%): {format_money(c4)}")
        self.lbl_res_tot.config(text=f"Total: {format_money(d4)}")
        self.lbl_res_ret.config(text=f"Retención (1.25%): {format_money(e4)}")
        self.lbl_res_net.config(text=f"Neto a Pagar: {format_money(f4)}")

    def calc_neto(self, event):
        try:
            b7 = float(self.entry_neto.get())
        except ValueError:
            b7 = 0.0
        f7 = b7 / 1.0674997
        c7 = f7 * 1.25 / 100
        d7 = b7 * 1.0117097
        e7 = f7 * 8 / 100

        self.val_sub_b = f7
        self.val_neto_b = b7

        self.lbl_b_net.config(text=f"Neto a Pagar: {format_money(b7)}")
        self.lbl_b_ret.config(text=f"Retención (1.25%): {format_money(c7)}")
        self.lbl_b_tot.config(text=f"Total: {format_money(d7)}")
        self.lbl_b_iva.config(text=f"IVA (8%): {format_money(e7)}")
        self.lbl_b_sub.config(text=f"Subtotal: {format_money(f7)}")

    def copiar(self, valor):
        texto = f"{valor:.2f}"
        self.root.clipboard_clear()
        self.root.clipboard_append(texto)
        messagebox.showinfo("Copiado", f"¡Monto {texto} copiado al portapapeles!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SysitapApp(root)
    root.mainloop()
