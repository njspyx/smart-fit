
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.card import MDCardSwipe, MDCard
from kivymd.uix.picker import MDDatePicker

from gui.classify import predict_using_model
import webbrowser

KV = '''

        


<DialogBoxContent>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    
    MDTextField:
        name_text: self.text
        hint_text: "Food name"
        on_text: app.food_name = self.text
    
    MDTextField:
        calories_text: self.text
        id: calories
        hint_text: "Calories"
        on_text: app.calories = self.text

<GoalDialogBoxContent>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    
    MDTextField:
        goal_text: self.text
        id: goal
        hint_text: "New goal"
        on_text: app.goal = self.text

<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    type_swipe: "auto"
    on_swipe_complete: app.on_swipe_complete(root)
    
    MDCardSwipeLayerBox:
    
    MDCardSwipeFrontBox:
        
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            markup: True

<MDListSpacing>:
    size_hint_y: None
    height: self.minimum_size[1]
    spacing:10
    padding: (0, 10, 0, 0)

<ItemDrawer>:

<ResizingRow_GridLayout@GridLayout>:
    cols: 1
    height: sum([c.height for c in self.children])

<ContentNavigationDrawer>:

    ScrollView:
    
        MDListSpacing:
        
            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height

                Image:
                    id: avatar
                    size_hint: None, None
                    size: "100dp", "100dp"
                    source: "Capture.PNG"

            MDLabel:
                text: "SmartFit"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: " made by Neel Jay"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]

            MDList:

                OneLineIconListItem:
                    text: "Take a picture"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "camera scr" 
                        
                    IconLeftWidget:
                        icon: "camera"
            
                OneLineIconListItem:
                    text: "Get recipes"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "recipes scr"
                        
                    IconLeftWidget:
                        icon: "newspaper-variant"
                    
                OneLineIconListItem:
                    text: "Current entries"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "current entries scr" 
                        
                    IconLeftWidget:
                        icon: "plus"
                
                OneLineIconListItem:
                    text: "Daily entries"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "daily entries scr"
                        
                    IconLeftWidget:
                        icon: "chart-line"
                        
Screen:

    NavigationLayout:
        x: camera_toolbar.height
        size_hint_y: 1.0
        
        ScreenManager:
            id: screen_manager

            Screen:
                name: "camera scr"
                
                BoxLayout:
                    orientation: "vertical"
                    
                    MDToolbar:
                        id: camera_toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Camera"
                        left_action_items: 
                            [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    FloatLayout:
                        size_hint_y: 0.9
                        
                        MDRoundFlatIconButton:
                            text: "Take picture"
                            icon: "folder"
                            pos_hint: {"center_x": .5, "center_y": .5}
                            on_release: app.file_manager_open()
                            
                        MDRoundFlatIconButton:
                            text: "Upload image"
                            icon: "folder"
                            pos_hint: {"center_x": .5, "center_y": .6}
                            on_release: app.file_manager_open()

            Screen:
                name: "recipes scr"

                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    size_hint: (1,1)
                
                    MDToolbar:
                        id: recipe_toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Recipes"
                        left_action_items: 
                            [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    ScrollView:
                    
                        GridLayout:
                            padding: dp(10)
                            spacing: dp(15)
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                            halign: "center"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Ingredient list"
                                font_style: "H6"
                                
                            MDTextField:
                                id: ingredient_list
                                hint_text: "Enter items"
                                mode: "rectangle"
                            
                            AnchorLayout:
                                size_hint_y: None
                                height: recipe_btn.height
                                
                                MDRoundFlatButton:
                                    id: recipe_btn
                                    text: "Get recipes!"
                                    text_color: 0.5, 0.5, 0.5, 1
                                    pos_hint: {"center_x": 0.5}
                            
                            MDSeparator:
                            
                MDCard:
                    size_hint: None, None
                    size: "200dp", "75dp"
                    pos_hint: {"center_x": .5, "center_y": .53}
                    
                    MDBoxLayout:
                        id: content_box
                        spacing: "30dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        
                        MDLabel:
                            id: recipe_lbl
                            text: "cookpad"
                            font_style: "H6"
                            pos_hit: {"center_y": .75}
                            height: self.texture_size[1]
                        
                        MDRaisedButton:
                            text: "GO"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hit: {"center_y": .5}
                            
                MDCard:
                    size_hint: None, None
                    size: "200dp", "75dp"
                    pos_hint: {"center_x": .5, "center_y": .35} 
                              
                    MDBoxLayout:
                        id: content_box
                        spacing: "30dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        
                        MDLabel:
                            id: recipe_lbl
                            text: "BigOven"
                            font_style: "H6"
                            pos_hit: {"center_y": .75}
                            height: self.texture_size[1]
                        
                        MDRaisedButton:
                            text: "GO"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hit: {"center_y": .5}
                
                MDCard:
                    size_hint: None, None
                    size: "200dp", "75dp"
                    pos_hint: {"center_x": .5, "center_y": .17} 
                              
                    MDBoxLayout:
                        id: content_box
                        spacing: "30dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        
                        MDLabel:
                            id: recipe_lbl
                            text: "allrecipe"
                            font_style: "H6"
                            pos_hit: {"center_y": .75}
                            height: self.texture_size[1]
                        
                        MDRaisedButton:
                            text: "GO"
                            md_bg_color: app.theme_cls.primary_color
                            pos_hit: {"center_y": .5}
                                        
                
            Screen:
                name: "current entries scr"
                
                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    size_hint: (1,1)
                
                    MDToolbar:
                        id: current_toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Current Entries"
                        left_action_items: 
                            [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    ScrollView:
                    
                        GridLayout:
                            padding: dp(10)
                            spacing: dp(15)
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                            halign: "center"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Total"
                                font_style: "H6"
                                
                            MDSeparator:
                            
                            AnchorLayout:
                                size_hint_y: None
                                height: 100
                                
                                MDLabel:
                                    id: lbl_calorie_total
                                    halign: "center"
                                    font_style: "H3"
                                    text: "0"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Entries"
                                font_style: "H6"
                                margin: (0, 10, 0, 0)
                            
                            MDSeparator:
                            
                            MDList:
                                id: current_cal_list

                MDFloatingActionButtonSpeedDial:
                    data: app.add_btn_data
                    rotation_root_button: True
                    hint_animation: True
                    bg_hint_color: app.theme_cls.primary_light
                    icon: "plus"
                    callback: app.callback
            
            Screen:
                name: "daily entries scr"
                
                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    size_hint: (1,1)
                
                    MDToolbar:
                        id: daily_toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Daily Entries"
                        left_action_items: 
                            [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    ScrollView:
                    
                        GridLayout:
                            padding: dp(10)
                            spacing: dp(15)
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                            halign: "center"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Daily goal"
                                font_style: "H6"
                                
                            MDSeparator:
                            
                            AnchorLayout:
                                size_hint_y: None
                                height: 100
                                
                                
                                MDLabel:
                                    id: lbl_daily_goal
                                    halign: "center"
                                    font_style: "H3"
                                    text: "2500"
                                    
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Entries"
                                font_style: "H6"
                                margin: (0, 10, 0, 0)
                            
                            MDSeparator:
                            
                            MDList:
                                id: daily_cal_list
            
            Screen:
                name: "img scan scr"
                
                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    size_hint: (1,1)
                
                    MDToolbar:
                        id: daily_toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Image Scan"
                        left_action_items: 
                            [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    ScrollView:
                    
                        GridLayout:
                            padding: dp(10)
                            spacing: dp(15)
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                            halign: "center"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Image"
                                font_style: "H6"
                                
                            SmartTile:
                                id: img_tile
                                size_hint_y: None
                                height: "500dp"
                                source: "apple-black-and-white-hi.png"
                            
                            MDLabel:
                                theme_text_color: "Secondary"
                                text: "Results"
                                font_style: "H6"
                                margin: (0, 10, 0, 0)
                            
                            MDSeparator:
                            
                            MDList:
                                id: img_scan_res
                            
                            MDTextField:
                                id: grams
                                hint_text: "Grams"
                                mode: "rectangle"
                                
                            MDRoundFlatButton:
                                text: "Recipes" 
                                text_color: app.theme_cls.primary_color
                                on_release: app.scan_recipe()
                            
                            MDRoundFlatButton:
                                text: "Add entry"
                                text_color: app.theme_cls.primary_color
                                on_release: app.scan_add()
                            

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class RecipeCard(MDCard):
    text = StringProperty()


class MDListSpacing(MDList):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class NavigationDrawerScreen(Screen):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class DialogBoxContent(BoxLayout):
    name_text = StringProperty()
    calories_text = StringProperty()


class GoalDialogBoxContent(BoxLayout):
    goal_text = StringProperty()


class MainApp(MDApp):
    food_name = ""
    calories = ""
    goal = ""
    dialog = None

    calorie_dict = {
        "Cauliflower": "",
        "Strawberry": "",
    }
    current_prediction = ""

    food_item_list = []
    day_item_list = [] # list of Cards
    res_item_list = [] # list of results from image scan

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def file_manager_open(self):
        path = "/Users/neelj/PycharmProjects/cac2020/classifier"
        self.file_manager.show(path)
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)
        self.screen.ids.screen_manager.current = "img scan scr"
        self.screen.ids.img_tile.source = path

        res = predict_using_model(path)
        self.current_prediction = res
        item = OneLineListItem(text=res, on_press=self.open_nutr)
        self.screen.ids.img_scan_res.add_widget(item)

    def open_nutr(self, instance):
        if self.current_prediction == "Cauliflower":
            webbrowser.open("https://nutritiondata.self.com/facts/fruits-and-fruit-juices/2064/2")
        else:
            webbrowser.open("https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2390/2")

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        return self.screen

    add_btn_data = {
        "food-apple": "Add food item",
        "calendar": "Add day to list",
    }

    def on_swipe_complete(self, instance):
        try:
            self.screen.ids.current_cal_list.remove_widget(instance)
            self.food_item_list.remove(instance)
        except ValueError:
            try:
                self.screen.ids.daily_cal_list.remove_widget(instance)
                self.day_item_list.remove(instance)
            except ValueError:
                pass

        self.update_calories()

    def callback(self, instance):
        if instance.icon == "food-apple":
            self.dialog = MDDialog(
                title="Enter item:",
                type="custom",
                content_cls=DialogBoxContent(),
                size_hint=(.75, .3),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color,
                        on_press=self.close_dialog_box,
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color,
                        on_press=self.add_food_item,
                    ),
                ],
            )
            self.dialog.auto_dismiss = False
            self.dialog.open()

        elif instance.icon == "calendar":
            date_dialog = MDDatePicker(callback=self.get_date)
            date_dialog.open()

    def get_date(self, date):
        self.screen.ids.screen_manager.current = "daily entries scr"
        item_str = str(date) + " [" + self.screen.ids.lbl_calorie_total.text + "]"
        if int(self.screen.ids.lbl_calorie_total.text) > int(self.screen.ids.lbl_daily_goal.text):
            item_str = "[color=#ad3300]"+item_str+"[/color]"
        else:
            item_str = "[color=#00ad08]"+item_str+"[/color]"
        item = SwipeToDeleteItem(text=item_str)
        self.screen.ids.daily_cal_list.add_widget(
            item
        )
        self.day_item_list.append(item)
        self.screen.ids.lbl_calorie_total.text = "0"
        self.screen.ids.current_cal_list.clear_widgets()
        self.food_item_list.clear()

    def scan_recipe(self):
        self.screen.ids.screen_manager.current = "recipes scr"
        self.screen.ids.ingredient_list.text = self.current_prediction

    def scan_add(self):
        cals = int(int(self.screen.ids.grams.text)*0.33)
        cals_str = str(cals)
        self.screen.ids.screen_manager.current = "current entries scr"
        item_str = self.current_prediction + " [" + cals_str + "]"
        item = SwipeToDeleteItem(text=item_str)
        self.screen.ids.current_cal_list.add_widget(
            item
        )
        self.food_item_list.append(item)
        self.update_calories()

    def add_food_item(self, instance):
        item_str = self.food_name + " [" + self.calories + "]"
        item = SwipeToDeleteItem(text=item_str)
        self.screen.ids.current_cal_list.add_widget(
            item
        )
        self.food_item_list.append(item)
        self.update_calories()
        self.dialog.auto_dismiss = True
        self.dialog.dismiss()

    def close_dialog_box(self, instance):
        self.dialog.auto_dismiss = True
        self.dialog.dismiss()

    def update_calories(self):
        total = 0
        for item in self.food_item_list:
            calorie_str = item.text.split("[")[1].replace("]", "")
            total += int(calorie_str)
        self.screen.ids.lbl_calorie_total.text = str(total)


    def goal_dialog(self):
        self.dialog = MDDialog(
            title="Update Goal:",
            type="custom",
            content_cls=GoalDialogBoxContent(),
            size_hint=(.75, .3),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color,
                    on_press=self.close_dialog_box,
                ),
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color,
                    on_press=self.update_goal,
                ),
            ],
        )
        self.dialog.auto_dismiss = False
        self.dialog.open()

    def update_goal(self):
        self.screen.ids.lbl_daily_goal.text = self.goal

    def recipe_btn_color(self):
        self.screen.ids.recipe_btn.text_color = self.theme_cls.primary_color




if __name__ == "__main__":
    MainApp().run()

"""
AnchorLayout:
                                size_hint_y: None
                                height: card.height
                                
                                MDCard:
                                    id: card
                                    orientation: "vertical"
                                    size_hint: None, None
                                    size: "175dp", "75dp"
                                    pos_hint: {"center_x": .5}
                                
"""