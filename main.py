"""
=============================================================================
THE ECONOMICON
Edexcel IGCSE Revision Suite (4BS1 & 4EC1)
Credit: Engineered by Zoar Hasan
Platform: Kivy / Pydroid 3 / Android
=============================================================================
"""

import json
import os
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Window.clearcolor = (0.031, 0.035, 0.047, 1)

KV_CODE = """
#:import hex kivy.utils.get_color_from_hex

<CyberButton@Button>:
    background_normal: ''
    background_color: (0, 0, 0, 0)
    markup: True
    font_size: '12sp'
    canvas.before:
        Color:
            rgba: hex('#13161F')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [6, 6, 6, 6]
        Color:
            rgba: hex('#2C3242')
        Line:
            width: 1.1
            rounded_rectangle: (self.x, self.y, self.width, self.height, 6)

<FolderCard@Button>:
    background_normal: ''
    background_color: (0, 0, 0, 0)
    size_hint_y: None
    height: dp(100)
    markup: True
    halign: 'left'
    valign: 'middle'
    padding: [dp(16), dp(10)]
    text_size: (self.width - dp(32), None)

<BusinessCard@FolderCard>:
    canvas.before:
        Color:
            rgba: hex('#0D1117')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10, 10, 10, 10]
        Color:
            rgba: hex('#3D72B4')
        Line:
            width: 1.2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

<EconCard@FolderCard>:
    canvas.before:
        Color:
            rgba: hex('#120D1A')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10, 10, 10, 10]
        Color:
            rgba: hex('#7B4CA8')
        Line:
            width: 1.2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

<MixedCard@FolderCard>:
    canvas.before:
        Color:
            rgba: hex('#17140B')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10, 10, 10, 10]
        Color:
            rgba: hex('#A37F15')
        Line:
            width: 1.2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

<BusinessNodeItem>:
    size_hint_y: None
    height: dp(78)
    background_normal: ''
    background_color: (0, 0, 0, 0)
    canvas.before:
        Color:
            rgba: hex('#0F131D')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8, 8, 8, 8]
        Color:
            rgba: hex('#2D5482')
        Line:
            width: 1.1
            rounded_rectangle: (self.x, self.y, self.width, self.height, 8)

<EconNodeItem>:
    size_hint_y: None
    height: dp(78)
    background_normal: ''
    background_color: (0, 0, 0, 0)
    canvas.before:
        Color:
            rgba: hex('#150F21')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8, 8, 8, 8]
        Color:
            rgba: hex('#5F388A')
        Line:
            width: 1.1
            rounded_rectangle: (self.x, self.y, self.width, self.height, 8)

<MixedNodeItem>:
    size_hint_y: None
    height: dp(78)
    background_normal: ''
    background_color: (0, 0, 0, 0)
    canvas.before:
        Color:
            rgba: hex('#1A160A')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8, 8, 8, 8]
        Color:
            rgba: hex('#735A12')
        Line:
            width: 1.1
            rounded_rectangle: (self.x, self.y, self.width, self.height, 8)

<RootFolderScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [dp(16), dp(12), dp(16), dp(12)]
        spacing: dp(12)

        BoxLayout:
            size_hint_y: None
            height: dp(34)
            spacing: dp(8)
            Label:
                text: "Edexcel IGCSE Revision System"
                font_size: '11sp'
                color: hex('#7CACF8')
                text_size: self.size
                halign: 'left'
                valign: 'middle'
            CyberButton:
                text: "Edit Code"
                size_hint_x: None
                width: dp(94)
                color: hex('#FDD663')
                on_release: root.open_ota_settings()

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(54)
            spacing: dp(2)
            Label:
                text: "[b]The Economicon[/b]"
                markup: True
                font_size: '22sp'
                color: hex('#FFFFFF')
                text_size: self.size
                halign: 'left'
            Label:
                text: "Full syllabus coverage, quantitative solvers and glossary"
                font_size: '11sp'
                color: hex('#9AA0A6')
                text_size: self.size
                halign: 'left'

        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(14)
                size_hint_y: None
                height: self.minimum_height

                BusinessCard:
                    text: "[color=#7CACF8][b]Business Studies (4BS1)[/b][/color]\\n[size=11sp][color=#B0B7C3]5 Core Units • 46 Complete Chapters[/color][/size]"
                    on_release: app.root.current = 'business'

                EconCard:
                    text: "[color=#C58AF9][b]Economics (4EC1)[/b][/color]\\n[size=11sp][color=#B0B7C3]Unit 1: Microeconomics • Unit 2: Macroeconomics[/color][/size]"
                    on_release: app.root.current = 'economics'

                MixedCard:
                    text: "[color=#FDD663][b]Formulas & Glossary[/b][/color]\\n[size=11sp][color=#B0B7C3]Quantitative Solvers & Complete Syllabus Terminology[/color][/size]"
                    on_release: app.root.current = 'mixed'

        BoxLayout:
            size_hint_y: None
            height: dp(22)
            Label:
                text: "Engineered by Zoar Hasan"
                font_size: '10sp'
                color: hex('#5F6368')
                text_size: self.size
                halign: 'left'
                valign: 'middle'
            Label:
                text: "System Ready"
                font_size: '10sp'
                color: hex('#81C995')
                text_size: self.size
                halign: 'right'
                valign: 'middle'

<BusinessFolderScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [dp(14), dp(10), dp(14), dp(10)]
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            CyberButton:
                text: "Back"
                size_hint_x: None
                width: dp(70)
                color: hex('#7CACF8')
                on_release: app.root.current = 'root'
            Label:
                text: "Business Studies (4BS1)"
                bold: True
                color: hex('#FFFFFF')
                text_size: self.size
                halign: 'left'
                valign: 'middle'

        TextInput:
            id: search_business
            size_hint_y: None
            height: dp(40)
            hint_text: "Search business chapters, terms, concepts..."
            background_normal: ''
            background_color: hex('#11131A')
            foreground_color: hex('#FFFFFF')
            hint_text_color: hex('#5F6368')
            multiline: False
            padding: [dp(12), dp(10)]
            on_text: root.filter_chapters(self.text)

        BoxLayout:
            size_hint_y: None
            height: dp(34)
            spacing: dp(4)
            CyberButton:
                text: "All Units"
                on_release: root.select_unit('all')
            CyberButton:
                text: "Unit 1"
                on_release: root.select_unit(1)
            CyberButton:
                text: "Unit 2"
                on_release: root.select_unit(2)
            CyberButton:
                text: "Unit 3"
                on_release: root.select_unit(3)
            CyberButton:
                text: "Unit 4"
                on_release: root.select_unit(4)
            CyberButton:
                text: "Unit 5"
                on_release: root.select_unit(5)

        ScrollView:
            BoxLayout:
                id: business_container
                orientation: 'vertical'
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height

<EconomicsFolderScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [dp(14), dp(10), dp(14), dp(10)]
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            CyberButton:
                text: "Back"
                size_hint_x: None
                width: dp(70)
                color: hex('#C58AF9')
                on_release: app.root.current = 'root'
            Label:
                text: "Economics (4EC1)"
                bold: True
                color: hex('#FFFFFF')
                text_size: self.size
                halign: 'left'
                valign: 'middle'

        TextInput:
            id: search_econ
            size_hint_y: None
            height: dp(40)
            hint_text: "Search economics chapters, graphs, policies..."
            background_normal: ''
            background_color: hex('#11131A')
            foreground_color: hex('#FFFFFF')
            hint_text_color: hex('#5F6368')
            multiline: False
            padding: [dp(12), dp(10)]
            on_text: root.filter_chapters(self.text)

        BoxLayout:
            size_hint_y: None
            height: dp(34)
            spacing: dp(4)
            CyberButton:
                text: "All Chapters"
                on_release: root.select_unit('all')
            CyberButton:
                text: "Microeconomics"
                on_release: root.select_unit(1)
            CyberButton:
                text: "Macroeconomics"
                on_release: root.select_unit(2)

        ScrollView:
            BoxLayout:
                id: econ_container
                orientation: 'vertical'
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height

<MixedFolderScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [dp(14), dp(10), dp(14), dp(10)]
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            CyberButton:
                text: "Back"
                size_hint_x: None
                width: dp(70)
                color: hex('#FDD663')
                on_release: app.root.current = 'root'
            Label:
                text: "Tools & Glossary"
                bold: True
                color: hex('#FFFFFF')
                text_size: self.size
                halign: 'left'
                valign: 'middle'
            CyberButton:
                text: "New Item"
                size_hint_x: None
                width: dp(82)
                color: hex('#7CACF8')
                on_release: root.open_add_modal()

        BoxLayout:
            size_hint_y: None
            height: dp(34)
            spacing: dp(6)
            CyberButton:
                text: "Formulas & Solvers"
                on_release: root.switch_subtab('formulas')
            CyberButton:
                text: "Syllabus Glossary"
                on_release: root.switch_subtab('glossary')

        TextInput:
            id: search_mixed
            size_hint_y: None
            height: dp(40)
            hint_text: "Tap formula to calculate • Hold item to edit..."
            background_normal: ''
            background_color: hex('#11131A')
            foreground_color: hex('#FFFFFF')
            hint_text_color: hex('#5F6368')
            multiline: False
            padding: [dp(12), dp(10)]
            on_text: root.filter_items(self.text)

        ScrollView:
            BoxLayout:
                id: mixed_container
                orientation: 'vertical'
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height

<ChapterDetailScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: [dp(14), dp(10), dp(14), dp(10)]
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            CyberButton:
                text: "Back"
                size_hint_x: None
                width: dp(70)
                color: hex('#7CACF8')
                on_release: root.go_back()
            Label:
                id: detail_header
                text: "Chapter Review"
                bold: True
                color: hex('#FFFFFF')
                text_size: self.size
                halign: 'left'
                valign: 'middle'
            CyberButton:
                text: "Edit"
                size_hint_x: None
                width: dp(64)
                color: hex('#FDD663')
                on_release: root.open_advanced_editor()

        Label:
            id: detail_title
            text: "Chapter Name"
            font_size: '15sp'
            bold: True
            color: hex('#7CACF8')
            size_hint_y: None
            height: dp(36)
            text_size: self.size
            halign: 'left'
            valign: 'middle'

        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: [dp(4), dp(6)]
                Label:
                    id: detail_content
                    text: "Content..."
                    font_size: '13.5sp'
                    color: hex('#D6D8DF')
                    size_hint_y: None
                    height: self.texture_size[1] + dp(24)
                    text_size: self.width - dp(10), None
                    markup: True
"""

