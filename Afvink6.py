import mysql.connector
import tkinter


class GUI:
    def __init__(self):
        # Aanmaken main window met titel
        self.main_window = tkinter.Tk()
        self.main_window.title("Pypiep")

        # Aanmaken frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid1_frame.pack()
        self.bottom_frame.pack()

        # Aanmaken label
        self.label = tkinter.Label(self.top_frame,
                                   text="Bericht:")
        self.label.pack(side="left")

        # Maakt een text vak
        self.bericht_entry = tkinter.Entry(self.top_frame,
                                          width=30)
        self.bericht_entry.pack(side="left")

        # Maakt buttons
        self.send_button = tkinter.Button(self.top_frame,
                                          text="Verstuur",
                                          command=self.verstuur)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        self.filter_button = tkinter.Button(self.mid_frame,
                                            text="Filter op #",
                                            command=self.filter)

        self.ververs_button = tkinter.Button(self.mid_frame,
                                             text="Ververs",
                                             command=self.show)

        self.send_button.pack(side="right")
        self.quit_button.pack(side="right")
        self.filter_button.pack(side="right")
        self.ververs_button.pack(side="left")

        # Maakt leeg vak
        self.display = tkinter.Text(self.mid1_frame,
                                   width=100,height=30)

        self.display.pack()

        # Zorgt dat de GUI zichtbaar is
        tkinter.mainloop()


    def verstuur(self):
        """Verstuurt berichten, en voegt ze dus toe aan de database

        """

        berichtje = str(self.bericht_entry.get())

        conn = mysql.connector.connect(host=" 145.74.104.145",
                                       user="tombs",
                                       db="tombs",
                                       password="Aa638928!")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO piep(bericht, datum, tijd, student_nr) "
                       "VALUES('{}' ,curdate(), curtime(),638928)".format(berichtje))

        conn.commit()

        cursor.close()
        conn.close()

        self.bericht_entry.delete(0, tkinter.END)

    def show(self):
        """Laat de berichten uit de database zien

        """

        self.display.delete("1.0", tkinter.END)

        conn = mysql.connector.connect(host=" 145.74.104.145",
                                       user="tombs",
                                       db="tombs",
                                       password="Aa638928!")
        cursor = conn.cursor()
        cursor.execute("SELECT bericht FROM piep")

        rows = cursor.fetchall()

        self.display.insert("1.0", rows)

        cursor.close()
        conn.close()


    def filter(self):
        """Filtert in de database op #

        """

        self.display.delete("1.0", tkinter.END)

        conn = mysql.connector.connect(host=" 145.74.104.145",
                                       user="tombs",
                                       db="tombs",
                                       password="Aa638928!")
        cursor = conn.cursor()
        cursor.execute("SELECT bericht FROM piep WHERE bericht like '%#%'")

        rows = cursor.fetchall()

        self.display.insert("1.0", rows)

        cursor.close()
        conn.close()


if __name__ == '__main__':
    myGUI = GUI()