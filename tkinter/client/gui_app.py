import tkinter as tk
from tkinter import filedialog
from client.plot_netcdf import plot
from client.to_csv import export_csv
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu= barra_menu, width= 300, height= 300)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)

    menu_inicio.add_command(label= 'Some action')
    menu_inicio.add_command(label= 'Some action')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)

    barra_menu.add_cascade(label= 'Action #2')
    barra_menu.add_cascade(label= 'Action #3')
    barra_menu.add_cascade(label= 'Action #4')

class Frame(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width= 500, height= 350)
        self.root = root
        self.pack()
        self.config(bg= 'gray')

        self.campos_netcdf()

    def campos_netcdf(self):
        # Button open File
        self.button_tmin = tk.Button(self, text= 'Seleccione NetCDF para Temperatura Minima', command= self.open_tmin)
        self.button_tmin.grid(row= 0, column= 0, padx= 10, pady= 10)

        self.button_tmax = tk.Button(self, text= 'Seleccione NetCDF para Temperatura Maxima', command= self.open_tmax)
        self.button_tmax.grid(row= 1, column= 0, padx= 10, pady= 10)

        self.button_pr = tk.Button(self, text= 'Seleccione NetCDF para Precipitaciones', command= self.open_pr)
        self.button_pr.grid(row= 2, column= 0, padx= 10, pady= 10)

        # Entry's
        self.entry_tmin = tk.Entry(self)
        self.entry_tmin.config(width= 50, state='normal', font= ('Arial', 12))
        self.entry_tmin.grid(row=0, column= 1, padx= 10, pady= 10)

        self.entry_tmax = tk.Entry(self)
        self.entry_tmax.config(width= 50, state='normal', font= ('Arial', 12))
        self.entry_tmax.grid(row=1, column= 1, padx= 10, pady= 10)

        self.entry_pr = tk.Entry(self)
        self.entry_pr.config(width= 50, state='normal', font= ('Arial', 12))
        self.entry_pr.grid(row=2, column= 1, padx= 10, pady= 10)

        # Button show Map
        self.button_show_tmin = tk.Button(self, text= 'Ver Mapa', command= self.show_map_tmin)
        self.button_show_tmin.grid(row= 0, column= 2, padx= 10, pady= 10)
        
        self.button_show_tmax = tk.Button(self, text= 'Ver Mapa', command= self.show_map_tmax)
        self.button_show_tmax.grid(row= 1, column= 2, padx= 10, pady= 10)
        
        self.button_show_pr = tk.Button(self, text= 'Ver Mapa', command= self.show_map_pr)
        self.button_show_pr.grid(row= 2, column= 2, padx= 10, pady= 10)


        # Button export to CSV
        self.button_export_tmin = tk.Button(self, text= 'Exportar a CSV', command= self.export_tmin)
        self.button_export_tmin.grid(row= 0, column= 3, padx= 10, pady= 10)
        
        self.button_export_tmax = tk.Button(self, text= 'Exportar a CSV', command= self.export_tmax)
        self.button_export_tmax.grid(row= 1, column= 3, padx= 10, pady= 10)
        
        self.button_export_pr = tk.Button(self, text= 'Exportar a CSV', command= self.export_pr)
        self.button_export_pr.grid(row= 2, column= 3, padx= 10, pady= 10)

        # Button to generate GIF
        self.button_gif_tmin = tk.Button(self, text= 'Generar GIF', command= self.generate_gif_tmin)
        self.button_gif_tmin.grid(row= 0, column= 4, padx= 10, pady= 10)

        self.button_gif_tmax = tk.Button(self, text= 'Generar GIF', command= self.generate_gif_tmin)
        self.button_gif_tmax.grid(row= 1, column= 4, padx= 10, pady= 10)

        self.button_gif_pr = tk.Button(self, text= 'Generar GIF', command= self.generate_gif_tmin)
        self.button_gif_pr.grid(row= 2, column= 4, padx= 10, pady= 10)

    # Functions open file
    def open_tmin(self):
        file = tk.filedialog.askopenfilename(title= 'Abrir NetCDF para temperatura minima', initialdir= 'C:/', filetypes= (("Archivos NetCDF","*.nc"), ("Cualquier Archivo", "*.*")))
        self.entry_tmin.delete(0, tk.END)
        self.entry_tmin.insert(0, file)
        self.entry_tmin.config(state= 'normal')

    def open_tmax(self):
        file = tk.filedialog.askopenfilename(title= 'Abrir NetCDF para temperatura maxima', initialdir= 'C:/', filetypes= (("Archivos NetCDF","*.nc"), ("Cualquier Archivo", "*.*")))
        self.entry_tmax.delete(0, tk.END)
        self.entry_tmax.insert(0, file)
        self.entry_tmax.config(state= 'normal')

    def open_pr(self):
        file = tk.filedialog.askopenfilename(title= 'Abrir NetCDF para precipitaciones', initialdir= 'C:/', filetypes= (("Archivos NetCDF","*.nc"), ("Cualquier Archivo", "*.*")))
        self.entry_pr.delete(0, tk.END)
        self.entry_pr.insert(0, file)
        self.entry_pr.config(state= 'normal')

    # Functions show map
    def show_map_tmin(self):
        if len(self.entry_tmin.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'tmin', action= 'plot')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para temperatura minima')

    def show_map_tmax(self):
        if len(self.entry_tmax.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'tmax', action= 'plot')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para temperatura maxima')
    
    def show_map_pr(self):
        if len(self.entry_pr.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'pr', action= 'plot')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para precipitaciones')
    
    #  Function export to CSV
    def export_tmin(self):
        if len(self.entry_tmin.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'tmin', action= 'csv')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para temperatura minima')

    def export_tmax(self):
        if len(self.entry_tmax.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'tmax', action= 'csv')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para temperatura maxima')


    def export_pr(self):
        if len(self.entry_pr.get()) > 0:
            # Create a modal to show the message
            self.modal_calendar(tipo= 'pr', action= 'csv')
        else:
            tk.messagebox.showerror('Ups! Se te ha olvidado el archivo', 'Por favor, ingrese archivo NetCDF para precipitaciones')


    def modal_calendar(self, tipo= ['tmin', 'tmax', 'pr'], action= ['plot', 'csv']):
        top = tk.Toplevel()
        top.title('Seleccione una fecha')
        top.geometry("680x80")

        lbl = tk.Label(top, text= 'Seleccione una fecha entre 1978-12-15 y 2019-01-01 (Formato: YYYY-MM-DD)')
        lbl.grid(row= 0, column= 0, padx= 10, pady= 10)
        cal = DateEntry(top, selectmode= 'day', date_pattern= 'YYYY-mm-dd')
        cal.grid(row= 0, column= 1, padx= 10, pady= 10)

        if tipo == 'tmin':
            title = 'Mapa de temperatura minima de '

        if tipo == 'tmax':
            title = 'Mapa de temperatura maxima de '

        if tipo == 'pr':
            title= 'Mapa de precipitaciones de '

        if action == 'plot':
            texto = 'Ver Mapa'
        else:
            texto = 'Exportar a CSV'

        self.button_date = tk.Button(top, text= texto, command= lambda: self.validate_date(fecha= cal.get_date(), 
                                                                                                titulo= title, tipo= tipo, action= action))
        self.button_date.grid(row= 0, column= 2, padx= 10, pady= 10)

        top.mainloop()
    
    # validar fecha dentro del rango valido
    def validate_date(self, fecha, titulo, tipo = ['tmin', 'tmax', 'pr'], action= ['plot', 'csv']):
        start_date = datetime.date(1978, 12, 15)
        ending_date = datetime.date(2019, 10, 30)
        if fecha < start_date or fecha > ending_date:
            return tk.messagebox.showerror('Ups! Fecha fuera de rango', 
                                            'Por favor, ingrese una fecha entre 1978-12-15 y 2019-10-30')
        else:
            if action == 'plot':
                self.modal_map(titulo= titulo, fecha= fecha, tipo= tipo)
            else:
                self.export_to_csv(fecha= fecha, tipo= tipo)

    # Desplegar imagen
    def modal_map(self, titulo, fecha, tipo= ['tmin', 'tmax', 'pr']):
        if tipo == 'tmin':
            path_netcdf= self.entry_tmin.get()
        
        if tipo == 'tmax':
            path_netcdf= self.entry_tmax.get()

        if tipo == 'pr':
            path_netcdf= self.entry_pr.get()

        res = plot(ruta= path_netcdf, fecha= fecha, tipo= tipo)
        image = ImageTk.PhotoImage(Image.open(res))
        top = tk.Toplevel()
        top.title(titulo + str(fecha))
        top.geometry("800x750")
        lbl = tk.Label(top, image= image)
        lbl.grid(row= 0, column= 0)
        tk.messagebox.showinfo('Imagen Guardada', 'La imagen se guardó correctamente en '+ str(res))
        top.mainloop()

    def generate_gif_tmin(self):
        pass

    def export_to_csv(self, fecha, tipo= ['tmin', 'tmax', 'pr']):
        if tipo == 'tmin':
            path_netcdf= self.entry_tmin.get()
        
        if tipo == 'tmax':
            path_netcdf= self.entry_tmax.get()

        if tipo == 'pr':
            path_netcdf= self.entry_pr.get()

        res = export_csv(path_netcdf, fecha, tipo)

        if res == None:
            tk.messagebox.showinfo('Exportado a CSV', 'Archivo CSV guardado correctamente en la carpera CSV')
        else:
            tk.messagebox.showerror('Ups! Error al exportar', 'Lo sentimos. No se pudo exportar a CSV')