# =============================================================================
# WIDGET CLASSES
# =============================================================================
class CyberNodeItem(Button):
    def __init__(self, on_short_press=None, on_long_press=None, **kwargs):
        super().__init__(**kwargs)
        self.on_short_press_cb = on_short_press
        self.on_long_press_cb = on_long_press
        self.long_press_event = None
        self.did_long_press = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.did_long_press = False
            self.long_press_event = Clock.schedule_once(self._trigger_long_press, 0.6)
            return super().on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        if self.long_press_event and not self.collide_point(*touch.pos):
            Clock.unschedule(self.long_press_event)
            self.long_press_event = None
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.long_press_event:
            Clock.unschedule(self.long_press_event)
            self.long_press_event = None
        if self.collide_point(*touch.pos):
            if not self.did_long_press and self.on_short_press_cb:
                self.on_short_press_cb()
            return True
        return super().on_touch_up(touch)

    def _trigger_long_press(self, dt):
        self.did_long_press = True
        if self.on_long_press_cb:
            self.on_long_press_cb()

class BusinessNodeItem(CyberNodeItem):
    pass

class EconNodeItem(CyberNodeItem):
    pass

class MixedNodeItem(CyberNodeItem):
    pass

class RootFolderScreen(Screen):
    def open_ota_settings(self):
        app = App.get_running_app()
        box = BoxLayout(orientation='vertical', spacing=dp(8), padding=dp(10))

        box.add_widget(Label(
            text="[b]Source Code Update[/b]",
            markup=True, font_size='14sp', color=(0.48, 0.67, 0.97, 1),
            size_hint_y: None, height=dp(22)
        ))
        box.add_widget(Label(
            text="Paste updated Python code below. All notes, chapter titles,\\ncustom formulas and glossary items will be preserved.",
            font_size='10.5sp', color=(0.7, 0.7, 0.7, 1),
            size_hint_y: None, height=dp(30)
        ))

        txt_code = TextInput(
            hint_text="# Paste new code here...",
            multiline=True,
            background_normal='',
            background_color=(0.06, 0.07, 0.09, 1),
            foreground_color=(1, 1, 1, 1),
            font_size='11sp',
            font_name='Roboto'
        )
        box.add_widget(txt_code)

        status_lbl = Label(text="Ready", font_size='11sp', color=(0.5, 0.78, 0.58, 1), size_hint_y=None, height=dp(20))
        box.add_widget(status_lbl)

        btn_row = BoxLayout(size_hint_y=None, height=dp(42), spacing=dp(8))
        apply_btn = Button(text="Update & Restart", background_normal='', background_color=(0.15, 0.35, 0.65, 1), bold=True)
        backup_btn = Button(text="Save Backup", background_normal='', background_color=(0.18, 0.22, 0.28, 1))

        btn_row.add_widget(apply_btn)
        btn_row.add_widget(backup_btn)
        box.add_widget(btn_row)

        popup = Popup(title="Settings & Updates", content=box, size_hint=(0.95, 0.88))

        def force_backup(inst):
            app.save_persistent_data()
            status_lbl.text = "Backup successfully written to storage"

        def flash_code(inst):
            new_script = txt_code.text.strip()
            if len(new_script) < 50:
                status_lbl.text = "Error: Input code buffer is empty"
                return

            try:
                app.save_persistent_data()

                target_file = os.path.abspath(sys.argv[0])
                if not os.path.exists(target_file):
                    target_file = os.path.abspath(__file__)

                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(new_script)

                status_lbl.text = "Success. Restarting app..."
                popup.dismiss()
                App.get_running_app().stop()
            except Exception as e:
                status_lbl.text = f"Error: {str(e)[:40]}"

        backup_btn.bind(on_release=force_backup)
        apply_btn.bind(on_release=flash_code)
        popup.open()

class BusinessFolderScreen(Screen):
    current_unit = 'all'

    def on_enter(self):
        self.populate_chapters(self.current_unit, self.ids.search_business.text)

    def select_unit(self, unit):
        self.current_unit = unit
        self.populate_chapters(unit, self.ids.search_business.text)

    def filter_chapters(self, query):
        self.populate_chapters(self.current_unit, query)

    def populate_chapters(self, unit_filter, query):
        container = self.ids.business_container
        container.clear_widgets()
        chapters = App.get_running_app().business_chapters
        q = query.strip().lower()

        for ch in chapters:
            if unit_filter != 'all' and ch['unit'] != unit_filter:
                continue
            if q and (q not in ch['title'].lower() and q not in ch['summary'].lower() and q not in ch['notes'].lower()):
                continue

            t_str = f"[b]Chapter {ch['number']}: {ch['title']}[/b] [color=#7CACF8](Unit {ch['unit']})[/color]"
            s_str = ch['summary']
            btn = create_cyber_node(
                'business', t_str, s_str,
                on_short=lambda c=ch: self.open_chapter(c)
            )
            container.add_widget(btn)

    def open_chapter(self, ch):
        app = App.get_running_app()
        detail_screen = app.root.get_screen('chapter_detail')
        detail_screen.display_chapter(ch, 'business')
        app.root.current = 'chapter_detail'

class EconomicsFolderScreen(Screen):
    current_unit = 'all'

    def on_enter(self):
        self.populate_chapters(self.current_unit, self.ids.search_econ.text)

    def select_unit(self, unit):
        self.current_unit = unit
        self.populate_chapters(unit, self.ids.search_econ.text)

    def filter_chapters(self, query):
        self.populate_chapters(self.current_unit, query)

    def populate_chapters(self, unit_filter, query):
        container = self.ids.econ_container
        container.clear_widgets()
        chapters = App.get_running_app().econ_chapters
        q = query.strip().lower()

        for ch in chapters:
            if unit_filter != 'all' and ch['unit'] != unit_filter:
                continue
            if q and (q not in ch['title'].lower() and q not in ch['summary'].lower() and q not in ch['notes'].lower()):
                continue

            u_name = "Micro" if ch['unit'] == 1 else "Macro"
            t_str = f"[b]Chapter {ch['number']}: {ch['title']}[/b] [color=#C58AF9]({u_name})[/color]"
            s_str = ch['summary']
            btn = create_cyber_node(
                'econ', t_str, s_str,
                on_short=lambda c=ch: self.open_chapter(c)
            )
            container.add_widget(btn)

    def open_chapter(self, ch):
        app = App.get_running_app()
        detail_screen = app.root.get_screen('chapter_detail')
        detail_screen.display_chapter(ch, 'economics')
        app.root.current = 'chapter_detail'

