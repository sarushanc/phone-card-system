import os
import tempfile
from datetime import datetime
from itertools import chain
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import sqlite3
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.button import MDRoundFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.fitimage import FitImage

conn = sqlite3.connect('cards.db')
c = conn.cursor()


class LogIn(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        def logger(event):
            c.execute("SELECT user_name FROM users;")
            fetch_user = c.fetchall()
            x = list(chain(*fetch_user))
            if user_name.text in x:
                try:
                    c.execute("SELECT rowid FROM users where user_name = (?);", (user_name.text,))
                    user_id = c.fetchall()[0]
                    c.execute("SELECT rowid FROM users where password = (?);", (password.text,))
                    password_id = c.fetchall()[0]
                    if user_id == password_id:
                        self.label.text = f'Hello {user_name.text}!'
                        on_going.screen_manager.current = "buttons"
                    else:
                        popup = Popup(title='Your Password is Wrong!', size_hint=(0.25, 0.1))
                        popup.open()
                except (ValueError, IndexError):
                    popup = Popup(title='User Name or Password is Wrong!', size_hint=(0.25, 0.1))
                    popup.open()
            else:
                popup = Popup(title='Your User Name is Wrong!', size_hint=(0.25, 0.1))
                popup.open()

        def clear(event):
            self.label.text = "WELCOME"
            user_name.text = ""
            password.text = ""

        self.card = MDCard(size_hint=(None, None),
                           size=(300, 400),
                           pos_hint={"center_x": 0.5, "center_y": 0.5},
                           elevation=10,
                           padding=25,
                           spacing=25,
                           orientation='vertical')
        self.add_widget(self.card)

        self.label = Label(text="VISWAMS TRADERS", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                           outline_color=(1, 0, 0), outline_width=1,
                           pos_hint={'center_x': 0.5, 'center_y': 0.92},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(self.label)

        user_name = TextInput(multiline=False, hint_text="User Name", font_size=14,
                              pos_hint={'center_x': 0.5, 'center_y': 0.7},
                              size_hint=(dp(0.3), dp(0.1)))
        self.add_widget(user_name)

        password = TextInput(multiline=False, hint_text="Password", font_size=14,
                             pos_hint={'center_x': 0.5, 'center_y': 0.6}, password=True,
                             size_hint=(dp(0.3), dp(0.1)))
        self.add_widget(password)

        log_in = MDRoundFlatButton(text="LOG IN",
                                   font_size=12,
                                   pos_hint={"center_x": 0.5, 'center_y': 0.45},
                                   on_press=logger)
        self.add_widget(log_in)

        clear = MDRoundFlatButton(text="CLEAR",
                                  font_size=12,
                                  pos_hint={"center_x": 0.5, 'center_y': 0.3},
                                  on_press=clear)
        self.add_widget(clear)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class ButtonCard(Screen):
    # initiate infinite keywords
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        def bill(event):
            on_going.screen_manager.current = "bills"
            on_going.screen_manager.transition.direction = "left"

        def card_details(event):
            on_going.screen_manager.current = "cards"
            on_going.screen_manager.transition.direction = "left"

        def p_bills(event):
            on_going.screen_manager.current = "purchase bills"
            on_going.screen_manager.transition.direction = "left"

        def companies(event):
            on_going.screen_manager.current = "company"
            on_going.screen_manager.transition.direction = "left"

        def user(event):
            on_going.screen_manager.current = "user"
            on_going.screen_manager.transition.direction = "left"

        def purchasing(event):
            on_going.screen_manager.current = "purchase"
            on_going.screen_manager.transition.direction = "left"

        def sale(event):
            on_going.screen_manager.current = "sales"
            on_going.screen_manager.transition.direction = "left"

        def day(event):
            on_going.screen_manager.current = "day"
            on_going.screen_manager.transition.direction = "left"

        def about_us(event):
            on_going.screen_manager.current = "about"
            on_going.screen_manager.transition.direction = "left"

        # add buttons
        purchase = Button(text="Purchase", bold=True, font_size=20,
                          pos_hint={'center_x': 0.25, 'center_y': 0.9}, size_hint=(dp(0.5), dp(0.20)))
        purchase.bind(on_press=purchasing)
        self.add_widget(purchase)

        sales = Button(text="Sales", bold=True, font_size=20,
                       pos_hint={'center_x': 0.75, 'center_y': 0.9}, size_hint=(dp(0.5), dp(0.20)))
        sales.bind(on_press=sale)
        self.add_widget(sales)

        cards = Button(text="Card Details", bold=True, font_size=20,
                       pos_hint={'center_x': 0.25, 'center_y': 0.68}, size_hint=(dp(0.5), dp(0.20)))
        cards.bind(on_press=card_details)
        self.add_widget(cards)

        company = Button(text="Company", bold=True, font_size=20,
                         pos_hint={'center_x': 0.75, 'center_y': 0.68}, size_hint=(dp(0.5), dp(0.20)))
        company.bind(on_press=companies)
        self.add_widget(company)

        payments = Button(text="Purchased Bills", bold=True, font_size=20,
                          pos_hint={'center_x': 0.25, 'center_y': 0.46}, size_hint=(dp(0.5), dp(0.20)))
        payments.bind(on_press=p_bills)
        self.add_widget(payments)

        bills = Button(text="Sales Bills Records", bold=True, font_size=20,
                       pos_hint={'center_x': 0.75, 'center_y': 0.46}, size_hint=(dp(0.5), dp(0.20)))
        bills.bind(on_press=bill)
        self.add_widget(bills)

        users = Button(text="Users", bold=True, font_size=20,
                       pos_hint={'center_x': 0.25, 'center_y': 0.24}, size_hint=(dp(0.5), dp(0.20)))
        users.bind(on_press=user)
        self.add_widget(users)

        day_end = Button(text="Day End", bold=True, font_size=20,
                         pos_hint={'center_x': 0.75, 'center_y': 0.24}, size_hint=(dp(0.5), dp(0.20)))
        day_end.bind(on_press=day)
        self.add_widget(day_end)

        about = Button(text="About", bold=True, font_size=20,
                       pos_hint={'center_x': 0.5, 'center_y': 0.07}, size_hint=(dp(0.5), dp(0.1)))
        about.bind(on_press=about_us)
        self.add_widget(about)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class BillRecords(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        label = Label(text="Sales Bill Records", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3,
                      pos_hint={'center_x': 0.5, 'center_y': 0.92},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)
        c.execute("SELECT * FROM bills;")
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.6, 0.6),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Bill No", dp(20)),
                ("Date", dp(20)),
                ("Time", dp(20)),
                ("Amount", dp(20))
            ],
            row_data=c.fetchall())

        self.add_widget(table)

        def delete(event):
            try:
                c.execute("DELETE from bills WHERE bill_no = (?);", search.text)
                conn.commit()
                c.execute("SELECT * FROM bills;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.6, 0.6),
                    use_pagination=True,
                    rows_num=10,
                    column_data=[
                        ("Bill No", dp(20)),
                        ("Date", dp(20)),
                        ("Time", dp(20)),
                        ("Amount", dp(20))
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.ProgrammingError:
                popup = Popup(title='Enter A Valid Bill Number!', size_hint=(0.25, 0.1))
                popup.open()

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.55, 'center_y': 0.1}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b2)
        b2.bind(on_press=delete)

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        search = TextInput(multiline=False, hint_text="Bill No", font_size=14,
                           pos_hint={'center_x': 0.45, 'center_y': 0.1},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(search)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Cards(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )
        # define TAble
        label = Label(text="MOBILE CARD DETAILS", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3,
                      pos_hint={'center_x': 0.5, 'center_y': 0.9}, size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        c.execute("SELECT * FROM card;")
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.6),
            rows_num=10,
            use_pagination=True,
            column_data=[
                ("Card ID", dp(30)),
                ("Network", dp(25)),
                ("Card", dp(25)),
                ("Cost", dp(20)),
                ("Retail", dp(25)),
                ("Qty", dp(25)),
            ],
            row_data=c.fetchall())

        # Add new

        self.add_widget(table)

        c.execute("SELECT company FROM company;")
        fetch = c.fetchall()
        network = Spinner(text="Network",
                          values=(i[0] for i in fetch),
                          background_color=(0.7, 0.75, 0.7, 1),
                          size_hint=(dp(0.1), dp(0.05)),
                          pos_hint={'center_x': 0.24, 'center_y': 0.125})
        card_id = TextInput(multiline=False, hint_text="Card_ID", pos_hint={'center_x': 0.12, 'center_y': 0.125},
                            size_hint=(dp(0.1), dp(0.1)))
        card = TextInput(multiline=False, hint_text="Card Name", font_size=12,
                         pos_hint={'center_x': 0.36, 'center_y': 0.125},
                         size_hint=(dp(0.1), dp(0.1)))
        cost = TextInput(multiline=False, hint_text="Cost", pos_hint={'center_x': 0.48, 'center_y': 0.125},
                         size_hint=(dp(0.1), dp(0.1)))
        retail = TextInput(multiline=False, hint_text="Retail", pos_hint={'center_x': 0.6, 'center_y': 0.125},
                           size_hint=(dp(0.1), dp(0.1)))
        qty = TextInput(multiline=False, hint_text="Qty", pos_hint={'center_x': 0.72, 'center_y': 0.125},
                        size_hint=(dp(0.1), dp(0.1)))

        self.add_widget(network)
        self.add_widget(card_id)
        self.add_widget(card)
        self.add_widget(cost)
        self.add_widget(retail)
        self.add_widget(qty)

        try:
            c.execute("SELECT card_id FROM card ORDER BY card_id DESC LIMIT 1;")
            old_bill = int(c.fetchall()[0][0])
            card_id.text = str(old_bill + 1)
        except IndexError:
            card_id.text = "1"

        def add_item(event):
            try:
                c.execute("INSERT INTO card VALUES (?,?,?,?,?,?);",
                          (card_id.text, network.text, card.text, cost.text, retail.text, qty.text))
                conn.commit()
                c.execute("SELECT * FROM card;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.9, 0.6),
                    rows_num=10,
                    use_pagination=True,
                    column_data=[
                        ("Card ID", dp(30)),
                        ("Network", dp(25)),
                        ("Card", dp(25)),
                        ("Cost", dp(20)),
                        ("Retail", dp(25)),
                        ("Qty", dp(25)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
                card_id.text = ""
                card.text = ""
                cost.text = ""
                retail.text = ""
                qty.text = ""
            except sqlite3.IntegrityError:
                popup = Popup(title='Enter The Details!', size_hint=(0.3, 0.1))
                popup.open()

        def delete(event):
            try:
                c.execute("DELETE from card WHERE rowid = (?);", card_id.text)
                conn.commit()
                c.execute("SELECT * FROM card;")
                conn.commit()
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.9, 0.6),
                    rows_num=10,
                    use_pagination=True,
                    column_data=[
                        ("Card ID", dp(30)),
                        ("Network", dp(25)),
                        ("Card", dp(25)),
                        ("Cost", dp(20)),
                        ("Retail", dp(25)),
                        ("Qty", dp(25)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.ProgrammingError:
                popup = Popup(title='Enter a Valid Card_ID to Delete!', size_hint=(0.3, 0.1))
                popup.open()

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.12, 'center_y': 0.05}, size_hint=(dp(0.1), dp(0.05)))
        b2.bind(on_press=delete)

        b3 = Button(text="ADD NEW", pos_hint={'center_x': 0.875, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.05)))
        b3.bind(on_press=add_item)

        self.add_widget(b2)
        self.add_widget(b3)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class PurBills(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        label = Label(text="Closed Purchase_Bills", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3,
                      pos_hint={'center_x': 0.5, 'center_y': 0.9},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)
        c.execute("SELECT * FROM payment;")
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.7),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Bill No", dp(20)),
                ("Invoice No", dp(20)),
                ("Date", dp(20)),
                ("Company", dp(20)),
                ("Payment", dp(20)),
                ("Method", dp(20))
            ],
            row_data=c.fetchall())

        self.add_widget(table)

        def delete(event):
            c.execute("DELETE from payment WHERE bill_no = (?);", (search.text,))
            conn.commit()
            c.execute("SELECT * FROM payment;")
            table1 = MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(0.8, 0.7),
                use_pagination=True,
                rows_num=10,
                column_data=[
                    ("Bill No", dp(20)),
                    ("Invoice No", dp(20)),
                    ("Date", dp(20)),
                    ("Company", dp(20)),
                    ("Payment", dp(20)),
                    ("Method", dp(20))
                ],
                row_data=c.fetchall())
            self.add_widget(table1)

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.2, 'center_y': 0.1}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b2)
        b2.bind(on_press=delete)

        search = TextInput(multiline=False, hint_text="ID", font_size=14,
                           pos_hint={'center_x': 0.1, 'center_y': 0.1},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(search)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Company(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        # define TAble
        label = Label(text="COMPANIES", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3, pos_hint={'center_x': 0.5, 'center_y': 0.9},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        c.execute("SELECT * FROM company;")
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.6, 0.6),
            rows_num=10,
            column_data=[
                ("Company ID", dp(50)),
                ("Company", dp(50)),
            ],
            row_data=c.fetchall())

        self.add_widget(table)

        com_id = TextInput(multiline=False, hint_text="Company ID", font_size=12,
                           pos_hint={'center_x': 0.525, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(com_id)
        company = TextInput(multiline=False, hint_text="Company", pos_hint={'center_x': 0.65, 'center_y': 0.125},
                            size_hint=(dp(0.15), dp(0.1)))
        self.add_widget(company)
        search = TextInput(multiline=False, hint_text="ID",
                           pos_hint={'center_x': 0.225, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(search)

        def add_item(event):
            try:
                c.execute("INSERT INTO company VALUES (?,?);",
                          (com_id.text, company.text))
                conn.commit()
                c.execute("SELECT * FROM company;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.6, 0.6),
                    rows_num=10,
                    column_data=[
                        ("Company ID", dp(50)),
                        ("Company", dp(50)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.IntegrityError:
                popup = Popup(title='Enter Details!', size_hint=(0.17, 0.1))
                popup.open()

        def delete(event):
            try:
                c.execute("DELETE from company WHERE rowid = (?);", search.text)
                conn.commit()
                c.execute("SELECT * FROM company;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.6, 0.6),
                    rows_num=10,
                    column_data=[
                        ("Company ID", dp(50)),
                        ("Company", dp(50)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.ProgrammingError:
                popup = Popup(title='Enter Company ID!', size_hint=(0.2, 0.1))
                popup.open()

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.325, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.075)))
        b2.bind(on_press=delete)

        b3 = Button(text="ADD NEW", pos_hint={'center_x': 0.775, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.075)))
        b3.bind(on_press=add_item)

        self.add_widget(b2)
        self.add_widget(b3)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class User(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )
        label = Label(text="USERS", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3, pos_hint={'center_x': 0.5, 'center_y': 0.9},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        c.execute("SELECT rowid, * FROM users;")
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.6, 0.6),
            rows_num=10,
            column_data=[
                ("ID", dp(20)),
                ("User Name", dp(20)),
                ("Password", dp(20)),
            ],
            row_data=c.fetchall())

        # Add new
        self.add_widget(table)

        username = TextInput(multiline=False, hint_text="User Name", font_size=12,
                             pos_hint={'center_x': 0.525, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(username)
        password = TextInput(multiline=False, hint_text="Password", pos_hint={'center_x': 0.65, 'center_y': 0.125},
                             size_hint=(dp(0.15), dp(0.1)))
        self.add_widget(password)
        row_id = TextInput(multiline=False, hint_text="ID",
                           pos_hint={'center_x': 0.225, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(row_id)

        def add_item(event):
            try:
                c.execute("INSERT INTO users VALUES (?,?);",
                          (username.text, password.text))
                conn.commit()
                c.execute("SELECT rowid, * FROM users;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.6, 0.6),
                    rows_num=10,
                    column_data=[
                        ("ID", dp(20)),
                        ("User Name", dp(20)),
                        ("Password", dp(20)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.IntegrityError:
                popup = Popup(title='Enter Details!', size_hint=(0.17, 0.1))
                popup.open()

        def delete(event):
            try:
                c.execute("DELETE from users WHERE rowid = (?);", row_id.text)
                conn.commit()
                c.execute("SELECT rowid, * FROM users;")
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.6, 0.6),
                    rows_num=10,
                    column_data=[
                        ("ID", dp(20)),
                        ("User Name", dp(20)),
                        ("Password", dp(20)),
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.ProgrammingError:
                popup = Popup(title='Enter Company ID!', size_hint=(0.2, 0.1))
                popup.open()

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.325, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.075)))
        b2.bind(on_press=delete)

        b3 = Button(text="ADD NEW", pos_hint={'center_x': 0.775, 'center_y': 0.125}, size_hint=(dp(0.1), dp(0.075)))
        b3.bind(on_press=add_item)

        self.add_widget(b2)
        self.add_widget(b3)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Purchase(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos)

        label = Label(text="PURCHASE", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3,
                      pos_hint={'center_x': 0.7, 'center_y': 0.92},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        card_label = Label(text="Item", font_size=14, pos_hint={'center_x': 0.2, 'center_y': 0.7},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(card_label)

        card_stock = Label(text="Qty", font_size=14, pos_hint={'center_x': 0.4, 'center_y': 0.7},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(card_stock)

        price = Label(text="Price:", font_size=14, pos_hint={'center_x': 0.8, 'center_y': 0.7},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(price)

        cost = Label(text="Cost:", font_size=14, pos_hint={'center_x': 0.6, 'center_y': 0.7},
                     size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(cost)

        date_label = Label(text="Date", font_size=14, pos_hint={'center_x': 0.125, 'center_y': 0.9},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(date_label)
        t_price = Label(text="Total Price", font_size=14,
                        pos_hint={'center_x': 0.4, 'center_y': 0.05},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(t_price)

        def close_p(event):
            try:
                c.execute("INSERT INTO payment VALUES (?,?,?,?,?,?);",
                          (grn.text, invoice.text, date_label.text, network.text, t_price.text, pay_method.text))
                conn.commit()

                c.execute("SELECT rowid, company, card, cost, qty, total FROM purchase WHERE bill_no = (?);",
                          (grn.text,))
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.4},
                    size_hint=(0.9, 0.5),
                    use_pagination=True,
                    rows_num=10,
                    column_data=[
                        ("ID", dp(10)),
                        ("Network", dp(20)),
                        ("Card", dp(15)),
                        ("Cost", dp(15)),
                        ("Qty", dp(15)),
                        ("Price", dp(15))
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.IntegrityError:
                popup = Popup(title='The Bill Already Closed!', size_hint=(0.25, 0.1))
                popup.open()

        def date_picker(event):
            date_dialog = MDDatePicker()
            date_dialog.bind(on_save=on_save)
            date_dialog.open()

        def on_save(instance, value, date_range):
            date_label.text = str(value)

        def add_item(event):
            try:
                c.execute("SELECT bill_no FROM payment;")
                fetch_rowid = c.fetchall()
                x = list(chain(*fetch_rowid))
                if int(grn.text) in x:
                    popup = Popup(title='The Bill Have Been Closed!', size_hint=(0.25, 0.1))
                    popup.open()
                else:
                    c.execute("INSERT INTO purchase VALUES (?,?,?,?,?,?,?,?);",
                              (grn.text, invoice.text, card_label.text, network.text, date_label.text, cost.text,
                               qty.text,
                               int(cost.text) * int(qty.text)))
                    conn.commit()

                    c.execute("SELECT qty FROM card WHERE card = (?);", (card_label.text,))
                    old_qty = int(c.fetchall()[0][0])
                    new_qty = old_qty + int(qty.text)
                    c.execute("UPDATE card SET qty = ? WHERE card = ?;", (new_qty, card_label.text))
                    conn.commit()

                    c.execute("SELECT rowid, company, card, cost, qty, total FROM purchase WHERE bill_no = (?);",
                              (grn.text,))
                    table1 = MDDataTable(
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        size_hint=(0.9, 0.5),
                        use_pagination=True,
                        rows_num=10,
                        column_data=[
                            ("ID", dp(10)),
                            ("Network", dp(20)),
                            ("Card", dp(15)),
                            ("Cost", dp(15)),
                            ("Qty", dp(15)),
                            ("Price", dp(15))
                        ],
                        row_data=c.fetchall())
                    self.add_widget(table1)

                    card_stock.text = "Stock: " + str(new_qty)

                    c.execute("SELECT SUM(total) FROM purchase WHERE bill_no = (?);", (grn.text,))
                    fetch_price1 = c.fetchall()
                    t_price.text = str(fetch_price1[0][0])
            except ValueError:
                popup = Popup(title='Enter Valid Input!', size_hint=(0.25, 0.1))
                popup.open()

        def delete(event):
            try:
                c.execute("SELECT bill_no FROM payment;")
                fetch_rowid = c.fetchall()
                x = list(chain(*fetch_rowid))
                if int(grn.text) in x:
                    popup = Popup(title='The Bill Have Been Closed!', size_hint=(0.25, 0.1))
                    popup.open()
                else:
                    c.execute("SELECT card FROM purchase WHERE rowid = (?);", (search.text,))
                    old_qty = c.fetchall()[0][0]
                    c.execute("SELECT qty FROM card WHERE card = (?);", (old_qty,))
                    o_qty = str(c.fetchall()[0][0])
                    c.execute("SELECT qty FROM purchase WHERE rowid = (?);", (search.text,))
                    un_qty = c.fetchall()[0][0]
                    new_qty = int(o_qty) - int(un_qty)
                    c.execute("UPDATE card SET qty = ? WHERE card = ?;", (new_qty, old_qty))
                    conn.commit()

                    c.execute("DELETE from purchase WHERE rowid = (?);", [search.text])
                    conn.commit()

                    c.execute("SELECT rowid, company, card, cost, qty, total FROM purchase WHERE bill_no = (?);",
                              (grn.text,))
                    table1 = MDDataTable(
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        size_hint=(0.9, 0.5),
                        use_pagination=True,
                        rows_num=10,
                        column_data=[
                            ("ID", dp(10)),
                            ("Network", dp(20)),
                            ("Card", dp(15)),
                            ("Cost", dp(15)),
                            ("Qty", dp(15)),
                            ("Price", dp(15))
                        ],
                        row_data=c.fetchall())

                    self.add_widget(table1)

                    card_stock.text = "Stock: " + str(new_qty)

                    c.execute("SELECT SUM(total) FROM purchase WHERE bill_no = (?);", (grn.text,))
                    fetch_price1 = c.fetchall()
                    t_price.text = str(fetch_price1[0][0])
            except (ValueError, IndexError):
                popup = Popup(title='Enter Valid ID!', size_hint=(0.25, 0.1))
                popup.open()

        def number(instance, value):
            c.execute("SELECT rowid, company, card, cost, qty, total FROM purchase WHERE bill_no = (?);", (grn.text,))
            table1 = MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                size_hint=(0.9, 0.5),
                use_pagination=True,
                rows_num=10,
                column_data=[
                    ("ID", dp(10)),
                    ("Network", dp(20)),
                    ("Card", dp(15)),
                    ("Cost", dp(15)),
                    ("Qty", dp(15)),
                    ("Price", dp(15))
                ],
                row_data=c.fetchall())
            self.add_widget(table1)

            try:
                c.execute("SELECT company FROM payment WHERE bill_no = (?);", (grn.text,))
                fetch_com = c.fetchall()
                card_label.text = str(fetch_com[0][0])
            except IndexError:
                card_label.text = ""

            card_stock.text = ""
            cost.text = ""
            qty.text = ""

            try:
                c.execute("SELECT invoice FROM purchase WHERE bill_no = ?;", [grn.text])
                fetch_in = c.fetchall()
                invoice.text = fetch_in[0][0]
            except IndexError:
                invoice.text = ""

            c.execute("SELECT SUM(total) FROM purchase WHERE bill_no = (?);", (grn.text,))
            fetch_price1 = c.fetchall()
            t_price.text = str(fetch_price1[0][0])

        def printer(event):
            printing = "welcome"
            print_it = tempfile.mktemp(".txt")
            open(print_it, "w").write(printing)
            os.startfile(print_it, "print")

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        # input boxes
        qty = TextInput(multiline=False, hint_text="Qty", font_size=14, pos_hint={'center_x': 0.725, 'center_y': 0.8},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(qty)

        grn = TextInput(multiline=False, hint_text="GRN", font_size=14,
                        pos_hint={'center_x': 0.325, 'center_y': 0.9},
                        size_hint=(dp(0.1), dp(0.08)))
        self.add_widget(grn)

        c.execute("SELECT SUM(total) FROM purchase WHERE bill_no = (?);", (grn.text,))
        fetch_price = c.fetchall()
        t_price.text = str(fetch_price[0][0])

        try:
            c.execute("SELECT bill_no FROM payment ORDER BY bill_no DESC LIMIT 1;")
            old_bill = int(c.fetchall()[0][0])
            grn.text = str(old_bill + 1)
        except IndexError:
            grn.text = "1"
        grn.bind(text=number)

        invoice = TextInput(multiline=False, hint_text="Invoice Ref.", font_size=14,
                            pos_hint={'center_x': 0.325, 'center_y': 0.8},
                            size_hint=(dp(0.175), dp(0.1)))
        c.execute("SELECT invoice FROM purchase WHERE bill_no = ?;", [grn.text])
        fetchall = c.fetchall()
        self.add_widget(invoice)
        try:
            invoice.text = fetchall[0][0]
        except IndexError:
            invoice.text = ""

        search = TextInput(multiline=False, hint_text="ID", font_size=14,
                           pos_hint={'center_x': 0.1, 'center_y': 0.1},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(search)
        # buttons
        b1 = Button(text="SUBMIT", font_size=10, pos_hint={'center_x': 0.85, 'center_y': 0.8},
                    size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b1)
        b1.bind(on_press=add_item)

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.2, 'center_y': 0.1}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b2)
        b2.bind(on_press=delete)

        b = Button(text="PRINT", pos_hint={'center_x': 0.9, 'center_y': 0.05}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b)
        b.bind(on_press=printer)

        close = Button(text="Close", pos_hint={'center_x': 0.78, 'center_y': 0.05}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(close)
        close.bind(on_press=close_p)

        # calender
        date = MDRaisedButton(text="Pick Date", pos_hint={'center_x': 0.15, 'center_y': 0.8}, on_press=date_picker,
                              size_hint=(dp(0.05), dp(0.05)))
        self.add_widget(date)

        # drop down lists
        c.execute("SELECT company FROM company;")
        fetch = c.fetchall()
        network = Spinner(text="Network",
                          values=(i[0] for i in fetch),
                          background_color=(0.7, 0.75, 0.7, 1),
                          size_hint=(dp(0.1), dp(0.05)),
                          pos_hint={'center_x': 0.475, 'center_y': 0.8})

        def select(spinner, text):
            c.execute("SELECT card FROM card WHERE network = ?;", [text])
            fetch1 = c.fetchall()
            card = Spinner(text=card_label.text,
                           values=(i[0] for i in fetch1),
                           background_color=(0, 1, 1, .5),
                           size_hint=(dp(0.1), dp(0.05)),
                           pos_hint={'center_x': 0.6, 'center_y': 0.8})
            self.add_widget(card)

            def item_label(event, data):
                card_label.text = str(card.text)
                c.execute("SELECT qty FROM card WHERE card = ?;", [card_label.text])
                fetch_q = c.fetchall()
                card_stock.text = "Stock: " + str(fetch_q[0][0])

                c.execute("SELECT cost FROM card WHERE card = ?;", [card_label.text])
                fetch_cost = c.fetchall()
                cost.text = str(fetch_cost[0][0])

            card.bind(text=item_label)

            def labeling(event, data):
                try:
                    c.execute("SELECT cost FROM card WHERE card = ?;", [card_label.text])
                    fetch_cost = c.fetchall()
                    price.text = str(int(fetch_cost[0][0]) * int(qty.text))
                except (ValueError, IndexError):
                    qty.text = "0"

            qty.bind(text=labeling)

        self.add_widget(network)
        network.bind(text=select)

        pay_method = Spinner(text="Payment",
                             values=("Cheque", "Cash"),
                             background_color=(0.7, 0.75, 0.7, 1),
                             size_hint=(dp(0.1), dp(0.05)),
                             pos_hint={'center_x': 0.6, 'center_y': 0.05})
        self.add_widget(pay_method)

        c.execute("SELECT rowid, company, card, cost, qty, total FROM purchase WHERE bill_no = (?);", (grn.text,))
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint=(0.9, 0.5),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("ID", dp(10)),
                ("Network", dp(20)),
                ("Card", dp(15)),
                ("Cost", dp(15)),
                ("Qty", dp(15)),
                ("Price", dp(15))
            ],
            row_data=c.fetchall())

        self.add_widget(table)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Sales(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos)

        label = Label(text="SALES", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3,
                      pos_hint={'center_x': 0.5, 'center_y': 0.92},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        card_label = Label(text="Item", font_size=15, pos_hint={'center_x': 0.2, 'center_y': 0.7},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(card_label)

        card_stock = Label(text="Qty", font_size=15, pos_hint={'center_x': 0.4, 'center_y': 0.7},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(card_stock)

        price = Label(text="Price:", font_size=15, pos_hint={'center_x': 0.8, 'center_y': 0.7},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(price)

        cost = Label(text="Cost:", font_size=15, pos_hint={'center_x': 0.6, 'center_y': 0.7},
                     size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(cost)

        today = datetime.today()
        d1 = today.strftime("%d/%m/%y")
        t1 = today.strftime("%I:%M%p")
        date_label = Label(text=d1, font_size=14, pos_hint={'center_x': 0.3, 'center_y': 0.95},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(date_label)
        time_label = Label(text=t1, font_size=14, pos_hint={'center_x': 0.3, 'center_y': 0.9},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(time_label)

        t_price = Label(text="", font_size=15,
                        pos_hint={'center_x': 0.35, 'center_y': 0.05},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(t_price)

        t_label = Label(text="Gross Amount", font_size=15,
                        pos_hint={'center_x': 0.35, 'center_y': 0.1},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(t_label)

        def close_p(event):
            try:
                c.execute("INSERT INTO bills VALUES (?,?,?,?);",
                          (grn.text, date_label.text, time_label.text, t_price.text))
                conn.commit()

                c.execute("SELECT rowid, company, card, retail, qty, total FROM sales WHERE bill_no = (?);",
                          (grn.text,))
                table1 = MDDataTable(
                    pos_hint={'center_x': 0.5, 'center_y': 0.4},
                    size_hint=(0.9, 0.5),
                    use_pagination=True,
                    rows_num=10,
                    column_data=[
                        ("ID", dp(15)),
                        ("Network", dp(30)),
                        ("Card", dp(20)),
                        ("Cost", dp(20)),
                        ("Qty", dp(20)),
                        ("Price", dp(20))
                    ],
                    row_data=c.fetchall())
                self.add_widget(table1)
            except sqlite3.IntegrityError:
                popup = Popup(title='The Bill Already Closed!', size_hint=(0.25, 0.1))
                popup.open()
            try:
                c.execute("SELECT bill_no FROM bills ORDER BY bill_no DESC LIMIT 1;")
                old_bill1 = int(c.fetchall()[0][0])
                grn.text = str(old_bill1 + 1)
            except IndexError:
                grn.text = "1"
            card_label.text = ""

        def add_item(event):
            c.execute("SELECT bill_no FROM bills;")
            fetch_rowid = c.fetchall()
            x = list(chain(*fetch_rowid))
            try:
                if grn.text in x:
                    popup = Popup(title='The Bill Have Been Closed!', size_hint=(0.25, 0.1))
                    popup.open()
                else:
                    c.execute("INSERT INTO sales VALUES (?,?,?,?,?,?,?);",
                              (grn.text, card_label.text, network.text, date_label.text, cost.text, qty.text,
                               int(cost.text) * int(qty.text)))
                    conn.commit()

                    c.execute("SELECT qty FROM card WHERE card = (?);", (card_label.text,))
                    old_qty = int(c.fetchall()[0][0])

                    new_qty = old_qty - int(qty.text)
                    c.execute("UPDATE card SET qty = ? WHERE card = ?;", (new_qty, card_label.text))
                    conn.commit()

                    c.execute("SELECT rowid, company, card, retail, qty, total FROM sales WHERE bill_no = (?);",
                              (grn.text,))
                    table1 = MDDataTable(
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        size_hint=(0.9, 0.5),
                        use_pagination=True,
                        rows_num=10,
                        column_data=[
                            ("ID", dp(15)),
                            ("Network", dp(30)),
                            ("Card", dp(20)),
                            ("Cost", dp(20)),
                            ("Qty", dp(20)),
                            ("Price", dp(20))
                        ],
                        row_data=c.fetchall())
                    self.add_widget(table1)

                    card_stock.text = "Stock: " + str(new_qty)
                    c.execute("SELECT SUM(total) FROM sales WHERE bill_no = (?);", (grn.text,))
                    fetch_price1 = c.fetchall()
                    t_price.text = str(fetch_price1[0][0])
            except ValueError:
                popup = Popup(title='Enter Valid Input!', size_hint=(0.25, 0.1))
                popup.open()

        def delete(event):
            c.execute("SELECT bill_no FROM bills;")
            fetch_rowid = c.fetchall()
            x = list(chain(*fetch_rowid))
            try:
                if grn.text in x:
                    popup = Popup(title='The Bill Have Been Closed!', size_hint=(0.25, 0.1))
                    popup.open()
                else:
                    c.execute("SELECT card FROM sales WHERE rowid = (?);", (search.text,))
                    old_qty = c.fetchall()[0][0]
                    c.execute("SELECT qty FROM card WHERE card = (?);", (old_qty,))
                    o_qty = str(c.fetchall()[0][0])
                    c.execute("SELECT qty FROM sales WHERE rowid = (?);", (search.text,))
                    un_qty = c.fetchall()[0][0]
                    new_qty = int(o_qty) + int(un_qty)

                    c.execute("UPDATE card SET qty = ? WHERE card = ?;", (new_qty, old_qty))
                    conn.commit()

                    c.execute("DELETE from sales WHERE rowid = (?);", [search.text])
                    conn.commit()

                    c.execute("SELECT rowid, company, card, retail, qty, total FROM sales WHERE bill_no = (?);",
                              (grn.text,))
                    table1 = MDDataTable(
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        size_hint=(0.9, 0.5),
                        use_pagination=True,
                        rows_num=10,
                        column_data=[
                            ("ID", dp(15)),
                            ("Network", dp(30)),
                            ("Card", dp(20)),
                            ("Cost", dp(20)),
                            ("Qty", dp(20)),
                            ("Price", dp(20))
                        ],
                        row_data=c.fetchall())
                    self.add_widget(table1)
                    search.text = ""

                    card_stock.text = "Stock: " + str(new_qty)
                    c.execute("SELECT SUM(total) FROM sales WHERE bill_no = (?);", (grn.text,))
                    fetch_price1 = c.fetchall()
                    t_price.text = str(fetch_price1[0][0])
            except ValueError:
                popup = Popup(title='Enter Valid Input!', size_hint=(0.25, 0.1))
                popup.open()

        def number(instance, value):
            c.execute("SELECT rowid, company, card, retail, qty, total FROM sales WHERE bill_no = (?);", (grn.text,))
            table1 = MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                size_hint=(0.9, 0.5),
                use_pagination=True,
                rows_num=10,
                column_data=[
                    ("ID", dp(15)),
                    ("Network", dp(30)),
                    ("Card", dp(20)),
                    ("Cost", dp(20)),
                    ("Qty", dp(20)),
                    ("Price", dp(20))
                ],
                row_data=c.fetchall())
            self.add_widget(table1)
            card_stock.text = ""
            cost.text = ""
            price.text = ""
            qty.text = ""
            c.execute("SELECT SUM(total) FROM sales WHERE bill_no = (?);", (grn.text,))
            fetch_price1 = c.fetchall()
            t_price.text = str(fetch_price1[0][0])

        # input boxes
        qty = TextInput(multiline=False, hint_text="Qty", font_size=14, pos_hint={'center_x': 0.65, 'center_y': 0.8},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(qty)

        grn = TextInput(multiline=False, text="Bill No.", font_size=14,
                        pos_hint={'center_x': 0.1, 'center_y': 0.9},
                        size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(grn)

        try:
            c.execute("SELECT bill_no FROM bills ORDER BY bill_no DESC LIMIT 1;")
            old_bill = int(c.fetchall()[0][0])
            grn.text = str(old_bill + 1)
        except IndexError:
            grn.text = "1"

        grn.bind(text=number)

        c.execute("SELECT SUM(total) FROM sales WHERE bill_no = (?);", (grn.text,))
        fetch_price = c.fetchall()
        t_price.text = str(fetch_price[0][0])

        search = TextInput(multiline=False, hint_text="ID", font_size=12,
                           pos_hint={'center_x': 0.1, 'center_y': 0.1},
                           size_hint=(dp(0.1), dp(0.08)))
        self.add_widget(search)

        def printer(event):
            name = "VISWAMS TRADERS"

            c.execute("SELECT card, qty, total FROM sales WHERE bill_no = (?);", (grn.text,))
            print_item = c.fetchall()
            data = ""
            for i in print_item:
                data = data + "\n   " + str(i[0]) + "X" + str(i[1]) + " \t| " + str(i[2])

            c.execute("SELECT SUM(total) FROM sales WHERE bill_no = (?);", (grn.text,))
            fetch_price1 = c.fetchall()
            total_price = "\tTotal Amount: " + str(fetch_price1[0][0])

            printing = f'   {date_label.text}\t{time_label.text}\n\t{name}\n {data}\n\n {total_price}'

            print_it = tempfile.mktemp(".txt")
            open(print_it, "w").write(printing)
            os.startfile(print_it, "print")

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

        def today_sale(event):
            layout = GridLayout(cols=1, padding=10)

            c.execute("SELECT card, qty, total FROM sales WHERE date = (?);", (date_label.text,))
            print_item = c.fetchall()
            card_sell = ""
            for i in print_item:
                card_sell = card_sell + "\n   " + str(i[0]) + "X" + str(i[1]) + " ==>| " + str(i[2])

            sales = Label(text=card_sell, font_size=14, pos_hint={'center_x': 0.3, 'center_y': 0.9},
                          size_hint=(dp(0.1), dp(0.1)))
            layout.add_widget(sales)
            popup = Popup(title='Sales!', content=layout, size_hint=(0.25, 0.1))
            popup.open()

        # buttons
        b1 = Button(text="SUBMIT", pos_hint={'center_x': 0.8, 'center_y': 0.8}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b1)
        b1.bind(on_press=add_item)

        b2 = Button(text="DELETE", pos_hint={'center_x': 0.2, 'center_y': 0.1}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b2)
        b2.bind(on_press=delete)

        b = Button(text="PRINT", pos_hint={'center_x': 0.9, 'center_y': 0.05}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(b)
        b.bind(on_press=printer)

        close = Button(text="Close", pos_hint={'center_x': 0.78, 'center_y': 0.05}, size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(close)
        close.bind(on_press=close_p)

        today_sales = Button(text="Today sales", pos_hint={'center_x': 0.66, 'center_y': 0.05},
                             size_hint=(dp(0.1), dp(0.05)))
        self.add_widget(today_sales)
        today_sales.bind(on_press=today_sale)

        # drop down lists
        c.execute("SELECT company FROM company;")
        fetch = c.fetchall()
        network = Spinner(text="Network",
                          values=(i[0] for i in fetch),
                          background_color=(0.7, 0.75, 0.7, 1),
                          size_hint=(dp(0.1), dp(0.05)),
                          pos_hint={'center_x': 0.4, 'center_y': 0.8})

        def select(spinner, text):
            c.execute("SELECT card FROM card WHERE network = ?;", [text])
            fetch1 = c.fetchall()
            card = Spinner(text=card_label.text,
                           values=(i[0] for i in fetch1),
                           background_color=(0, 1, 1, .5),
                           size_hint=(dp(0.1), dp(0.05)),
                           pos_hint={'center_x': 0.525, 'center_y': 0.8})
            self.add_widget(card)

            def item_label(event, data):
                card_label.text = str(card.text)
                c.execute("SELECT qty FROM card WHERE card = ?;", [card_label.text])
                fetchall = c.fetchall()
                card_stock.text = "Stock: " + str(fetchall[0][0])

                c.execute("SELECT retail FROM card WHERE card = ?;", [card_label.text])
                fetch_cost = c.fetchall()
                cost.text = str(fetch_cost[0][0])

            card.bind(text=item_label)

            def labeling(event, data):
                try:
                    c.execute("SELECT retail FROM card WHERE card = ?;", [card_label.text])
                    fetch_cost = c.fetchall()
                    price.text = str(int(fetch_cost[0][0]) * int(qty.text))
                except (ValueError, IndexError):
                    qty.text = "0"

            qty.bind(text=labeling)

        self.add_widget(network)
        network.bind(text=select)

        c.execute("SELECT rowid, company, card, retail, qty, total FROM sales WHERE bill_no = (?);", (grn.text,))
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint=(0.9, 0.5),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("ID", dp(15)),
                ("Network", dp(30)),
                ("Card", dp(20)),
                ("Cost", dp(20)),
                ("Qty", dp(20)),
                ("Price", dp(20))
            ],
            row_data=c.fetchall())

        self.add_widget(table)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class DayEnd(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )

        # define TAble
        label = Label(text="Day End", font_size=25, color=(.5, .5, 1, 1), font_name='Comic', bold=True,
                      outline_color=(1, 0, 0), outline_width=3, pos_hint={'center_x': 0.5, 'center_y': 0.9},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        date_label = Label(text="Date", font_size=14, pos_hint={'center_x': 0.125, 'center_y': 0.9},
                           size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(date_label)

        sales = Label(text="Total Sales: ", font_size=20, pos_hint={'center_x': 0.3, 'center_y': 0.7},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(sales)

        purchase = Label(text="Total Purchase: ", font_size=20, pos_hint={'center_x': 0.3, 'center_y': 0.5},
                         size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(purchase)

        sales_amount = Label(text="", font_size=20, pos_hint={'center_x': 0.7, 'center_y': 0.7},
                             size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(sales_amount)

        purchase_amount = Label(text="", font_size=20, pos_hint={'center_x': 0.7, 'center_y': 0.5},
                                size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(purchase_amount)

        profit = Label(text="", font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.3},
                       size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(profit)

        def date_picker(event):
            date_dialog = MDDatePicker()
            date_dialog.bind(on_save=on_save)
            date_dialog.open()

        def on_save(instance, value, date_range):
            date_label.text = str(value)

            c.execute("SELECT SUM(total) FROM purchase WHERE date = (?);", (value,))
            fetch_purchase = c.fetchall()
            purchase_amount.text = str(fetch_purchase[0][0])

            c.execute("SELECT SUM(total) FROM sales WHERE date = (?);", (value,))
            fetch_sales = c.fetchall()
            sales_amount.text = str(fetch_sales[0][0])

            try:
                profit.text = "Profit: " + str(fetch_sales[0][0] - fetch_purchase[0][0])
            except TypeError:
                profit.text = "None"

        date = MDRaisedButton(text="Pick Date", pos_hint={'center_x': 0.15, 'center_y': 0.8}, on_press=date_picker,
                              size_hint=(dp(0.05), dp(0.05)))
        self.add_widget(date)

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class About(Screen):
    # initiate infinite keywords
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.bind(
            size=self._update_rect,
            pos=self._update_rect
        )
        with self.canvas.before:
            Color(.25, .25, .25, 1)
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos)

        label = Label(text="About Us!", font_size=25, bold=True,
                      outline_color=(1, 0, 0), outline_width=3, pos_hint={'center_x': 0.5, 'center_y': 0.9},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        text = "Mobil Card Manager v0.1\n\n©copyrights only to and Developed by " \
               "Chandrasekar Sharushan & Thanoj Pushpakumar\n\nContact Details:\n          " \
               "Phone: +94769980662\n                         +94766481240\n                         " \
               "+94758202743\n          " \
               "E-Mail: sarushan1994@gmail.com\n          Address: 23/A/1, " \
               "Kajugaswatta, Amunuwalapitiya, Badulla, Sri Lanka\n\nDeveloped on 10/10/2021"

        label = Label(text=text, font_size=14, pos_hint={'center_x': 0.5, 'center_y': 0.5},
                      size_hint=(dp(0.1), dp(0.1)))
        self.add_widget(label)

        def close(event):
            on_going.screen_manager.current = "buttons"
            on_going.screen_manager.transition.direction = "right"

        home = Button(text="X", pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(dp(0.05), dp(0.05)),
                      font_size=25, color=(1, 1, 1, 1), bold=True)
        self.add_widget(home)
        home.bind(on_press=close)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class AwesomeApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        self.log_in = LogIn()
        screen = Screen(name="log_in")
        screen.add_widget(self.log_in)
        self.screen_manager.add_widget(screen)

        self.buttons = ButtonCard()
        screen = Screen(name="buttons")
        screen.add_widget(self.buttons)
        self.screen_manager.add_widget(screen)

        self.bills = BillRecords()
        screen = Screen(name="bills")
        screen.add_widget(self.bills)
        self.screen_manager.add_widget(screen)

        self.card = Cards()
        screen = Screen(name="cards")
        screen.add_widget(self.card)
        self.screen_manager.add_widget(screen)

        self.p_bills = PurBills()
        screen = Screen(name="purchase bills")
        screen.add_widget(self.p_bills)
        self.screen_manager.add_widget(screen)

        self.company = Company()
        screen = Screen(name="company")
        screen.add_widget(self.company)
        self.screen_manager.add_widget(screen)

        self.user = User()
        screen = Screen(name="user")
        screen.add_widget(self.user)
        self.screen_manager.add_widget(screen)

        self.purchase = Purchase()
        screen = Screen(name="purchase")
        screen.add_widget(self.purchase)
        self.screen_manager.add_widget(screen)

        self.sales = Sales()
        screen = Screen(name="sales")
        screen.add_widget(self.sales)
        self.screen_manager.add_widget(screen)

        self.day = DayEnd()
        screen = Screen(name="day")
        screen.add_widget(self.day)
        self.screen_manager.add_widget(screen)

        self.about = About()
        screen = Screen(name="about")
        screen.add_widget(self.about)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    on_going = AwesomeApp()
    on_going.run()
