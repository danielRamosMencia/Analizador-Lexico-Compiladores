from ..converter.lexical_parser import LexicalParser
from ..converter.syntactic_parser import SyntacticParser
from tkinter import filedialog, ttk
import regex as re
import tkinter as tk
import customtkinter
import codecs

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.window_width = 1344
        self.window_height = 768
        self.lex_table_headings = [
            {"name": "token_line", "text": "Línea del token"},
            {"name": "token_type", "text": "Tipo del token"},
            {"name": "value", "text": "Valor"}
        ]
        self.syn_table_headings = [
            {"name": "input", "text": "Entrada"},
            {"name": "output", "text": "Salida"}
        ]

        self.window_config()
        self.layout_config()
        self.populate_window()

    def window_config(self):
        # Configuración básica de CustomTkinter
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        # Configuración básica de la ventana
        self.set_geometry()
        self.title("Convertidor de números")

        # Configuración de estilos para la tabla
        ttk.Style().theme_use("default")
        ttk.Style().configure(
            "Treeview",
            background="#1d1f1e",
            foreground="white",
            fieldbackground="#1d1f1e",
            borderwidth=0
        )
        ttk.Style().configure(
            "Treeview.Heading",
            background="#4a4c4b",
            foreground="white",
            relief="flat"
        )
        ttk.Style().map(
            'Treeview',
            background=[('selected', '#22559b')]
        )
        ttk.Style().map(
            "Treeview.Heading",
            background=[('active', '#1f6aa4')]
        )

    def set_geometry(self):
        # Establece las dimensiones de la ventana
        self.geometry(f"{self.window_width}x{self.window_height}")

        # Obtiene las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcula las coordenadas de la ventana para centrarla
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2

        # Establece la posición de la ventana en las coordenadas calculadas
        self.geometry(f"+{x}+{y}")

    def layout_config(self):
        # Configura el diseño de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Crea y configura los marcos internos de la ventana
        self.left_frame = customtkinter.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, padx=16, pady=16, sticky="nsew")

        self.right_frame = customtkinter.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=16, pady=16, sticky="nsew")

    def populate_window(self):
        self.populate_left_frame()
        self.populate_right_frame()

    def populate_left_frame(self):
        # Crea un encabezado
        heading = customtkinter.CTkLabel(
            self.left_frame,
            text="Entrada",
            font=customtkinter.CTkFont(size=32, weight="bold")
        )
        heading.grid(row=0, column=0, padx=16, pady=16, sticky="w")

        # Crea el botón para seleccionar un archivo de texto
        self.file_button = customtkinter.CTkButton(
            self.left_frame,
            width=384,
            height=48,
            text="Selecciona un archivo...",
            command=self.file_button_event,
            text_color=("gray10", "#DCE4EE"),
            fg_color="transparent",
            border_width=2
        )
        self.file_button.grid(row=1, column=0, padx=16, pady=24, sticky="w")

        # Crea una etiqueta
        label1 = customtkinter.CTkLabel(
            self.left_frame,
            text="...o introduce las cadenas manualmente:"
        )
        label1.grid(row=2, column=0, padx=16, pady=16, sticky="w")

        # Crea el cuadro de texto de entrada
        self.input_text = customtkinter.CTkTextbox(
            self.left_frame,
            width=384,
            height=240,
        )
        self.input_text.grid(row=3, column=0, padx=16, pady=24, sticky="w")

        # Crea un botón para seleccionar un archivo de texto
        self.convert_button = customtkinter.CTkButton(
            self.left_frame,
            width=384,
            height=48,
            text="Convertir",
            command=self.convert_button_event
        )
        self.convert_button.grid(row=5, column=0, padx=16, pady=24, sticky="w")

        # Crea el botón para limpiar las entradas
        self.reset_button = customtkinter.CTkButton(
            self.left_frame,
            width=384,
            height=48,
            text="Limpiar",
            command=self.reset_button_event,
            text_color=("gray10", "#DCE4EE"),
            fg_color="transparent",
            border_width=2
        )
        self.reset_button.grid(row=6, column=0, padx=16, pady=24, sticky="w")

    def populate_right_frame(self):
        # Crea un encabezado
        heading = customtkinter.CTkLabel(
            self.right_frame,
            text="Salida del analizador léxico",
            font=customtkinter.CTkFont(size=32, weight="bold")
        )
        heading.grid(row=0, column=0, padx=16, pady=16, sticky="w")

        # Crea la tabla de salida para el analizador léxico a partir de los encabezados en el diccionario
        self.lex_table = ttk.Treeview(
            self.right_frame,
            columns=tuple(heading["name"] for heading in self.lex_table_headings),
            show="headings"
        )
        for heading in self.lex_table_headings:
            self.lex_table.heading(heading["name"], text=heading["text"])
            self.lex_table.column(heading["name"], width=276)
        for column in self.lex_table["columns"]:
            self.lex_table.column(column, anchor="center")
        self.lex_table.grid(row=1, column=0, padx=16, pady=24, sticky="w")

        # Crea un encabezado
        heading = customtkinter.CTkLabel(
            self.right_frame,
            text="Salida del analizador sintáctico",
            font=customtkinter.CTkFont(size=32, weight="bold")
        )
        heading.grid(row=2, column=0, padx=16, pady=16, sticky="w")

        # Crea la tabla de salida para el analizador sintáctico a partir de los encabezados en el diccionario
        self.syn_table = ttk.Treeview(
            self.right_frame,
            columns=tuple(heading["name"] for heading in self.syn_table_headings),
            show="headings"
        )
        for heading in self.syn_table_headings:
            self.syn_table.heading(heading["name"], text=heading["text"])
            self.syn_table.column(heading["name"], width=416)
        for column in self.syn_table["columns"]:
            self.syn_table.column(column, anchor="center")
        self.syn_table.grid(row=3, column=0, padx=16, pady=24, sticky="w")

    # Abre la ventana de diálogo para buscar archivos
    # Lee el contenido de los archivos de texto, en formato UTF-8
    # Modifica el texto del cuadro de texto de entrada
    def file_button_event(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
            if not file_path:
                print("No se seleccionó ningún archivo.")
            else:
                with codecs.open(file_path, "r", encoding="utf-8") as file:
                    tmp = file.read()
                    # Reemplaza los saltos de línea 
                    readed_text = tmp.replace("\n","")
                    # Reemplaza los retornos de carro
                    readed_text = tmp.replace("\r","")
                    self.file_button.configure(text=file_path)
                    self.input_text.delete("0.0", "end")
                    self.input_text.insert("0.0", readed_text)
        except tk.TclError:
            print("No se seleccionó ningún archivo.")

    # Limpia tanto la entrada como la salida del programa
    def reset_button_event(self):
        self.file_button.configure(text="Selecciona un archivo...")
        self.input_text.delete("0.0", "end")
        self.lex_table.delete(*self.lex_table.get_children())
        self.syn_table.delete(*self.syn_table.get_children())

    # Ejecuta los analizadores y convierte los números al sistema destino
    def convert_button_event(self):
        # Limpia la salida anterior (si existe)
        self.lex_table.delete(*self.lex_table.get_children())
        self.syn_table.delete(*self.syn_table.get_children())

        # Obtiene el texto de entrada
        tmp_text = self.input_text.get("0.0", "end")
        # Pasa el texto de entrada para facilitar el match de los tokens en el analizador léxico
        text = tmp_text.lower()
        # Expresión regular para solo obtener las entradas que cumplan con la gramática "NUMBER DESTINY"
        matches = re.findall("\d+\s*hexadecimal|\d+\s*octal|\d+\s*binary|\d+\s*roman|\d+\s*alternative|\d+\s*random",text)
        # Expresión regular para obtener las entradas que NO cumplan con la gramática "NUMBER DESTINTY"
        no_matches = re.split("\d+\s*hexadecimal|\d+\s*octal|\d+\s*binary|\d+\s*roman|\d+\s*alternative|\d+\s*random",text)
        
        # Lista para almacenar las entradas invalidas depuradas
        invalid_entrances = []

        # Se recorre la lista 
        for i in no_matches:
            # Expresiòn regular para eliminar los saltos de línea, tabulaciones, retornos de carro
            clean = re.sub("\n*|\t*|\r*|\s", "", i)
            # Las entradas invalidas depuradas se anexan a la lista
            invalid_entrances.append(clean)

        # Crea el analizador léxico
        lex = LexicalParser()

        # Ejecuta el analizador léxico y retorna el resultado
        lex_result = lex.parse(text)

        # Crea y añade una fila a la tabla de salida del analizador léxico para cada token
        for lex_token in lex_result:
            new_row = (lex_token.lineno, lex_token.type, lex_token.value)
            self.lex_table.insert("", "end", values=new_row)

        # Crea el analizador sintáctico
        syn = SyntacticParser()        
        
        # Recorre la lista con las entradas válidas
        for element in matches:
            # Expresiòn regular para eliminar los saltos de línea, tabulaciones, retornos de carro
            # limpia las coincidencias para una mejor visualización de los matches.
            temp = re.sub("\n*|\t*|\r*|\s", "", element)
            # Llama al analizador sintáctico para realizar la conversión
            syn_result = syn.parse(element)
            # Crea una nueva fila con los valores de la entrada y el retorno de la conversión del analizador sintáctico
            new_row = (temp, syn_result)
            # Se añade a la tabla de salida
            self.syn_table.insert("", "end", values=new_row)

        #Recorre la lista con las entradas válidas
        for invalid in invalid_entrances:
            # Si el elemento en la lista es diferente a ''
            if(invalid != ''):
                # Toma el elemento y lo muestra con un mensaje de inválidez
                new_row = (invalid, "---Entrada inválida---")
                # Se añadae a la tabla de salida
                self.syn_table.insert("", "end", value=new_row)