class MixedFolderScreen(Screen):
    current_subtab = 'formulas'

    def on_enter(self):
        self.populate_content(self.ids.search_mixed.text)

    def switch_subtab(self, subtab):
        self.current_subtab = subtab
        self.populate_content(self.ids.search_mixed.text)

    def filter_items(self, query):
        self.populate_content(query)

    def populate_content(self, query):
        container = self.ids.mixed_container
        container.clear_widgets()
        app = App.get_running_app()
        q = query.strip().lower()

        if self.current_subtab == 'formulas':
            for f in app.formulas:
                if q and (q not in f['name'].lower() and q not in f['formula'].lower() and q not in f['category'].lower()):
                    continue
                t_str = f"[b]{f['name']}[/b] [color=#7CACF8]({f['category']})[/color]"
                s_str = f"[color=#FDD663]Formula: {f['formula']}[/color]"
                btn = create_cyber_node(
                    'mixed', t_str, s_str,
                    on_short=lambda item=f: self.open_formula_solver(item),
                    on_long=lambda item=f: self.open_edit_modal(item, is_formula=True)
                )
                container.add_widget(btn)
        else:
            for g in app.glossary:
                if q and (q not in g['term'].lower() and g not in g['definition'].lower()):
                    continue
                t_str = f"[b]{g['term']}[/b] [color=#81C995]({g.get('subject', 'General').capitalize()})[/color]"
                s_str = g['definition']
                btn = create_cyber_node(
                    'mixed', t_str, s_str,
                    on_short=lambda item=g: self.open_glossary_viewer(item),
                    on_long=lambda item=g: self.open_edit_modal(item, is_formula=False)
                )
                container.add_widget(btn)

    def open_formula_solver(self, item):
        solver_defs = {
            "Total Revenue (TR)": [("Selling Price", "P"), ("Quantity Sold", "Q"), lambda v: f"TR = {v[0]*v[1]:,.2f}"],
            "Total Cost (TC)": [("Total Fixed Costs (TFC)", "TFC"), ("Total Variable Costs (TVC)", "TVC"), lambda v: f"TC = {v[0]+v[1]:,.2f}"],
            "Average Cost (AC)": [("Total Cost", "TC"), ("Total Output", "Q"), lambda v: f"AC = {v[0]/v[1]:,.2f}" if v[1] else "Div by Zero"],
            "Total Profit / Loss": [("Total Revenue", "TR"), ("Total Cost", "TC"), lambda v: f"Profit = {v[0]-v[1]:,.2f}"],
            "Contribution per Unit": [("Selling Price", "P"), ("Variable Cost/Unit", "VC"), lambda v: f"Contribution = {v[0]-v[1]:,.2f}"],
            "Break-even Output (BEP)": [("Fixed Costs", "FC"), ("Price/Unit", "P"), ("Var Cost/Unit", "VC"), lambda v: f"BEP = {v[0]/(v[1]-v[2]):,.2f} units" if (v[1]-v[2]) else "Invalid Contribution"],
            "Margin of Safety": [("Actual/Budgeted Output", "Actual"), ("Break-even Output", "BEP"), lambda v: f"Margin of Safety = {v[0]-v[1]:,.2f} units"],
            "Net Cash Flow": [("Total Cash Inflows", "Inflows"), ("Total Cash Outflows", "Outflows"), lambda v: f"Net Cash Flow = {v[0]-v[1]:,.2f}"],
            "Closing Cash Balance": [("Opening Balance", "Opening"), ("Net Cash Flow", "NCF"), lambda v: f"Closing Balance = {v[0]+v[1]:,.2f}"],
            "Gross Profit Margin (GPM)": [("Gross Profit", "GP"), ("Sales Revenue", "Rev"), lambda v: f"GPM = {(v[0]/v[1])*100:,.2f}%" if v[1] else "Div by Zero"],
            "Net Profit Margin (NPM)": [("Profit for the Year", "NetProfit"), ("Sales Revenue", "Rev"), lambda v: f"NPM = {(v[0]/v[1])*100:,.2f}%" if v[1] else "Div by Zero"],
            "Return on Capital Employed (ROCE)": [("Operating Profit", "OP"), ("Capital Employed", "CE"), lambda v: f"ROCE = {(v[0]/v[1])*100:,.2f}%" if v[1] else "Div by Zero"],
            "Working Capital": [("Current Assets", "CA"), ("Current Liabilities", "CL"), lambda v: f"Working Capital = {v[0]-v[1]:,.2f}"],
            "Current Ratio": [("Current Assets", "CA"), ("Current Liabilities", "CL"), lambda v: f"Current Ratio = {v[0]/v[1]:,.2f} : 1" if v[1] else "Div by Zero"],
            "Acid Test Ratio": [("Current Assets", "CA"), ("Inventory", "Stock"), ("Current Liabilities", "CL"), lambda v: f"Acid Test = {(v[0]-v[1])/v[2]:,.2f} : 1" if v[2] else "Div by Zero"],
            "Added Value": [("Selling Price", "Price"), ("Bought-in Costs", "Costs"), lambda v: f"Added Value = {v[0]-v[1]:,.2f}"],
            "Labour Productivity": [("Total Output", "Output"), ("Total Workers", "Workers"), lambda v: f"Productivity = {v[0]/v[1]:,.2f} units/worker" if v[1] else "Div by Zero"],
            "Market Share": [("Business Sales", "FirmSales"), ("Total Market Sales", "MarketSales"), lambda v: f"Market Share = {(v[0]/v[1])*100:,.2f}%" if v[1] else "Div by Zero"],
            "Percentage Change": [("Original Value", "V1"), ("New Value", "V2"), lambda v: f"Change = {((v[1]-v[0])/v[0])*100:,.2f}%" if v[0] else "Div by Zero"],
            "Price Elasticity of Demand (PED)": [("% Change in QD", "%QD"), ("% Change in Price", "%P"), lambda v: f"PED = {v[0]/v[1]:,.2f} ({'Price Elastic' if abs(v[0]/v[1])>1 else 'Price Inelastic'})" if v[1] else "Div by Zero"],
            "Income Elasticity of Demand (YED)": [("% Change in QD", "%QD"), ("% Change in Income", "%Y"), lambda v: f"YED = {v[0]/v[1]:,.2f} ({'Normal Good' if (v[0]/v[1])>0 else 'Inferior Good'})" if v[1] else "Div by Zero"],
            "Price Elasticity of Supply (PES)": [("% Change in QS", "%QS"), ("% Change in Price", "%P"), lambda v: f"PES = {v[0]/v[1]:,.2f}" if v[1] else "Div by Zero"],
            "GDP per Capita": [("Real GDP", "GDP"), ("Population", "Pop"), lambda v: f"GDP per Capita = {v[0]/v[1]:,.2f}" if v[1] else "Div by Zero"],
            "Unemployment Rate": [("Unemployed Persons", "Unemployed"), ("Labour Force", "Workforce"), lambda v: f"Unemployment Rate = {(v[0]/v[1])*100:,.2f}%" if v[1] else "Div by Zero"]
        }

        cfg = solver_defs.get(item['name'])

        content = BoxLayout(orientation='vertical', padding=dp(14), spacing=dp(8))
        content.add_widget(Label(text=f"[b]{item['name']}[/b]", markup=True, font_size='16sp', color=(0.48, 0.67, 0.97, 1), size_hint_y=None, height=dp(26)))
        content.add_widget(Label(text=f"Formula: [color=#FDD663]{item['formula']}[/color]", markup=True, font_size='11.5sp', size_hint_y=None, height=dp(24)))

        if not cfg:
            content.add_widget(Label(text="Standard formula reference node.\\nHold press this item to edit.", font_size='12sp', color=(0.7, 0.7, 0.7, 1)))
            popup = Popup(title="Formula Details", content=content, size_hint=(0.92, 0.48))
            popup.open()
            return

        inputs = []
        for label_text, hint in cfg[:-1]:
            row = BoxLayout(size_hint_y=None, height=dp(38), spacing=dp(6))
            row.add_widget(Label(text=label_text, font_size='11.5sp', halign='left', text_size=(dp(160), None)))
            inp = TextInput(hint_text=hint, input_filter='float', multiline=False, background_normal='', background_color=(0.08, 0.09, 0.12, 1), foreground_color=(1, 1, 1, 1), padding=[dp(8), dp(8)])
            inputs.append(inp)
            row.add_widget(inp)
            content.add_widget(row)

        res_lbl = Label(text="Result: --", font_size='13sp', bold=True, color=(0.5, 0.78, 0.58, 1), size_hint_y=None, height=dp(28))
        content.add_widget(res_lbl)

        def calculate(inst):
            try:
                vals = [float(inp.text.strip()) for inp in inputs]
                res_lbl.text = f"Result: {cfg[-1](vals)}"
            except Exception:
                res_lbl.text = "Result: [Invalid or Missing Inputs]"

        calc_btn = Button(text="Calculate", size_hint_y=None, height=dp(40), background_normal='', background_color=(0.15, 0.35, 0.65, 1), bold=True)
        calc_btn.bind(on_release=calculate)
        content.add_widget(calc_btn)

        popup = Popup(title="Formula Calculator", content=content, size_hint=(0.94, 0.68))
        popup.open()

    def open_glossary_viewer(self, item):
        content = BoxLayout(orientation='vertical', padding=dp(14), spacing=dp(8))
        content.add_widget(Label(text=f"[b]{item['term']}[/b]", markup=True, font_size='17sp', color=(0.5, 0.78, 0.58, 1)))
        content.add_widget(Label(text=f"Subject: {item['subject'].capitalize()}", font_size='12sp', color=(0.6, 0.6, 0.6, 1)))
        lbl_def = Label(text=item['definition'], font_size='13sp', text_size=(dp(280), None), halign='center')
        content.add_widget(lbl_def)
        content.add_widget(Label(text="Hold press this item to edit definition.", font_size='10sp', color=(0.4, 0.4, 0.4, 1)))
        popup = Popup(title="Glossary Term", content=content, size_hint=(0.9, 0.55))
        popup.open()

    def open_edit_modal(self, item, is_formula):
        app = App.get_running_app()
        title = "Edit Formula" if is_formula else "Edit Glossary Term"

        layout = BoxLayout(orientation='vertical', spacing=dp(8), padding=dp(10))
        input1 = TextInput(
            text=item['name'] if is_formula else item['term'],
            multiline=False, size_hint_y=None, height=dp(40),
            background_normal='', background_color=(0.08, 0.09, 0.12, 1),
            foreground_color=(1, 1, 1, 1)
        )
        input2 = TextInput(
            text=item['category'] if is_formula else item['subject'],
            multiline=False, size_hint_y=None, height=dp(40),
            background_normal='', background_color=(0.08, 0.09, 0.12, 1),
            foreground_color=(1, 1, 1, 1)
        )
        input3 = TextInput(
            text=item['formula'] if is_formula else item['definition'],
            multiline=True,
            background_normal='', background_color=(0.08, 0.09, 0.12, 1),
            foreground_color=(1, 1, 1, 1)
        )

        btn_row = BoxLayout(size_hint_y=None, height=dp(44), spacing=dp(6))
        save_btn = Button(text="Save", background_normal='', background_color=(0.15, 0.35, 0.65, 1), bold=True)
        del_btn = Button(text="Delete", background_normal='', background_color=(0.6, 0.15, 0.15, 1), bold=True)

        btn_row.add_widget(save_btn)
        btn_row.add_widget(del_btn)

        layout.add_widget(input1)
        layout.add_widget(input2)
        layout.add_widget(input3)
        layout.add_widget(btn_row)

        popup = Popup(title=title, content=layout, size_hint=(0.92, 0.7))

        def save_action(instance):
            f1 = input1.text.strip()
            f2 = input2.text.strip()
            f3 = input3.text.strip()
            if not f1 or not f3:
                return

            if is_formula:
                item['name'] = f1
                item['category'] = f2 or "General"
                item['formula'] = f3
            else:
                item['term'] = f1
                item['subject'] = f2 or "General"
                item['definition'] = f3

            app.save_persistent_data()
            self.populate_content(self.ids.search_mixed.text)
            popup.dismiss()

        def delete_action(instance):
            if is_formula:
                if item in app.formulas:
                    app.formulas.remove(item)
            else:
                if item in app.glossary:
                    app.glossary.remove(item)
            app.save_persistent_data()
            self.populate_content(self.ids.search_mixed.text)
            popup.dismiss()

        save_btn.bind(on_release=save_action)
        del_btn.bind(on_release=delete_action)
        popup.open()

    def open_add_modal(self):
        is_formula = self.current_subtab == 'formulas'
        title = "New Formula" if is_formula else "New Glossary Term"

        layout = BoxLayout(orientation='vertical', spacing=dp(8), padding=dp(10))
        input1 = TextInput(hint_text="Title / Term", multiline=False, size_hint_y=None, height=dp(40),
                           background_normal='', background_color=(0.08, 0.09, 0.12, 1), foreground_color=(1, 1, 1, 1))
        input2 = TextInput(hint_text="Category / Subject", multiline=False, size_hint_y=None, height=dp(40),
                           background_normal='', background_color=(0.08, 0.09, 0.12, 1), foreground_color=(1, 1, 1, 1))
        input3 = TextInput(hint_text="Formula String or Exam Definition", multiline=True,
                           background_normal='', background_color=(0.08, 0.09, 0.12, 1), foreground_color=(1, 1, 1, 1))

        save_btn = Button(text="Add Item", size_hint_y=None, height=dp(44), background_normal='',
                          background_color=(0.15, 0.35, 0.65, 1), bold=True)

        layout.add_widget(input1)
        layout.add_widget(input2)
        layout.add_widget(input3)
        layout.add_widget(save_btn)

        popup = Popup(title=title, content=layout, size_hint=(0.92, 0.65))

        def save_action(instance):
            f1 = input1.text.strip()
            f2 = input2.text.strip()
            f3 = input3.text.strip()
            if not f1 or not f3:
                return

            app = App.get_running_app()
            if is_formula:
                app.formulas.insert(0, {"name": f1, "category": f2 or "Custom", "formula": f3})
            else:
                app.glossary.insert(0, {"term": f1, "subject": f2 or "Custom", "definition": f3})

            app.save_persistent_data()
            self.populate_content(self.ids.search_mixed.text)
            popup.dismiss()

        save_btn.bind(on_release=save_action)
        popup.open()

