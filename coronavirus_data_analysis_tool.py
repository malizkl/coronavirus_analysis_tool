

class Cluster:
    def cluster_data(self):
        countries, words, data = clusters.readfile('matrix.txt')  # reads matrix
        clust = clusters.hcluster(data)
        clusters.drawdendrogram(clust, labels=countries, jpeg="cl.jpeg")  # makes picture


class Data:
    def __init__(self, countries, criterias):
        self.countries = countries  # countries data
        self.criterias = criterias  # criterias data

    def create_file(self, selected_countries, selected_criterias, reverse=False):
        if not selected_criterias:  # fills list if empty
            c_lst = []
            for indx in range(10):
                c_lst.append(indx)
            selected_criterias = tuple(c_lst)
        if not selected_countries:
            c_lst = []
            for indx in range(len(self.countries)):
                c_lst.append(indx)
            selected_countries = tuple(c_lst)
        info_file = open('matrix.txt', 'w')
        if not reverse:  # cluster countries
            info_file.write("Countries")
            for criterias in selected_criterias:
                info_file.write(self.criterias[criterias] + "\t")
            info_file.write('\n')
            for countries in selected_countries:
                info_file.write(self.countries[countries][0])
                if selected_criterias:
                    for indx in selected_criterias:
                        info_file.write("\t" + str(int(self.countries[countries][indx+1])))
                else:
                    for indx in range(1, 11):
                        info_file.write("\t" + str(int(self.countries[countries][indx])))
                info_file.write('\n')
        else:  # cluster criterias
            info_file.write("Criterias")
            for countries in selected_countries:
                info_file.write(self.countries[countries][0] + "\t")
            info_file.write('\n')
            for criterias in selected_criterias:
                info_file.write(self.criterias[criterias])
                for countries in selected_countries:
                    info_file.write("\t" + str(int(self.countries[countries][criterias+1])))
                info_file.write('\n')
        info_file.close()


