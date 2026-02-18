from tkinter import Tk, ttk
import tkinter as tk
from math import cos, sin
from db_init import VendMachine, Employer, Modem, Operator, Role
from hasher import verify
from datetime import datetime


class Main(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.pack()

        self.up_frame = tk.Frame(master)
        self.main_frame = tk.Frame(master)
        self.left_bar_frame = tk.Frame(master, background="grey")
        self.current_page = tk.Frame(master, background="grey")

        self.logo_canv = tk.Canvas(self.up_frame)
        self.logo_canv.create_text(50, 50, text="LOGO", font=("Arial", 15))

        self.username_label = tk.Label(self.up_frame, text="0")
        self.role_label = tk.Label(self.up_frame, text="0")
        self.person_settings = ttk.Combobox(self.up_frame, values=["Мои сессии", "Мой профиль", "Выход", "Вход"])

        self.main_button = tk.Button(self.left_bar_frame, text="Главная", command=self.main_window)
        self.ta_monitor_but = tk.Button(self.left_bar_frame, text="Монитор ТА", command=self.ta_monitor)
        self.report_list = ttk.Combobox(self.left_bar_frame, values=["Детальные отчёты"])
        self.record_tmc = ttk.Combobox(self.left_bar_frame, values=["Учёт ТМЦ"])
        self.administr_list = ttk.Combobox(self.left_bar_frame, values=["Дополнительное",
                                                                        "Торговые автоматы",
                                                                        "Пользователи",
                                                                        "Компании",
                                                                        "Модемы"])

        self.page_name = tk.Label(self.current_page, text="ООО Торговые Автоматы", font=("Arial", 15))
        self.current_dir = tk.Label(self.current_page, text="Главная", font=("Arial", 15))

        self.up_frame.place(x=0, y=0, width=1500, height=100)
        self.main_frame.place(x=300, y=150, width=1200, height=600)
        self.left_bar_frame.place(x=0, y=100, width=300, height=600)
        self.logo_canv.place(x=0, y=0, width=100, height=100)
        self.username_label.place(x=1350, y=10)
        self.role_label.place(x=1350, y=30)
        self.person_settings.place(x=1350, y=80)
        self.main_button.place(x=10, y=0)
        self.ta_monitor_but.place(x=10, y=50)
        self.report_list.place(x=10, y=100)
        self.record_tmc.place(x=10, y=150)
        self.administr_list.place(x=10, y=200)
        self.current_page.place(x=300, y=100, width=1200, height=50)
        self.page_name.place(x=0, y=10)
        self.current_dir.place(x=1000, y=10)

        self.authentification()
        self.person_settings.bind("<<ComboboxSelected>>", self.choice)

    def clear_main(self):
        for item in self.main_frame.winfo_children():
            item.destroy()

    def choice(self, event=None):
        match self.administr_list.get():
            case "Торговые автоматы":
                self.vend_machine()

        match self.person_settings.get():
            case "Вход":
                self.authentification()
                self.person_settings.set("")

                self.username_label.config(text=0)
                self.role_label.config(text=0)

            case "Выход":
                self.authentification()
                self.person_settings.set("")
                self.administr_list.unbind("<<ComboboxSelected>>")

                self.username_label.config(text=0)
                self.role_label.config(text=0)

            case "Мой профиль":
                self.profile()
                self.person_settings.set("")

    def main_window(self):
        self.clear_main()

        net_efficient = 30
        net_status = 300
        brief_data = [1000, 122, 124, 3563, 374563, 8756, "2/8"]
        sell_data = [100, 200, 50, 100, 20, 170, 200]
        news = ["kdslfb", "slkdnjghlnjkd", "skdhjfgb", "dskjgf", "slgfdihuldsif", "dsjfghbdsjhbkfdsjb"]
        xStep = 30

        self.name = tk.Canvas(self.main_frame)
        self.name.create_text(150, 20, text="Личный кабинет. Главная", font=("Arial", 15))

        self.net_efficient = tk.Canvas(self.main_frame, background="white")
        self.net_efficient.create_text(70, 20, text="Эффективность сети", font=("Arial", 10))
        self.net_efficient.create_arc(50, 50, 250, 250, start=0, extent=180, fill="green")
        self.net_efficient.create_line(150, 150, 150 + 100 * cos(net_efficient), 150 + 100 * sin(net_efficient))

        self.net_status = tk.Canvas(self.main_frame, background="white")
        self.net_status.create_text(70, 20, text="Состояние сети", font=("Arial", 10))
        self.net_status.create_arc(70, 40, 220, 190, start=0, extent=net_status, fill="blue")
        self.net_status.create_oval(80, 50, 210, 180, fill="white", outline="")

        self.brief = tk.Canvas(self.main_frame, background="white")
        self.brief.create_text(70, 20, text="Сводка", font=("Arial", 10))
        self.ta_money = tk.Label(self.main_frame, text=f"Денег в ТА {brief_data[0]}")
        self.ta_return = tk.Label(self.main_frame, text=f"Сдача в ТА {brief_data[1]}")
        self.money_tod = tk.Label(self.main_frame, text=f"Выручка сегодня {brief_data[2]}")
        self.money_yes = tk.Label(self.main_frame, text=f"Выручка вчера {brief_data[3]}")
        self.incas_tod = tk.Label(self.main_frame, text=f"Инкассировано сегодня {brief_data[4]}")
        self.incas_yes = tk.Label(self.main_frame, text=f"Инкассированно вчера {brief_data[5]}")
        self.servesed = tk.Label(self.main_frame, text=f"Обслужено сег.\вчера {brief_data[6]}")

        self.sell_dinamic = tk.Canvas(self.main_frame, background="white")
        self.sell_dinamic.create_text(130, 20, text="Динамика продаж за последние 10 дней", font=("Arial", 10))
        for index, item in enumerate(sell_data):
            self.sell_dinamic.create_rectangle((index + 1) * xStep, item, ((index + 1) * xStep) + 20, 200)

        self.news = tk.Canvas(self.main_frame, background="white")
        self.news.create_text(130, 20, text="Новости", font=("Arial", 10))
        for index, item in enumerate(news):
            self.lab = tk.Label(self.main_frame, text=item)
            self.lab.place(x=720, y=270 + ((index + 1) * xStep))

        self.username_label.config(text=self.user.first_name)
        self.role_label.config(text=self.user.role)

        self.name.place(x=0, y=0)
        self.net_efficient.place(x=50, y=50, width=300, height=200)
        self.net_status.place(x=400, y=50, width=300, height=200)
        self.brief.place(x=750, y=50, width=300, height=200)
        self.ta_money.place(x=770, y=80)
        self.ta_return.place(x=770, y=100)
        self.money_tod.place(x=770, y=120)
        self.money_yes.place(x=770, y=140)
        self.incas_tod.place(x=770, y=160)
        self.incas_yes.place(x=770, y=180)
        self.servesed.place(x=770, y=200)
        self.sell_dinamic.place(x=50, y=250, width=600, height=250)
        self.news.place(x=700, y=250, width=300, height=250)

    def profile(self):
        self.clear_main()

        self.user_label = tk.Label(self.main_frame, text="\n".join([self.user.email, self.user.phone, self.user.first_name, self.user.last_name, Role.get_by_id(self.user.role).name]))

        self.user_label.place(x=10, y=10)

    def vend_machine(self):
        self.clear_main()

        columns = ["ID", "Название автомата", "Модель", "Компания", "Модем", "Адрес\место", "В работе с", "Действия"]

        self.table = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        self.table.heading("ID", text="ID")
        self.table.column("ID", width=50)
        self.table.heading("Название автомата", text="Название автомата")
        self.table.heading("Модель", text="Модель")
        self.table.column("Модель", width=100)
        self.table.heading("Компания", text="Компания")
        self.table.column("Компания", width=100)
        self.table.heading("Модем", text="Модем")
        self.table.column("Модем", width=100)
        self.table.heading(r"Адрес\место", text=r"Адрес\место")
        self.table.heading("В работе с", text="В работе с")
        self.table.column("В работе с", width=100)
        self.table.heading("Действия", text="Действия")
        self.table.column("Действия", width=100)

        self.add_button = tk.Button(self.main_frame, text="Добавить", command=self.create_machine)
        self.export_button = tk.Button(self.main_frame, text="Экспорт")
        self.sort_line = tk.Entry(self.main_frame)
        self.title = tk.Label(self.main_frame, text="Торговый автомат", font=("Arial", 15))

        self.table.place(x=50, y=100, width=1100, height=600)
        self.add_button.place(x=900, y=25)
        self.export_button.place(x=1000, y=25)
        self.sort_line.place(x=550, y=25, width=200, height=25)
        self.title.place(x=50, y=25)

        self.add_vend_machine()

    def add_vend_machine(self):
        lst = VendMachine.select()
        for i in lst:
            self.table.insert("", tk.END, values=[i.id, i.name, i.model, i.firm, i.modem, i.adress, i.date_expluatation])

    def create_machine(self):
        self.clear_main()

        self.create_list = [
            tk.Label(self.main_frame, text="Название ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Производитель ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модель ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Режим работы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Производитель ТА (Slave)"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модель ТА (Slave)"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Адрес"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Место"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Координаты"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Номер автомата"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Время работы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Часовой пояс"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Товарная матрица"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Шаблон крит. значений"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Шаблон уведомлений"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Клиент"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Менеджер"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Инженер"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Техник-оператор"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Платёжные системы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты обслужывания"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты инкасации"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты загрузки"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="id кассы Kit Online"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Приоритет обслуживания"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модем"),
            tk.Entry(self.main_frame),
        ]

        for index, item in enumerate(self.create_list):
            x_step = (index // 2) % 3
            y_step = (index // 2) // 3
            offset_x = (index % 2) * 160
            item.place(x=x_step * (120 + 160) + offset_x, y=50 * y_step)

        self.create_button = tk.Button(self.main_frame, text="Создать", command=self.create_vend_machine)
        self.dell = tk.Button(self.main_frame, text="Отменить", command=self.vend_machine)

        self.create_button.place(x=900, y=500, width=80, height=20)
        self.dell.place(x=1000, y=500, width=80, height=20)

    def create_vend_machine(self):
        data = []

        for i in self.create_list:
            try:
                data.append(i.get())

            except AttributeError:
                pass

        VendMachine.get_or_create(
            name=data[0],
            firm=data[1],
            model=data[2],
            status=data[3],
            adress=data[6],
            place=data[7],
            coordinates=data[8],
            ser_num=data[9],
            work_time=data[10],
            time_zone=data[11],
            product_matrix=data[12],
            krit_sample=data[13],
            push_sample=data[14],
            client=data[15],
            manager=data[16],
            enginer=data[17],
            operator=data[18],
            pay_system=data[19],
            service_card=data[20],
            incas_card=data[21],
            download_card=data[22],
            kit_id=data[23],
            service_prior=data[24],
            modem=data[25]
        )

    def ta_monitor(self):
        self.clear_main()

        fields = list(range(2, 10))
        style = ttk.Style(self.main_frame)
        style.configure("1.Treeview", rowheight=50)
        self.ta_table = ttk.Treeview(self.main_frame, columns=fields, show="headings", style="1.Treeview")
        self.ta_table.heading(2, text="ТА")
        self.ta_table.heading(3, text="Связь")
        self.ta_table.column(3, width=100, )
        self.ta_table.heading(4, text="Загрузка")
        self.ta_table.column(4, width=100)
        self.ta_table.heading(5, text="Денежные средства")
        self.ta_table.heading(6, text="События")
        self.ta_table.column(6, width=100)
        self.ta_table.heading(7, text="Оборудование")
        self.ta_table.heading(8, text="Информация")
        self.ta_table.column(8, width=150)
        self.ta_table.heading(9, text="Доп.")
        self.ta_table.column(9, width=50)

        self.info_label = tk.Label(self.main_frame, text=f"Итого в автоматах: {10}, денег в автоматах: {10}")

        self.condi_label = tk.Label(self.main_frame, text="Общее состояние")
        self.connect_label = tk.Label(self.main_frame, text="Подключение")
        self.statuses_label = tk.Label(self.main_frame, text="Доп статусы")
        self.clear_button = tk.Button(self.main_frame, text="Очистить")
        accept_button = tk.Button(self.main_frame, text="Применить")
        self.sort_menu = ttk.Combobox(self.main_frame, values=["По состоянию ТА"])
        lst = [
            tk.Button(self.main_frame, text="🟢", fg="green"),
            tk.Button(self.main_frame, text="🔴", fg="red"),
            tk.Button(self.main_frame, text="🔵", fg="blue"),

            tk.Button(self.main_frame, text="!¡!"),
            tk.Button(self.main_frame, text="MDB"),
            tk.Button(self.main_frame, text="EXE-PG"),
            tk.Button(self.main_frame, text="EXE-ST"),

            tk.Button(self.main_frame, text="🌍"),
            tk.Button(self.main_frame, text="⚙"),
            tk.Button(self.main_frame, text="☕"),
            tk.Button(self.main_frame, text="💲🔁"),
            tk.Button(self.main_frame, text="🚐"),
            tk.Button(self.main_frame, text="🛒🔁"),
            tk.Button(self.main_frame, text="💲↓"),
            tk.Button(self.main_frame, text="🛒↓")]

        self.ta_table.place(x=20, y=150, width=1150, height=350)
        self.info_label.place(x=20, y=510)
        self.condi_label.place(x=40, y=10)
        self.connect_label.place(x=160, y=10)
        self.statuses_label.place(x=330, y=10)
        self.clear_button.place(x=140, y=80)
        accept_button.place(x=40, y=80)
        self.sort_menu.place(x=650, y=50)

        for index, item in enumerate(lst):
            item.place(x=40 * (index + 1), y=40, width=30, height=30)

        self.ta_insert()

    def ta_insert(self):
        lst = VendMachine.select()
        for i in lst:
            modem = Modem.get_by_id(i.modem)
            operator = Operator.get_by_id(modem.operator)
            self.ta_table.insert("", tk.END, values=["\n".join([i.adress, i.place, i.invent_num]), "\n".join([operator.name, str(datetime.utcnow())]), modem.load, i.money])

    def authentification(self, _=None):
        self.clear_main()

        self.email = tk.Entry(self.main_frame)
        self.password = tk.Entry(self.main_frame)
        accept_button = tk.Button(self.main_frame, text="Войти", command=self.render_main)

        self.email.place(x=50, y=50)
        self.password.place(x=50, y=90)
        accept_button.place(x=200, y=90)

    def render_main(self):
        self.user = Employer.get_or_none(email=self.email.get())

        if verify(self.password.get(), self.user.password):
            self.main_window()
            self.administr_list.bind("<<ComboboxSelected>>", self.choice)


if __name__ == "__main__":
    master = Tk()
    main_window = Main(master)
    master.geometry("1500x700")
    master.mainloop()