class ChapterDetailScreen(Screen):
    current_chapter = None
    origin_screen = 'business'

    def display_chapter(self, chapter, origin):
        self.current_chapter = chapter
        self.origin_screen = origin
        code = "Business (4BS1)" if origin == 'business' else "Economics (4EC1)"
        self.ids.detail_header.text = f"{code} • Unit {chapter['unit']}"
        self.ids.detail_title.text = f"Chapter {chapter['number']}: {chapter['title']}"
        self.ids.detail_content.text = chapter['notes']

    def go_back(self):
        App.get_running_app().root.current = self.origin_screen

    def open_advanced_editor(self):
        if not self.current_chapter:
            return

        box = BoxLayout(orientation='vertical', spacing=dp(8), padding=dp(10))

        box.add_widget(Label(text="Edit Chapter Title:", font_size='11sp', color=(0.48, 0.67, 0.97, 1), size_hint_y=None, height=dp(18), halign='left'))
        txt_title = TextInput(
            text=self.current_chapter['title'],
            multiline=False,
            size_hint_y=None,
            height=dp(38),
            background_normal='',
            background_color=(0.09, 0.11, 0.16, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[dp(10), dp(8)]
        )
        box.add_widget(txt_title)

        toolbar = BoxLayout(size_hint_y=None, height=dp(36), spacing=dp(4))

        txt_notes = TextInput(
            text=self.current_chapter['notes'],
            multiline=True,
            background_normal='',
            background_color=(0.06, 0.07, 0.09, 1),
            foreground_color=(1, 1, 1, 1),
            font_size='13sp',
            padding=[dp(10), dp(10)]
        )

        def apply_tag(open_tag, close_tag):
            if txt_notes.selection_text:
                sel = txt_notes.selection_text
                txt_notes.insert_text(f"{open_tag}{sel}{close_tag}")
            else:
                txt_notes.insert_text(f"{open_tag}Text{close_tag}")

        actions = [
            ("Bold", "[b]", "[/b]"),
            ("Italic", "[i]", "[/i]"),
            ("Heading", "[size=18sp][b]", "[/b][/size]"),
            ("Subhead", "[size=15sp][b]", "[/b][/size]"),
            ("Highlight", "[color=#FDD663]", "[/color]")
        ]

        for label_t, ot, ct in actions:
            btn = Button(text=label_t, markup=True, background_normal='', background_color=(0.12, 0.15, 0.22, 1), font_size='11sp')
            btn.bind(on_release=lambda x, o=ot, c=ct: apply_tag(o, c))
            toolbar.add_widget(btn)

        btn_bullet = Button(text="Bullet", background_normal='', background_color=(0.12, 0.15, 0.22, 1), font_size='11sp')
        btn_bullet.bind(on_release=lambda x: txt_notes.insert_text("\n• "))
        toolbar.add_widget(btn_bullet)

        save_btn = Button(
            text="Save Changes",
            size_hint_y=None,
            height=dp(44),
            background_normal='',
            background_color=(0.15, 0.35, 0.65, 1),
            bold=True
        )

        box.add_widget(toolbar)
        box.add_widget(txt_notes)
        box.add_widget(save_btn)

        popup = Popup(
            title=f"Edit Chapter {self.current_chapter['number']}",
            content=box,
            size_hint=(0.95, 0.92)
        )

        def save_changes(instance):
            updated_title = txt_title.text.strip()
            updated_notes = txt_notes.text.strip()
            if updated_title:
                self.current_chapter['title'] = updated_title
                self.ids.detail_title.text = f"Chapter {self.current_chapter['number']}: {updated_title}"
            if updated_notes:
                self.current_chapter['notes'] = updated_notes
                self.ids.detail_content.text = updated_notes
            App.get_running_app().save_persistent_data()

            app = App.get_running_app()
            if self.origin_screen == 'business':
                app.root.get_screen('business').populate_chapters('all', '')
            else:
                app.root.get_screen('economics').populate_chapters('all', '')

            popup.dismiss()

        save_btn.bind(on_release=save_changes)
        popup.open()

def create_cyber_node(node_type, title_text, sub_text, on_short=None, on_long=None):
    if node_type == 'business':
        btn = BusinessNodeItem(on_short_press=on_short, on_long_press=on_long)
    elif node_type == 'econ':
        btn = EconNodeItem(on_short_press=on_short, on_long_press=on_long)
    else:
        btn = MixedNodeItem(on_short_press=on_short, on_long_press=on_long)

    box = BoxLayout(orientation='vertical', padding=[dp(14), dp(8)], spacing=dp(2))
    box.size = btn.size
    box.pos = btn.pos

    lbl_title = Label(
        text=title_text,
        markup=True,
        font_size='13sp',
        size_hint_y=0.45,
        halign='left',
        valign='middle'
    )
    lbl_title.bind(size=lambda inst, val: setattr(inst, 'text_size', (val[0], val[1])))

    lbl_sub = Label(
        text=sub_text,
        markup=True,
        font_size='10.5sp',
        color=(0.60, 0.64, 0.70, 1),
        size_hint_y=0.55,
        halign='left',
        valign='top'
    )
    lbl_sub.bind(size=lambda inst, val: setattr(inst, 'text_size', (val[0], val[1])))

    box.add_widget(lbl_title)
    box.add_widget(lbl_sub)

    btn.bind(pos=lambda inst, val: setattr(box, 'pos', val))
    btn.bind(size=lambda inst, val: setattr(box, 'size', val))
    btn.add_widget(box)
    return btn

# =============================================================================
# RUNTIME APPLICATION
# =============================================================================
class EdexcelIGCSEApp(App):
    DATA_FILE = "edexcel_master_study_engine.json"

    def build(self):
        self.init_data()
        self.load_persistent_data()
        Builder.load_string(KV_CODE)

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(RootFolderScreen(name='root'))
        sm.add_widget(BusinessFolderScreen(name='business'))
        sm.add_widget(EconomicsFolderScreen(name='economics'))
        sm.add_widget(MixedFolderScreen(name='mixed'))
        sm.add_widget(ChapterDetailScreen(name='chapter_detail'))
        return sm

    def save_persistent_data(self):
        try:
            data = {
                "business_chapters": self.business_chapters,
                "econ_chapters": self.econ_chapters,
                "formulas": self.formulas,
                "glossary": self.glossary
            }
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"I/O Exception: {e}")

    def load_persistent_data(self):
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.business_chapters = data.get("business_chapters", self.business_chapters)
                    self.econ_chapters = data.get("econ_chapters", self.econ_chapters)
                    self.formulas = data.get("formulas", self.formulas)
                    self.glossary = data.get("glossary", self.glossary)
            except Exception as e:
                print(f"I/O Exception: {e}")

    def init_data(self):
        self.business_chapters = [
            {"number": 1, "unit": 1, "title": "Business Activity & Enterprise", "summary": "Needs, wants, scarcity, adding value.", "notes": "[b]Needs vs Wants:[/b] Needs are essential for survival (food, shelter); wants are non-essential preferences.\\n\\n[b]Scarcity:[/b] Finite resources vs infinite wants.\\n\\n[b]Factors of Production:[/b] Land (natural), Labour (human output), Capital (man-made tools/machinery), Enterprise (risk-bearing management).\\n\\n[b]Added Value:[/b] Selling Price - Cost of Bought-in Raw Materials."},
            {"number": 2, "unit": 1, "title": "Business Objectives", "summary": "Survival, profit, market share, growth, CSR.", "notes": "[b]Objectives:[/b] Survival (early-stage startups), Profit Maximisation (long-term return for owners), Market Share (market pricing dominance), Growth (economies of scale), CSR (ethical and sustainable practices)."},
            {"number": 3, "unit": 1, "title": "Sole Traders & Partnerships", "summary": "Unincorporated businesses, unlimited liability.", "notes": "[b]Sole Trader:[/b] Owned by 1 person. Total control, keeps all profit, but has unlimited liability and restricted finance.\\n\\n[b]Partnership:[/b] 2-20 partners. Pooled skills and capital, but joint unlimited liability and shared profits."},
            {"number": 4, "unit": 1, "title": "Limited Companies (Ltd & Plc)", "summary": "Incorporation, separate legal identity, limited liability.", "notes": "[b]Ltd:[/b] Shares sold privately with board consent. Limited liability, but financial accounts are public.\\n\\n[b]Plc:[/b] Shares traded on stock exchange. Huge capital generation, but vulnerable to hostile takeovers."},
            {"number": 5, "unit": 1, "title": "Franchises & Social Enterprises", "summary": "Franchising model and non-profit organisations.", "notes": "[b]Franchising:[/b] Franchisor sells brand identity; franchisee pays initial fee + ongoing royalties.\\n\\n[b]Social Enterprises:[/b] Surpluses reinvested into social/environmental missions."},
            {"number": 6, "unit": 1, "title": "Public Sector Corporations", "summary": "State-owned utilities and merit goods.", "notes": "[b]Public Sector:[/b] Government owned and funded via taxation. Focuses on social welfare rather than profit maximisation."},
            {"number": 7, "unit": 1, "title": "Classification of Businesses", "summary": "Primary, secondary, tertiary sectors; de-industrialisation.", "notes": "[b]Sectors:[/b] Primary (extraction), Secondary (manufacturing/processing), Tertiary (services).\\n\\n[b]De-industrialisation:[/b] Structural decline of manufacturing sector relative to tertiary."},
            {"number": 8, "unit": 1, "title": "Business Location Decisions", "summary": "Proximity to market, raw materials, labour, transport.", "notes": "[b]Location Drivers:[/b] Proximity to customers (retail), proximity to materials (weight-losing processes), transport links, labour pool, government grants."},
            {"number": 9, "unit": 1, "title": "Internal & External Growth", "summary": "Organic growth vs mergers, takeovers, integration.", "notes": "[b]Organic Growth:[/b] Retained profits, opening new sites.\\n\\n[b]Integration Types:[/b] Horizontal (same stage), Vertical Backward (suppliers), Vertical Forward (retailers), Conglomerate (unrelated markets)."},
            {"number": 10, "unit": 1, "title": "Government Influences & Law", "summary": "Employment, consumer protection, competition laws.", "notes": "[b]Legal Safeguards:[/b] Consumer rights (fitness for purpose), employment law (minimum wage, redundancy terms, anti-discrimination), competition commission (anti-cartel)."},
            {"number": 11, "unit": 1, "title": "Economic Influences", "summary": "Interest rates, inflation, unemployment, exchange rates.", "notes": "[b]Economic Indicators:[/b] Higher interest rates increase borrowing costs; inflation erodes consumer purchasing power; unemployment provides larger labour pool at lower wages."},
            {"number": 12, "unit": 1, "title": "Environmental & Ethical Issues", "summary": "Externalities, pollution, sustainability, pressure groups.", "notes": "[b]Negative Externalities:[/b] Unintended third-party costs (pollution).\\n\\n[b]Ethical Standards:[/b] Fairtrade sourcing, living wages, refusing child labour."},
            {"number": 13, "unit": 1, "title": "International Trade & Globalisation", "summary": "Tariffs, quotas, multinationals, free trade.", "notes": "[b]Trade Barriers:[/b] Tariffs (customs tax), Quotas (physical volume limits).\\n\\n[b]MNCs:[/b] Bring inward FDI and jobs, but may repatriate profits."},
            {"number": 14, "unit": 2, "title": "Internal Organisational Structures", "summary": "Hierarchy, span of control, chain of command.", "notes": "[b]Tall Hierarchy:[/b] Many management levels, narrow spans of control.\\n\\n[b]Flat Hierarchy:[/b] Few levels, wide spans of control, faster communication."},
            {"number": 15, "unit": 2, "title": "Centralisation & Decentralisation", "summary": "Head office control vs local branch delegation.", "notes": "[b]Centralisation:[/b] Strategic decisions kept at executive HQ.\\n\\n[b]Decentralisation:[/b] Authority delegated to branch managers, boosting local responsiveness."},
            {"number": 16, "unit": 2, "title": "Recruitment & Selection", "summary": "Job description, person specification, internal vs external.", "notes": "[b]Job Description:[/b] Tasks and responsibilities.\\n\\n[b]Person Spec:[/b] Qualifications and skills required.\\n\\n[b]Internal vs External:[/b] Internal is cheaper and faster; external injects fresh skills."},
            {"number": 17, "unit": 2, "title": "Employee Training & Development", "summary": "Induction, on-the-job, off-the-job training.", "notes": "[b]Induction:[/b] Orientation for new staff.\\n\\n[b]On-the-job:[/b] Shadowing at the workstation.\\n\\n[b]Off-the-job:[/b] Specialist external training courses."},
            {"number": 18, "unit": 2, "title": "Motivation Theories", "summary": "Taylor, Maslow hierarchy, Herzberg dual factor.", "notes": "[b]Taylor:[/b] Motivated purely by money (piece-rate).\\n\\n[b]Maslow:[/b] Physiological -> Safety -> Social -> Esteem -> Self-actualisation.\\n\\n[b]Herzberg:[/b] Hygiene factors prevent dissatisfaction; Motivators drive performance."},
            {"number": 19, "unit": 2, "title": "Methods of Motivation", "summary": "Financial incentives vs non-financial enrichment.", "notes": "[b]Financial:[/b] Piece-rate, commission, bonuses, PRP.\\n\\n[b]Non-financial:[/b] Job rotation, job enlargement, job enrichment, flexible scheduling."},
            {"number": 20, "unit": 2, "title": "Leadership Styles", "summary": "Autocratic, democratic, laissez-faire.", "notes": "[b]Autocratic:[/b] Direct orders without consultation.\\n\\n[b]Democratic:[/b] Consults workforce, delegates decisions.\\n\\n[b]Laissez-faire:[/b] Hands-off autonomy for skilled teams."},
            {"number": 21, "unit": 3, "title": "Sources of Finance", "summary": "Short-term (overdraft, trade credit) vs long-term (shares, loans).", "notes": "[b]Short-Term:[/b] Bank overdraft, trade credit, debt factoring.\\n\\n[b]Long-Term:[/b] Retained profit, share issues, bank loans, venture capital."},
            {"number": 22, "unit": 3, "title": "Costs, Revenues & Profit", "summary": "Fixed, variable, total costs, total revenue, profit.", "notes": "[b]Formulas:[/b] TC = FC + VC\\nTR = Price * Quantity\\nProfit = Total Revenue - Total Cost."},
            {"number": 23, "unit": 3, "title": "Break-even Analysis", "summary": "Contribution, break-even output formula, margin of safety.", "notes": "[b]Contribution:[/b] Price - Variable Cost per unit.\\n\\n[b]BEP:[/b] Total Fixed Costs / Contribution per unit.\\n\\n[b]Margin of Safety:[/b] Actual Output - Break-even Output."},
            {"number": 24, "unit": 3, "title": "Cash Flow Forecasting", "summary": "Inflows, outflows, net cash flow, opening/closing balance.", "notes": "[b]Net Cash Flow:[/b] Inflows - Outflows.\\n\\n[b]Closing Balance:[/b] Opening Balance + Net Cash Flow.\\n\\nCash is liquid money to pay immediate bills; profit is long-term net financial gain."},
            {"number": 25, "unit": 3, "title": "Income Statements", "summary": "Gross profit, operating profit, net profit for the year.", "notes": "[b]Structure:[/b] Revenue - Cost of Sales = Gross Profit.\\nGross Profit - Expenses = Operating Profit.\\nOperating Profit - (Tax + Interest) = Net Profit for the Year."},
            {"number": 26, "unit": 3, "title": "Statement of Financial Position", "summary": "Non-current/current assets, liabilities, net equity.", "notes": "[b]Assets:[/b] Non-current (premises, machinery) + Current (cash, inventory, debtors).\\n\\n[b]Liabilities:[/b] Current (overdraft, creditors) + Non-current (mortgage).\\n\\n[b]Net Assets:[/b] Total Assets - Total Liabilities."},
            {"number": 27, "unit": 3, "title": "Financial Ratio Analysis", "summary": "GPM, NPM, ROCE, Current Ratio, Acid Test Ratio.", "notes": "[b]GPM:[/b] (Gross Profit / Revenue) * 100\\n[b]NPM:[/b] (Net Profit / Revenue) * 100\\n[b]ROCE:[/b] (Operating Profit / Capital Employed) * 100\\n[b]Current Ratio:[/b] Current Assets / Current Liabilities\\n[b]Acid Test:[/b] (Current Assets - Stock) / Current Liabilities."},
            {"number": 28, "unit": 4, "title": "The Role of Marketing", "summary": "Customer needs, market vs product orientation.", "notes": "[b]Market Orientation:[/b] Researching consumer needs before product design.\\n\\n[b]Product Orientation:[/b] Making the product first, then finding buyers.\\n\\n[b]Mass vs Niche:[/b] Mass targets broad markets (high volume, low margins); niche targets specialized segments (low volume, high margins)."},
            {"number": 29, "unit": 4, "title": "Market Research", "summary": "Primary (field) vs secondary (desk) research.", "notes": "[b]Primary Research:[/b] Surveys, interviews, focus groups (first-hand, specific, but costly).\\n\\n[b]Secondary Research:[/b] Reports, census, industry journals (cheap, fast, but may be outdated)."},
            {"number": 30, "unit": 4, "title": "Market Segmentation", "summary": "Demographic, geographic, psychographic, behavioural.", "notes": "[b]Segmentation Bases:[/b] Demographic (age, gender, income), Geographic (location, climate), Psychographic (lifestyle, values), Behavioural (loyalty, usage rate)."},
            {"number": 31, "unit": 4, "title": "Product Life Cycle", "summary": "Development, introduction, growth, maturity, decline.", "notes": "[b]Stages:[/b] Introduction (high costs, low sales) -> Growth (rising sales, profits rise) -> Maturity (peak sales) -> Decline (slump).\\n\\n[b]Extension Strategies:[/b] Rebranding, updated packaging, new export markets."},
            {"number": 32, "unit": 4, "title": "Boston Matrix (BCG)", "summary": "Stars, Cash Cows, Question Marks, Dogs.", "notes": "[b]Stars:[/b] High share, high growth (needs investment).\\n[b]Cash Cows:[/b] High share, low growth (generates surplus cash).\\n[b]Question Marks:[/b] Low share, high growth (needs funding or divestment).\\n[b]Dogs:[/b] Low share, low growth (divest)."},
            {"number": 33, "unit": 4, "title": "Pricing Strategies", "summary": "Cost-plus, skimming, penetration, competitive, psychological.", "notes": "[b]Cost-plus:[/b] Unit cost + markup.\\n[b]Penetration:[/b] Low initial price to undercut rivals and build market share.\\n[b]Skimming:[/b] High initial price for new tech innovations.\\n[b]Psychological:[/b] e.g. $9.99 instead of $10.00."},
            {"number": 34, "unit": 4, "title": "Promotion & Advertising", "summary": "Above-the-line mass media vs below-the-line incentives.", "notes": "[b]Above-the-line (ATL):[/b] TV, radio, billboard campaigns (broad reach, costly).\\n\\n[b]Below-the-line (BTL):[/b] Direct coupons, loyalty cards, sponsorship, PR, BOGOF promotions."},
            {"number": 35, "unit": 4, "title": "Place & Channels of Distribution", "summary": "Direct, retail, wholesale distribution channels.", "notes": "[b]Direct Channel:[/b] Manufacturer -> Consumer (max margins, e-commerce).\\n[b]Retail Channel:[/b] Manufacturer -> Retailer -> Consumer.\\n[b]Wholesale:[/b] Manufacturer -> Wholesaler -> Retailer -> Consumer (breaks bulk, stores stock)."},
            {"number": 36, "unit": 4, "title": "E-Commerce & Digital Marketing", "summary": "Online retail, social media advertising, global reach.", "notes": "[b]Benefits:[/b] 24/7 global reach, lower fixed property costs.\\n\\n[b]Drawbacks:[/b] High parcel delivery and return logistics costs, website security vulnerabilities."},
            {"number": 37, "unit": 5, "title": "Methods of Production", "summary": "Job, batch, and flow (mass) production systems.", "notes": "[b]Job Production:[/b] Bespoke, single one-off items (high margins, slow).\\n[b]Batch Production:[/b] Sets of identical items made together before retooling.\\n[b]Flow Production:[/b] Continuous assembly lines (mass volume, low unit cost)."},
            {"number": 38, "unit": 5, "title": "Productivity & Efficiency", "summary": "Labour productivity, automation, division of labour.", "notes": "[b]Labour Productivity:[/b] Total Output / Total Workers.\\n\\n[b]Methods to Improve:[/b] Automation, training, lean workflows, division of labour."},
            {"number": 39, "unit": 5, "title": "Lean Production & Kaizen", "summary": "Waste elimination, continuous improvement, JIT.", "notes": "[b]Lean Production:[/b] Eliminating non-value-adding waste (TIMWOOD: transport, inventory, motion, waiting, overproduction, overprocessing, defects).\\n\\n[b]Kaizen:[/b] Continuous incremental improvement."},
            {"number": 40, "unit": 5, "title": "Just-in-Time (JIT) Stock Management", "summary": "Zero buffer stock systems vs Just-in-Case buffer security.", "notes": "[b]JIT:[/b] Materials arrive only as needed on the assembly line. Eliminates storage costs and stock decay. Highly vulnerable to supply-chain delays."},
            {"number": 41, "unit": 5, "title": "Inventory Control Charts", "summary": "Maximum stock, buffer stock, reorder level, lead time.", "notes": "[b]Chart Components:[/b] Maximum stock level, buffer (safety) stock, reorder level (triggers new order), lead time (delivery wait duration)."},
            {"number": 42, "unit": 5, "title": "Quality Management & Control", "summary": "QC inspection vs QA prevention and TQM culture.", "notes": "[b]Quality Control (QC):[/b] Inspecting end products for flaws (wasteful).\\n[b]Quality Assurance (QA):[/b] Standards at each production stage to prevent defects.\\n[b]TQM:[/b] Company-wide zero-defect culture."},
            {"number": 43, "unit": 5, "title": "Economies & Diseconomies of Scale", "summary": "Purchasing, technical, managerial economies; communication barriers.", "notes": "[b]Internal Economies of Scale:[/b] Bulk buying (purchasing), technical machinery, cheaper borrowing rates (financial).\\n\\n[b]Diseconomies of Scale:[/b] Poor communication, low worker morale in giant firms."},
            {"number": 44, "unit": 5, "title": "Supply Chain Management & Procurement", "summary": "Supplier relationships, logistics, ethical sourcing.", "notes": "[b]Supply Chain Priorities:[/b] Delivery reliability, competitive raw material costs, component quality, ethical labour standards across overseas suppliers."},
            {"number": 45, "unit": 5, "title": "Customer Service & After-Sales Care", "summary": "Customer retention, competitive advantage, brand loyalty.", "notes": "[b]Importance:[/b] Keeping existing customers costs less than acquiring new ones; supports premium pricing and positive word-of-mouth."},
            {"number": 46, "unit": 5, "title": "Technology in Business Operations", "summary": "CAD, CAM, robotics, automation.", "notes": "[b]CAD:[/b] Computer-aided design prototyping.\\n[b]CAM:[/b] Computer-aided automated manufacturing.\\nReduces unit labour costs and defects, but requires high initial capital investment."}
        ]

        self.econ_chapters = [
            {"number": 1, "unit": 1, "title": "The Economic Problem & Scarcity", "summary": "Finite resources vs infinite human wants, resource allocation.", "notes": "[b]The Economic Problem:[/b] Scarcity exists because resources are finite while wants are infinite.\\n\\n[b]Economic Agents:[/b] Consumers (maximise utility), Producers (maximise profit), Government (maximise social welfare)."},
            {"number": 2, "unit": 1, "title": "Opportunity Cost & PPF Curves", "summary": "Trade-offs, Production Possibility Frontiers, efficiency.", "notes": "[b]Opportunity Cost:[/b] The cost of the next best alternative forgone.\\n\\n[b]PPF Curve:[/b] Maximum output combination of two goods using all resources efficiently. Outward shift indicates long-run economic growth."},
            {"number": 3, "unit": 1, "title": "Demand Factors & Demand Curves", "summary": "Law of demand, income effect, substitutes, complements.", "notes": "[b]Law of Demand:[/b] As price rises, quantity demanded contracts.\\n\\n[b]Shifts (PASIFIC):[/b] Population, Advertising, Substitutes, Income, Fashions, Interest rates, Complements."},
            {"number": 4, "unit": 1, "title": "Supply Factors & Supply Curves", "summary": "Law of supply, costs of production, subsidies, indirect taxes.", "notes": "[b]Law of Supply:[/b] As price rises, quantity supplied expands.\\n\\n[b]Shifts (PINTS WC):[/b] Productivity, Indirect taxes, Number of firms, Technology, Subsidies, Weather, Costs of production."},
            {"number": 5, "unit": 1, "title": "Market Equilibrium & Price Determination", "summary": "Market clearing price, excess demand, excess supply.", "notes": "[b]Equilibrium:[/b] Quantity Demanded = Quantity Supplied.\\n\\n[b]Shortage (Excess Demand):[/b] Price below equilibrium; buyers bid up price.\\n\\n[b]Surplus (Excess Supply):[/b] Price above equilibrium; sellers discount price."},
            {"number": 6, "unit": 1, "title": "Price Elasticity of Demand (PED)", "summary": "Formula, determinants, elastic vs inelastic, revenue impacts.", "notes": "[b]PED Formula:[/b] % Change in QD / % Change in Price.\\n\\n[b]Inelastic (PED < 1):[/b] Raising price increases total revenue (necessities).\\n[b]Elastic (PED > 1):[/b] Lowering price increases total revenue (many substitutes)."},
            {"number": 7, "unit": 1, "title": "Income Elasticity of Demand (YED)", "summary": "Normal goods, inferior goods, luxury items.", "notes": "[b]YED Formula:[/b] % Change in QD / % Change in Income.\\n\\n• Normal Goods: YED > 0 (demand rises as income rises).\\n• Inferior Goods: YED < 0 (demand falls as income rises).\\n• Luxury Goods: YED > 1."},
            {"number": 8, "unit": 1, "title": "Price Elasticity of Supply (PES)", "summary": "Determinants of supply elasticity, spare capacity, lead times.", "notes": "[b]PES Formula:[/b] % Change in QS / % Change in Price.\\n\\n[b]Determinants:[/b] Spare factory capacity, level of stock inventory, production lead time, factor mobility."},
            {"number": 9, "unit": 1, "title": "The Price Mechanism", "summary": "Signalling, incentive, and rationing functions of prices.", "notes": "[b]Functions:[/b]\\n1. Signalling: Prices show market changes.\\n2. Incentive: Higher prices encourage suppliers to produce more.\\n3. Rationing: Rising prices allocate scarce goods to those willing and able to pay."},
            {"number": 10, "unit": 1, "title": "Indirect Taxes & Subsidies", "summary": "Specific vs ad valorem taxes, producer subsidies, tax incidence.", "notes": "[b]Indirect Tax:[/b] Tax on spending; shifts supply curve left. Consumers pay most of the tax if demand is inelastic.\\n\\n[b]Subsidy:[/b] Government grant to producers; shifts supply curve right, lowering consumer prices."},
            {"number": 11, "unit": 1, "title": "Price Controls (Max & Min Prices)", "summary": "Price ceilings (rent controls) and price floors (minimum wages).", "notes": "[b]Maximum Price (Ceiling):[/b] Set below equilibrium to protect consumers. Creates shortages and black markets.\\n\\n[b]Minimum Price (Floor):[/b] Set above equilibrium. Creates excess supply/surpluses."},
            {"number": 12, "unit": 1, "title": "Market Failure & Externalities", "summary": "Private vs social costs/benefits, market failure causes.", "notes": "[b]Market Failure:[/b] Free-market price mechanism misallocates resources.\\n\\n[b]Negative Externalities:[/b] Social Cost > Private Cost (pollution). Overproduced by free market.\\n\\n[b]Positive Externalities:[/b] Social Benefit > Private Benefit (education). Underconsumed in free market."},
            {"number": 13, "unit": 1, "title": "Public & Merit Goods", "summary": "Non-rivalry, non-excludability, free-rider problem.", "notes": "[b]Public Goods:[/b] Non-excludable and non-rival (street lighting, defence). Free-rider problem prevents private market supply; funded by taxation.\\n\\n[b]Merit Goods:[/b] Underconsumed due to information failure (healthcare)."},
            {"number": 14, "unit": 1, "title": "Government Intervention in Markets", "summary": "Legislation, regulation, state provision, pollution permits.", "notes": "[b]Interventions:[/b] Indirect taxes on demerit goods, state funding of public goods, advertising bans, tradable carbon emissions permits."},
            {"number": 15, "unit": 1, "title": "Labour Markets & Wage Determination", "summary": "Derived demand for labour, supply of labour, equilibrium wages.", "notes": "[b]Derived Demand:[/b] Labour is demanded for the goods it produces.\\n\\n[b]Wage Determination:[/b] Intersection of labour demand and labour supply curves."},
            {"number": 16, "unit": 1, "title": "Trade Unions & Minimum Wages", "summary": "Collective bargaining, wage effects, classical unemployment.", "notes": "[b]Trade Unions:[/b] Collective bargaining for higher pay and safer working conditions.\\n\\n[b]National Minimum Wage:[/b] Statutory floor; protects low-wage workers, but can cause unemployment if set too high above equilibrium."},
            {"number": 17, "unit": 1, "title": "Production & Costs of Production", "summary": "Short run vs long run, fixed, variable, marginal, average costs.", "notes": "[b]Short vs Long Run:[/b] At least one fixed factor in short run; all factors variable in long run.\\n\\nATC = Total Cost / Output\\nMC = Cost of one extra unit."},
            {"number": 18, "unit": 1, "title": "Revenue & Profit Maximisation", "summary": "TR, AR, MR, normal profit vs supernormal profit.", "notes": "[b]Revenues:[/b] TR = Price * Output\\nAR = TR / Output = Price\\n\\n[b]Profits:[/b] Normal profit (covers opportunity cost); Supernormal profit (profit above normal profit)."},
            {"number": 19, "unit": 1, "title": "Competitive Markets (Perfect Competition)", "summary": "Price takers, homogeneous goods, perfect information.", "notes": "[b]Characteristics:[/b] Countless buyers and sellers, identical goods, no entry/exit barriers. Firms are price takers and earn only normal profit in the long run."},
            {"number": 20, "unit": 1, "title": "Monopoly Markets", "summary": "Price makers, barriers to entry, deadweight loss, inefficiency.", "notes": "[b]Monopoly:[/b] Single dominant supplier (>25% legally, 100% pure). High entry barriers (patents, scale). Can restrict output to charge higher prices."},
            {"number": 21, "unit": 1, "title": "Oligopoly Markets", "summary": "Interdependence, game theory, collusion, price rigidity.", "notes": "[b]Oligopoly:[/b] Dominated by a few large firms. High concentration ratio, interdependent decisions.\\n\\n[b]Collusion:[/b] Illegal agreements between rival firms to fix prices or carve up markets."},
            {"number": 22, "unit": 1, "title": "Privatisation & Competition Policy", "summary": "Sale of state assets, deregulation, regulatory bodies.", "notes": "[b]Privatisation:[/b] Transfer of state assets to private sector to increase efficiency.\\n\\n[b]Deregulation:[/b] Removing legal barriers to entry to increase competition."},
            {"number": 23, "unit": 2, "title": "Gross Domestic Product (GDP) & Growth", "summary": "Real vs nominal GDP, measuring growth, living standards.", "notes": "[b]GDP:[/b] Total value of goods and services produced within a country in a year.\\n\\n[b]Real GDP:[/b] Adjusted for inflation.\\n\\n[b]GDP per Capita:[/b] Real GDP / Population (tracks living standards)."},
            {"number": 24, "unit": 2, "title": "The Economic (Business) Cycle", "summary": "Boom, downturn, recession, recovery, output gaps.", "notes": "[b]Cycle Stages:[/b] Boom (rapid growth, low unemployment, rising inflation) -> Downturn -> Recession (two consecutive quarters of negative growth) -> Recovery."},
            {"number": 25, "unit": 2, "title": "Inflation & Price Stability", "summary": "Consumer Price Index (CPI), demand-pull and cost-push inflation.", "notes": "[b]Inflation:[/b] Sustained increase in the general price level.\\n\\n[b]Causes:[/b] Demand-pull (excess aggregate demand) vs Cost-push (rising costs of production/imported raw materials)."},
            {"number": 26, "unit": 2, "title": "Deflation", "summary": "Malignant vs benign deflation, deflationary spirals.", "notes": "[b]Deflation:[/b] Sustained fall in general price level (inflation < 0%). Consumers delay purchases expecting cheaper prices, triggering a deflationary economic spiral."},
            {"number": 27, "unit": 2, "title": "Employment & Unemployment", "summary": "Claimant count vs ILO Labour Force Survey, economic costs.", "notes": "[b]Unemployment:[/b] Working age individuals seeking work but unable to find jobs.\\n\\n[b]Measures:[/b] Claimant Count (benefit claims) vs ILO Labour Force Survey (interviews)."},
            {"number": 28, "unit": 2, "title": "Causes & Types of Unemployment", "summary": "Cyclical, structural, frictional, and seasonal unemployment.", "notes": "[b]Types:[/b] Cyclical (demand-deficient due to recession), Structural (mismatch of worker skills to new industries), Frictional (moving between jobs), Seasonal (climate/tourism)."},
            {"number": 29, "unit": 2, "title": "The Balance of Payments (Current Account)", "summary": "Trade in goods/services, primary and secondary income.", "notes": "[b]Current Account:[/b] Trade in Goods + Trade in Services + Primary Income (investment profits) + Secondary Income (transfers/aid).\\n\\n[b]Deficit:[/b] Total Imports > Total Exports."},
            {"number": 30, "unit": 2, "title": "Fiscal Policy", "summary": "Government spending, direct/indirect taxation, budget balances.", "notes": "[b]Fiscal Policy:[/b] Managing aggregate demand via taxation and state spending.\\n\\n[b]Expansionary:[/b] Higher spending and lower taxes (used in recessions).\\n\\n[b]Contractionary:[/b] Cut spending and raise taxes to curb inflation."},
            {"number": 31, "unit": 2, "title": "Monetary Policy", "summary": "Central bank interest rates, money supply, quantitative easing.", "notes": "[b]Monetary Policy:[/b] Managed by central banks.\\n\\n• Raising interest rates: Increases borrowing costs, encourages saving, lowers inflation.\\n• Lowering interest rates: Stimulates borrowing and investment."},
            {"number": 32, "unit": 2, "title": "Supply-Side Policies", "summary": "Market-based vs interventionist policies, shifting LRAS.", "notes": "[b]Objective:[/b] Shifts Long-Run Aggregate Supply (LRAS) right.\\n\\n• Market-Based: Deregulation, lower corporate taxes, cutting red tape.\\n• Interventionist: Spending on roads/rail, education, and R&D."},
            {"number": 33, "unit": 2, "title": "Macroeconomic Policy Conflicts", "summary": "Trade-offs: growth vs inflation, unemployment vs inflation.", "notes": "[b]Trade-Offs:[/b] Growth vs Inflation; Low Unemployment vs Wage Inflation (Phillips curve); Economic Growth vs Current Account Deficit."},
            {"number": 34, "unit": 2, "title": "Income Inequality & Poverty", "summary": "Absolute vs relative poverty, Lorenz curve, Gini coefficient.", "notes": "[b]Absolute Poverty:[/b] Cannot afford basic food/shelter necessities.\\n\\n[b]Relative Poverty:[/b] Income significantly below national median (e.g. <60%).\\n\\n[b]Gini Coefficient:[/b] Measures inequality from 0 (equality) to 1 (inequality)."},
            {"number": 35, "unit": 2, "title": "Redistribution of Income Policies", "summary": "Progressive, regressive, proportional taxes, welfare transfers.", "notes": "[b]Taxes:[/b] Progressive (takes higher % from high earners), Regressive (takes higher % from low earners; VAT), Proportional (flat rate).\\n\\n[b]Transfers:[/b] Welfare benefits."},
            {"number": 36, "unit": 2, "title": "Globalisation & Multinationals", "summary": "Causes of globalisation, foreign direct investment, MNC impacts.", "notes": "[b]Drivers:[/b] Container shipping, digital communications, WTO trade tariff cuts.\\n\\n[b]Impacts:[/b] Inward FDI, jobs, lower prices, but risks environmental exploitation and profit repatriation."},
            {"number": 37, "unit": 2, "title": "International Specialisation & Comparative Advantage", "summary": "Absolute vs comparative advantage, opportunity cost ratios.", "notes": "[b]Comparative Advantage:[/b] Producing a good at a lower opportunity cost than another country. Specialisation expands global trade output and lowers prices."},
            {"number": 38, "unit": 2, "title": "Trade Protectionism & Trade Barriers", "summary": "Tariffs, import quotas, subsidies, infant industry arguments.", "notes": "[b]Protectionist Tools:[/b] Tariffs (import tax), Quotas (import volume limits), Domestic Subsidies.\\n\\n[b]Arguments:[/b] Protect infant industries, stop dumping, save domestic jobs."},
            {"number": 39, "unit": 2, "title": "Trading Blocs & The WTO", "summary": "Free trade areas, customs unions, trade creation vs diversion.", "notes": "[b]Free Trade Area:[/b] Zero tariffs between member countries.\\n\\n[b]Customs Union:[/b] Free trade internally + Common External Tariff on non-members.\\n\\n[b]WTO:[/b] Global trade arbiter and tariff reduction body."},
            {"number": 40, "unit": 2, "title": "Foreign Exchange Rates", "summary": "Floating vs fixed exchange rates, depreciation, appreciation.", "notes": "[b]Floating Rate:[/b] Determined by market currency demand and supply.\\n\\n[b]SPICED:[/b] Strong Pound Imports Cheap Exports Dear.\\n\\n[b]WPIDEC:[/b] Weak Pound Imports Dear Exports Cheap."},
            {"number": 41, "unit": 2, "title": "Exchange Rate Impacts on the Economy", "summary": "Effects on inflation, current account, GDP, and debt.", "notes": "[b]Depreciation:[/b] Exports become cheaper abroad, imports cost more. Improves trade balance and GDP, but risks imported cost-push inflation."},
            {"number": 42, "unit": 2, "title": "Economic Development & Sustainability", "summary": "Human Development Index (HDI) vs GDP, sustainable growth.", "notes": "[b]HDI:[/b] Composite measure tracking life expectancy (health), years of schooling (education), and GNI per capita (income).\\n\\n[b]Sustainability:[/b] Growth without compromising future generations."}
        ]

        self.formulas = [
            {"name": "Total Revenue (TR)", "category": "Business Finance", "formula": "Selling Price * Quantity Sold"},
            {"name": "Total Cost (TC)", "category": "Business Finance", "formula": "Total Fixed Costs (TFC) + Total Variable Costs (TVC)"},
            {"name": "Average Cost (AC)", "category": "Business Finance", "formula": "Total Cost / Total Output"},
            {"name": "Total Profit / Loss", "category": "Business Finance", "formula": "Total Revenue (TR) - Total Cost (TC)"},
            {"name": "Contribution per Unit", "category": "Break-even Analysis", "formula": "Selling Price - Variable Cost per unit"},
            {"name": "Total Contribution", "category": "Break-even Analysis", "formula": "Contribution per unit * Units Sold  (OR: Total Revenue - Total Variable Costs)"},
            {"name": "Break-even Output (BEP)", "category": "Break-even Analysis", "formula": "Total Fixed Costs / Contribution per unit"},
            {"name": "Margin of Safety", "category": "Break-even Analysis", "formula": "Actual (or Budgeted) Sales Output - Break-even Output"},
            {"name": "Net Cash Flow", "category": "Cash Flow", "formula": "Total Cash Inflows - Total Cash Outflows"},
            {"name": "Closing Cash Balance", "category": "Cash Flow", "formula": "Opening Cash Balance + Net Cash Flow"},
            {"name": "Cost of Goods Sold (COGS)", "category": "Income Statement", "formula": "Opening Inventory + Purchases - Closing Inventory"},
            {"name": "Gross Profit", "category": "Income Statement", "formula": "Sales Revenue - Cost of Goods Sold (COGS)"},
            {"name": "Operating Profit", "category": "Income Statement", "formula": "Gross Profit - Operating Expenses (Overheads)"},
            {"name": "Profit for the Year (Net Profit)", "category": "Income Statement", "formula": "Operating Profit - (Interest Charges + Tax)"},
            {"name": "Gross Profit Margin (GPM)", "category": "Profitability Ratios", "formula": "(Gross Profit / Sales Revenue) * 100"},
            {"name": "Net Profit Margin (NPM)", "category": "Profitability Ratios", "formula": "(Profit for the Year / Sales Revenue) * 100"},
            {"name": "Return on Capital Employed (ROCE)", "category": "Profitability Ratios", "formula": "(Operating Profit / Capital Employed) * 100"},
            {"name": "Working Capital", "category": "Balance Sheet", "formula": "Current Assets - Current Liabilities"},
            {"name": "Current Ratio", "category": "Liquidity Ratios", "formula": "Current Assets / Current Liabilities  (Ideal: 1.5 - 2.0 : 1)"},
            {"name": "Acid Test Ratio", "category": "Liquidity Ratios", "formula": "(Current Assets - Inventory) / Current Liabilities  (Ideal: 1.0 : 1)"},
            {"name": "Added Value", "category": "Operations", "formula": "Selling Price - Cost of Bought-in Raw Materials"},
            {"name": "Labour Productivity", "category": "Operations", "formula": "Total Output / Total Number of Workers"},
            {"name": "Market Share", "category": "Marketing", "formula": "(Business Sales / Total Market Sales) * 100"},
            {"name": "Percentage Change", "category": "General Economics", "formula": "((New Value - Original Value) / Original Value) * 100"},
            {"name": "Price Elasticity of Demand (PED)", "category": "Microeconomics", "formula": "% Change in Quantity Demanded / % Change in Price"},
            {"name": "Income Elasticity of Demand (YED)", "category": "Microeconomics", "formula": "% Change in Quantity Demanded / % Change in Income"},
            {"name": "Price Elasticity of Supply (PES)", "category": "Microeconomics", "formula": "% Change in Quantity Supplied / % Change in Price"},
            {"name": "Real GDP", "category": "Macroeconomics", "formula": "(Nominal GDP / CPI Price Index) * 100"},
            {"name": "GDP per Capita", "category": "Macroeconomics", "formula": "Real GDP / Total Population"},
            {"name": "Unemployment Rate", "category": "Macroeconomics", "formula": "(Number of Unemployed / Total Labour Force) * 100"},
            {"name": "Inflation Rate (CPI %)", "category": "Macroeconomics", "formula": "((CPI in Year 2 - CPI in Year 1) / CPI in Year 1) * 100"},
            {"name": "Balance of Trade in Goods", "category": "Macroeconomics", "formula": "Visible Exports - Visible Imports"},
            {"name": "Current Account Balance", "category": "Macroeconomics", "formula": "Trade in Goods + Trade in Services + Net Primary Income + Net Secondary Income"},
            {"name": "Aggregate Demand (AD)", "category": "Macroeconomics", "formula": "C + I + G + (X - M)"}
        ]

        self.glossary = [
            {"term": "Acid Test Ratio", "subject": "Business", "definition": "A liquidity ratio: (Current Assets - Inventory) / Current Liabilities. Evaluates short-term liquidity without selling stock."},
            {"term": "Added Value", "subject": "Business", "definition": "The difference between the selling price of a finished product and the cost of bought-in raw materials."},
            {"term": "Aggregate Demand (AD)", "subject": "Economics", "definition": "The total planned expenditure on all domestic goods and services in an economy: AD = C + I + G + (X - M)."},
            {"term": "Aggregate Supply (AS)", "subject": "Economics", "definition": "The total quantity of goods and services domestic producers are willing and able to sell at a given price level."},
            {"term": "Autocratic Leadership", "subject": "Business", "definition": "Management style where the leader retains all authority and issues instructions without consulting staff."},
            {"term": "Balance of Payments", "subject": "Economics", "definition": "Financial record of all economic transactions between a country and the rest of the world over a year."},
            {"term": "Barriers to Entry", "subject": "Economics", "definition": "Obstacles that make it difficult for new firms to enter an industry (patents, scale economies)."},
            {"term": "Boston Matrix (BCG)", "subject": "Business", "definition": "Portfolio tool mapping products by market share and market growth (Stars, Cash Cows, Question Marks, Dogs)."},
            {"term": "Break-even Output", "subject": "Business", "definition": "The production level where Total Revenue equals Total Costs, yielding zero profit and zero loss."},
            {"term": "Buffer Stock", "subject": "Business", "definition": "Safety stock held in a warehouse to protect against unforeseen delivery delays or demand spikes."},
            {"term": "Centralisation", "subject": "Business", "definition": "Retaining major decision-making authority strictly at senior executive headquarters."},
            {"term": "Chain of Command", "subject": "Business", "definition": "The line of authority through which instructions pass from senior managers down to workers."},
            {"term": "Collusion", "subject": "Economics", "definition": "Agreements between rival firms in an oligopoly to fix prices or restrict production quotas."},
            {"term": "Comparative Advantage", "subject": "Economics", "definition": "The ability of a country to produce a good at a lower opportunity cost than another nation."},
            {"term": "Consumer Price Index (CPI)", "subject": "Economics", "definition": "An official monthly index measuring price changes in a representative basket of goods to track inflation."},
            {"term": "Current Ratio", "subject": "Business", "definition": "A liquidity ratio (Current Assets / Current Liabilities) testing if a firm can pay short-term debts."},
            {"term": "De-industrialisation", "subject": "Both", "definition": "Decline in the relative output and employment share of manufacturing in an economy."},
            {"term": "Demerit Good", "subject": "Economics", "definition": "A good where social costs exceed private costs; overconsumed in a free market (e.g. tobacco)."},
            {"term": "Diseconomies of Scale", "subject": "Both", "definition": "Rising Long-Run Average Costs as a firm grows too large, caused by communication and coordination issues."},
            {"term": "Division of Labour", "subject": "Both", "definition": "Separating a production process into distinct, specialized tasks performed by separate workers."},
            {"term": "Economies of Scale", "subject": "Both", "definition": "Reductions in Long-Run Average Costs resulting from increasing the scale of production."},
            {"term": "Fiscal Policy", "subject": "Economics", "definition": "Government taxation and public expenditure used to influence Aggregate Demand."},
            {"term": "Gross Domestic Product (GDP)", "subject": "Economics", "definition": "Total market value of all finished goods and services produced within a country over a year."},
            {"term": "Gross Profit Margin (GPM)", "subject": "Business", "definition": "Profitability percentage: (Gross Profit / Sales Revenue) * 100."},
            {"term": "Human Development Index (HDI)", "subject": "Economics", "definition": "UN index tracking life expectancy, schooling years, and GNI per capita."},
            {"term": "Just-in-Time (JIT)", "subject": "Business", "definition": "Lean production system where stock arrives at the exact moment needed on the line, eliminating buffer inventory."},
            {"term": "Kaizen", "subject": "Business", "definition": "Japanese management philosophy focused on continuous small incremental improvements by all workers."},
            {"term": "Limited Liability", "subject": "Business", "definition": "Shareholders only lose the capital invested in shares if the company fails; personal assets are safe."},
            {"term": "Margin of Safety", "subject": "Business", "definition": "The difference between current/budgeted sales output and the break-even output volume."},
            {"term": "Market Failure", "subject": "Economics", "definition": "When the free-market mechanism misallocates resources, causing a net loss in social welfare."},
            {"term": "Merit Good", "subject": "Economics", "definition": "A good generating positive externalities where social benefits exceed private benefits (healthcare)."},
            {"term": "Monetary Policy", "subject": "Economics", "definition": "Central bank management of base interest rates and the money supply to keep prices stable."},
            {"term": "Monopoly", "subject": "Both", "definition": "Market dominated by a single seller (>25% legally, 100% pure) with high barriers to entry."},
            {"term": "National Minimum Wage", "subject": "Both", "definition": "Statutory hourly wage rate floor below which employers cannot legally pay staff."},
            {"term": "Negative Externality", "subject": "Economics", "definition": "Adverse spillover cost imposed on third parties from economic production or consumption (pollution)."},
            {"term": "Net Profit Margin (NPM)", "subject": "Business", "definition": "Profitability ratio: (Profit for the Year / Sales Revenue) * 100."},
            {"term": "Oligopoly", "subject": "Both", "definition": "Market dominated by a few large firms with high concentration ratios and interdependent pricing."},
            {"term": "Opportunity Cost", "subject": "Both", "definition": "The cost of the next best alternative given up when selecting an economic choice."},
            {"term": "Price Elasticity of Demand (PED)", "subject": "Both", "definition": "Metric measuring responsiveness of quantity demanded to price: % change in QD / % change in Price."},
            {"term": "Product Life Cycle (PLC)", "subject": "Business", "definition": "Commercial stages of a product: Development, Introduction, Growth, Maturity, and Decline."},
            {"term": "Protectionism", "subject": "Economics", "definition": "Trade barriers (tariffs, quotas, subsidies) shielding domestic firms from foreign imports."},
            {"term": "Public Good", "subject": "Economics", "definition": "Non-excludable and non-rival good (street lighting); must be funded by the state."},
            {"term": "Return on Capital Employed (ROCE)", "subject": "Business", "definition": "Profitability ratio: (Operating Profit / Capital Employed) * 100."},
            {"term": "Span of Control", "subject": "Business", "definition": "The number of direct subordinates reporting to a manager."},
            {"term": "SPICED", "subject": "Both", "definition": "Mnemonic: Strong Pound Imports Cheap Exports Dear."},
            {"term": "Supply-Side Policies", "subject": "Economics", "definition": "Government policies aimed at expanding productive capacity and shifting LRAS to the right."},
            {"term": "Total Quality Management (TQM)", "subject": "Business", "definition": "Company-wide approach where all staff are responsible for zero defects."},
            {"term": "Unlimited Liability", "subject": "Business", "definition": "Sole traders and partners are personally liable for all business debts to the point of bankruptcy."},
            {"term": "Working Capital", "subject": "Business", "definition": "Day-to-day liquidity for trading expenses: Current Assets - Current Liabilities."},
            {"term": "WPIDEC", "subject": "Both", "definition": "Mnemonic: Weak Pound Imports Dear Exports Cheap."}
        ]

if __name__ == '__main__':
    EdexcelIGCSEApp().run()