class Gui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.criterias = []
        self.countries = []

    def user_interface(self):
        # Main container
        self.container = Frame(self, bg='grey')
        self.label = Label(self.container, text='Coronavirus Data Analysis Tool', bg='red', font='Arial 16 bold',
                           fg='white')
        self.canvas_scroll_container = Frame(self.container, bg='grey')
        self.canvas_y_scroll = Scrollbar(self.canvas_scroll_container, orient=VERTICAL)
        self.canvas_x_scroll = Scrollbar(self.container, orient=HORIZONTAL)
        self.canvas = Canvas(self.canvas_scroll_container, bg='grey', width=1025, height=300,
                             yscrollcommand=self.canvas_y_scroll.set, xscrollcommand=self.canvas_x_scroll.set)
        self.canvas_y_scroll.config(command=self.canvas.yview)
        self.canvas_x_scroll.config(command=self.canvas.xview)

        # Buttons and container
        self.button_container = Frame(self.container, bg='grey')
        self.country_button = Button(self.button_container, text="Upload Country Data", command=self.open_country_file)
        self.statistics_button = Button(self.button_container, text="Upload Test Statistics",
                                        command=self.open_statistics_file)

        # Tools Container
        self.tools_container = Frame(self.container, bg='grey')

        # Sorting Container
        self.sorting_container = Frame(self.tools_container,  highlightbackground='black', bg='grey',
                                       highlightthickness=1)
        self.sort_label = Label(self.sorting_container, text="Sort Countries:", bg='grey')
        self.sort_name = Button(self.sorting_container, text="Sort by name", command=self.sort_by_name)
        self.sort_cases = Button(self.sorting_container, text="Sort by Total Case", command=self.sort_by_cases)

        # Country Listbox Container
        self.country_container = Frame(self.tools_container, bg='grey')
        self.listbox_country_label = Label(self.country_container, text='Countries: ', bg='grey')
        self.country_scrollbar_y = Scrollbar(self.country_container, orient=VERTICAL)
        self.listbox_country = Listbox(self.country_container, width=40, height=7, exportselection=False,
                                       yscrollcommand=self.country_scrollbar_y.set, selectmode=MULTIPLE)
        self.country_scrollbar_y.config(command=self.listbox_country.yview)
        self.listbox_country.propagate(False)

        # Criterias Listbox Container
        self.criterias_container = Frame(self.tools_container, bg='grey')
        self.listbox_criterias_label = Label(self.criterias_container, text="Criterias: ", bg='grey')
        self.criterias_scrollbar_y = Scrollbar(self.criterias_container, orient=VERTICAL)
        self.listbox_criterias = Listbox(self.criterias_container, width=40, height=7, exportselection=False,
                                         yscrollcommand=self.criterias_scrollbar_y.set, selectmode=MULTIPLE                                         )
        self.criterias_scrollbar_y.config(command=self.listbox_criterias.yview)
        self.listbox_criterias.propagate(False)

        # Clustering Container
        self.cluster_container = Frame(self.tools_container, highlightbackground='black', bg='grey',
                                       highlightthickness=1)
        self.cluster_label = Label(self.cluster_container, text="Analyse Data: ", bg='grey')
        self.cluster_countries = Button(self.cluster_container,
                                        text="Cluster Countries:", command=self.cluster_countries)
        self.cluster_criterias = Button(self.cluster_container,
                                        text="Cluster Criterias", command=self.cluster_criterias)

        # Pack widgets
        self.pack(fill=BOTH, expand=TRUE)
        self.container.pack(fill=BOTH, expand=TRUE)
        self.label.pack(fill=X)
        self.canvas_scroll_container.pack()
        self.canvas.pack(side=LEFT)
        self.canvas_y_scroll.pack(side=LEFT, fill=Y)
        self.canvas_x_scroll.pack(fill=X)
        self.button_container.pack(anchor=CENTER, pady=10)
        self.country_button.pack(side=LEFT, padx=20)
        self.statistics_button.pack(side=LEFT)
        self.tools_container.pack(anchor=CENTER, pady=10, expand=TRUE)
        self.sorting_container.pack(side=LEFT, padx=20)
        self.sort_label.pack(pady=5)
        self.sort_name.pack(pady=10)
        self.sort_cases.pack(padx=20,pady=10)
        self.country_container.pack(side=LEFT, expand=TRUE)
        self.listbox_country_label.pack(side=LEFT)
        self.listbox_country.pack(side=LEFT)
        self.criterias_container.pack(side=LEFT, expand=TRUE)
        self.listbox_criterias_label.pack(side=LEFT)
        self.listbox_criterias.pack(side=LEFT)
        self.cluster_container.pack()
        self.cluster_container.pack(side=LEFT, padx=20)
        self.cluster_label.pack(pady=5)
        self.cluster_countries.pack(pady=10)
        self.cluster_criterias.pack(padx=20, pady=10)
        self.country_scrollbar_y.pack(fill=Y, expand=TRUE)
        self.criterias_scrollbar_y.pack(fill=Y, expand=TRUE)

    def open_country_file(self):
        file = filedialog.askopenfilename()
        loc = (file)  # used from https://www.geeksforgeeks.org/reading-excel-file-using-python/
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for criteria in range(sheet.ncols):
            if sheet.cell_value(0, criteria) != 'Country':
                self.criterias.append(sheet.cell_value(0, criteria))
        for countries in range(sheet.nrows-1):
            if sheet.row_values(countries)[0] != 'Country':
                self.countries.append(sheet.row_values(countries))
        self.add_data()

    def open_statistics_file(self):
        file = filedialog.askopenfilename()
        loc = (file)
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for countries in range(sheet.nrows):
            new = sheet.row_values(countries)
            for saved in self.countries:
                if new[0].strip() in saved:  # strip taken from https://www.geeksforgeeks.org/python-string-strip/
                    saved.extend(new[1:3])
                    saved.extend(new[4:6])
        for countries in self.countries:
            if len(countries) == 7:
                countries.extend([0,0,0,0,0])
            if '' in countries:
                for item in countries:
                    if item == '':
                        item_indx = countries.index(item)
                        countries.pop(item_indx)
                        countries.insert(item_indx, 0)
        for criteria in range(sheet.ncols):
            if sheet.cell_value(0, criteria) == 'Country or region' or sheet.cell_value(0, criteria) == 'As of':
                continue
            else:
                self.criterias.append(sheet.cell_value(0, criteria))
        self.add_criterias()

    def add_criterias(self):
        for criteria in self.criterias:
            self.listbox_criterias.insert(END, criteria)  # adds items to listbox

    def add_data(self):
        for country in self.countries:
            self.listbox_country.insert(END, country[0] + '(' + str(int(country[1])) + ')')

    def sort_by_cases(self):
        self.listbox_country.delete(0, END)
        sorted_countries = []
        for country in self.countries:
            sorted_countries.append(country[1])
        sorted_countries.sort(reverse=True)
        for s in sorted_countries:
            for country in self.countries:
                if s in country:
                    self.listbox_country.insert(END, country[0] + '(' + str(int(s)) + ')')

    def sort_by_name(self):
        self.listbox_country.delete(0, END)
        sorted_countries = []
        for country in self.countries:
            sorted_countries.append(country[0])
        sorted_countries.sort()
        for s in sorted_countries:
            for country in self.countries:
                if s in country:
                    self.listbox_country.insert(END, s + '(' + str(int(country[1])) + ')')

    def get_selected_countries(self):
        return self.listbox_country.curselection()  # from http://effbot.org/tkinterbook/listbox.htm

    def get_selected_criterias(self):
        return self.listbox_criterias.curselection()  # from http://effbot.org/tkinterbook/listbox.htm

    def clear_list_boxes(self):
        self.listbox_country.selection_clear(0, END)  # https://stackoverflow.com/questions/27158542/tkinter-listbox-change-highlighted-item-programmatically
        self.listbox_criterias.selection_clear(0, END)

    def display_on_canvas(self):
        load = Image.open("cl.jpeg")
        self.render = ImageTk.PhotoImage(load)
        self.canvas.create_image(0, 0, image=self.render, anchor=NW)

    def cluster_countries(self):
        data = Data(self.countries, self.criterias)
        cluster = Cluster()
        data.create_file(self.get_selected_countries(), self.get_selected_criterias())
        cluster.cluster_data()
        self.display_on_canvas()
        self.canvas.configure(scrollregion=(0, 0, self.render.width()+15, self.render.height()+15))  # taken from https://bytes.com/topic/python/answers/157174-how-get-scrollregion-adjust-w-window-size
        self.clear_list_boxes()

    def cluster_criterias(self):
        data = Data(self.countries, self.criterias)
        cluster = Cluster()  # cluster object
        data.create_file(self.get_selected_countries(), self.get_selected_criterias(), reverse=True)
        cluster.cluster_data()  # makes picture
        self.display_on_canvas()  # puts picture in canvas
        self.canvas.configure(scrollregion=(0, 0, self.render.width()+15, self.render.height()+15))
        self.clear_list_boxes()  # clears selection


root = Tk()
gui = Gui(root)
gui.user_interface()
root.title("Corona Virus Analyser Tool")
root.geometry("1050x550")
root.mainloop()
