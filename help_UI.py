import sys
import os

basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.join(basedir, 'Dependencies'))
os.chdir(os.path.join(basedir, 'Dependencies'))

from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

from PyQt5.QtWidgets import QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem,QColor,QFont
import cv2

import help_texts

ui, _ = loadUiType("UI/help.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class help(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, lang='en'):
        super(help, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        title = "SENSE-Help"
        self.setWindowTitle(title)

        self.activate_()
        self.font_size=self.spinBox_font.value()
        self.set_language(lang)
        self.win_set_geometry()
        self.center()
        self._old_pos = None
        self.statusBar().setMaximumHeight(5)
        self.statusBar().setStyleSheet('background-color:rgb(85, 0, 0);')
        
        self.spinBox_font.valueChanged.connect(self.set_font)
        self.lang_comboBox.currentTextChanged.connect(self.set_language)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        if not self.isMaximized():
            self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self, left=50, top=300, width=350, height=20):
        height=350
        width=550
        top=10
        left=10
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def set_font(self):
        self.font_size=self.spinBox_font.value()
        style='font-size: {}pt;background-color: rgb(220, 220,220);border-color: rgb(188, 188, 188);'.format(self.font_size)
        # style.relace(''','"')
        self.centralwidget.setStyleSheet(style)
        self.set_tree_view()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        ##print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)
        
    def set_text(self, text):
        self.textEdit.clear()
        self.textEdit.setText(text)
    
    def set_language(self, lang):
        if lang=='fa' or lang==help_texts.Titles['persian']['fa'] or lang==help_texts.Titles['persian']['en']:
            self.language = 'fa'
        else:
             self.language = 'en'
        self.set_tree_view()
        help_texts.set_help_title(self, self.language)
        self.label.clear()
        self.textEdit.clear()

    def set_tree_view(self):
        self.treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()


        # train_software
        train_software = StandardItem(help_texts.Titles['Train Software'][self.language], self.font_size+2, set_bold=True)

        # ---------------------------Data Aquization-------------------------------
        Data_Aquization = StandardItem(help_texts.Titles['Data Auquzation'][self.language], self.font_size+1)
        train_software.appendRow(Data_Aquization)
        Live_tab = StandardItem(help_texts.Titles['Live'][self.language], self.font_size, color=QColor(155, 0, 0))
        Technical_view_tab = StandardItem(help_texts.Titles['Technical View'][self.language], self.font_size, color=QColor(155, 0, 0))
        Data_Aquization.appendRow(Live_tab)
        Data_Aquization.appendRow(Technical_view_tab)

        # ---------------------------Label-------------------------------
        Label = StandardItem(help_texts.Titles['Label'][self.language], self.font_size+1)
        train_software.appendRow(Label)
        austin = StandardItem(help_texts.Titles['Label'][self.language], self.font_size, color=QColor(155, 0, 0))
        Label.appendRow(austin)
        # ---------------------------Tuning-------------------------------
        tuning = StandardItem(help_texts.Titles[' Tuning'][self.language], self.font_size+1)
        train_software.appendRow(tuning)
        binary = StandardItem(help_texts.Titles['Binary'][self.language], self.font_size)
        tuning.appendRow(binary)

        localization = StandardItem(help_texts.Titles['Localization'][self.language], self.font_size)
        tuning.appendRow(localization)

        classification = StandardItem(help_texts.Titles['Classification'][self.language], self.font_size)
        tuning.appendRow(classification)

        yolo = StandardItem(help_texts.Titles['Yolo2'][self.language], self.font_size)
        tuning.appendRow(yolo)

        b_list = StandardItem(help_texts.Titles['binary_list'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_list)
        b_training = StandardItem(help_texts.Titles['binary_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_training)
        b_history = StandardItem(help_texts.Titles['binary_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        binary.appendRow(b_history)

        l_training = StandardItem(help_texts.Titles['localization_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        localization.appendRow(l_training)

        l_history = StandardItem(help_texts.Titles['localization_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        localization.appendRow(l_history)

        c_list = StandardItem(help_texts.Titles['classes_list'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        classification.appendRow(c_list)
 
        # c_training = StandardItem(help_texts.Titles['classification_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        # classification.appendRow(c_training)

        # c_history = StandardItem(help_texts.Titles['classification_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        # classification.appendRow(c_history)

        y_training = StandardItem(help_texts.Titles['yolo_training'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        yolo.appendRow(y_training)

        y_history = StandardItem(help_texts.Titles['yolo_history'][self.language], self.font_size-1, color=QColor(185, 0, 0))
        yolo.appendRow(y_history)

        # ---------------------------Pipline Build Test-------------------------------
        pipline_m = StandardItem(help_texts.Titles['Pipline Build & Test'][self.language], self.font_size+1)
        train_software.appendRow(pipline_m)

        Pipline = StandardItem(help_texts.Titles['Pipline'][self.language], self.font_size, color=QColor(155, 0, 0))
        pipline_m.appendRow(Pipline)

        load_dataset = StandardItem(help_texts.Titles['Load Dataset'][self.language], self.font_size, color=QColor(155, 0, 0))
        pipline_m.appendRow(load_dataset)

        History = StandardItem(help_texts.Titles['history'][self.language], self.font_size, color=QColor(185, 0, 0))
        pipline_m.appendRow(History)


        # ---------------------------User Page-------------------------------
        user_profile = StandardItem(help_texts.Titles['User Profile'][self.language], self.font_size+1)
        train_software.appendRow(user_profile)

        create_data = StandardItem(help_texts.Titles['create_new_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(create_data)
        all_dataset = StandardItem(help_texts.Titles['all_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(all_dataset)
        my_data = StandardItem(help_texts.Titles['my_ds'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(my_data)
        my_pipline = StandardItem(help_texts.Titles['pipelines'][self.language], self.font_size, color=QColor(155, 0, 0))
        user_profile.appendRow(my_pipline)

        # ---------------------------Settings Page-------------------------------
        settings = StandardItem(help_texts.Titles['settings'][self.language], self.font_size+1)
        train_software.appendRow(settings)
        austin = StandardItem(help_texts.Titles['settings'][self.language], self.font_size, color=QColor(155, 0, 0))
        settings.appendRow(austin)

        # ---------------------------LoadSheet Page-------------------------------
        load_sheet = StandardItem(help_texts.Titles['load_sheet'][self.language], self.font_size+1)
        train_software.appendRow(load_sheet)
        austin = StandardItem(help_texts.Titles['load_sheet'][self.language], self.font_size, color=QColor(155, 0, 0))
        load_sheet.appendRow(austin)

        # ---------------------------Image Enlargement Page-------------------------------
        image_enlargement = StandardItem(help_texts.Titles['image_enlargement'][self.language], self.font_size+1)
        train_software.appendRow(image_enlargement)
        austin = StandardItem(help_texts.Titles['image_enlargement'][self.language], self.font_size, color=QColor(155, 0, 0))
        image_enlargement.appendRow(austin)

        # ---------------------------Show Logs Page-------------------------------
        show_logs = StandardItem(help_texts.Titles['show_logs'][self.language], self.font_size+1)
        train_software.appendRow(show_logs)
        austin = StandardItem(help_texts.Titles['show_logs'][self.language], self.font_size, color=QColor(155, 0, 0))
        show_logs.appendRow(austin)

        # settings_page = StandardItem(help_texts.Titles['settings_page'][self.language], self.font_size, color=QColor(155, 0, 0))
        # settings.appendRow(settings_page)

        # # setting_software 
        # setting_software = StandardItem(help_texts.Titles['Setting Software'][self.language], self.font_size+2, set_bold=True)

        # Dashboard = StandardItem(help_texts.Titles['page_dashboard'][self.language], self.font_size+1)
        # Camera = StandardItem(help_texts.Titles['page_camera'][self.language], self.font_size+1)
        # PLC = StandardItem(help_texts.Titles['page_plc'][self.language], self.font_size+1)
        # Level2 = StandardItem(help_texts.Titles['page_level2'][self.language], self.font_size+1)
        # Defection = StandardItem(help_texts.Titles['page_defection'][self.language], self.font_size+1)
        # Calibration = StandardItem(help_texts.Titles['page_calibration'][self.language], self.font_size+1)
        # Setting = StandardItem(help_texts.Titles['page_settings'][self.language], self.font_size+1)
        # Storage = StandardItem(help_texts.Titles['page_storage'][self.language], self.font_size+1)
        # User = StandardItem(help_texts.Titles['page_users'][self.language], self.font_size+1)

        # PLC = StandardItem('PLC', self.font_size+1)
        # PLC = StandardItem('Storage', self.font_size+1)
        # Level2 = StandardItem('Level2', self.font_size+1)
        # Defection = StandardItem('Defection', self.font_size+1)
        # Calibration = StandardItem('Calibration', self.font_size+1)
        # PLC = StandardItem('User', self.font_size+1)
        # Setting = StandardItem('Setting', self.font_size+1)
        # setting_software.appendRows([Dashboard, Camera, PLC,Calibration,Level2,Defection,Storage,User,Setting])

        # ------------------------------------------ Operator Software ----------------------------------------------
        operator_software = StandardItem(help_texts.Titles['Operator Software'][self.language], self.font_size+2, set_bold=True)

        # ---------------------------Settings Page-------------------------------
        operator_settings = StandardItem(help_texts.Titles['settings_and_info'][self.language], self.font_size+1)
        operator_software.appendRow(operator_settings)
        austin = StandardItem(help_texts.Titles['settings_and_info'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_settings.appendRow(austin)

        # ---------------------------Model Settings Page-------------------------------
        operator_model_settings = StandardItem(help_texts.Titles['model_settings'][self.language], self.font_size+1)
        operator_software.appendRow(operator_model_settings)
        austin = StandardItem(help_texts.Titles['model_settings'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_model_settings.appendRow(austin)

        # ---------------------------Detection Page-------------------------------
        operator_detection = StandardItem(help_texts.Titles['detection'][self.language], self.font_size+1)
        operator_software.appendRow(operator_detection)
        austin = StandardItem(help_texts.Titles['detection'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_detection.appendRow(austin)

        # ---------------------------Live Page-------------------------------
        operator_live = StandardItem(help_texts.Titles['live'][self.language], self.font_size+1)
        operator_software.appendRow(operator_live)
        austin = StandardItem(help_texts.Titles['live'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_live.appendRow(austin)

        # ---------------------------Online Report Page-------------------------------
        operator_online_report = StandardItem(help_texts.Titles['online_report'][self.language], self.font_size+1)
        operator_software.appendRow(operator_online_report)
        austin = StandardItem(help_texts.Titles['online_report_technical'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_online_report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['online_report_binary'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_online_report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['online_report_classification'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_online_report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['online_report_width'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_online_report.appendRow(austin)

        # ---------------------------Offline Report Page-------------------------------
        operator_offline_report = StandardItem(help_texts.Titles['offline_report'][self.language], self.font_size+1)
        operator_software.appendRow(operator_offline_report)
        search = StandardItem(help_texts.Titles['offline_report_search'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_offline_report.appendRow(search)
        report = StandardItem(help_texts.Titles['offline_report_report'][self.language], self.font_size, color=QColor(155, 0, 0))
        operator_offline_report.appendRow(report)

        austin = StandardItem(help_texts.Titles['offline_report_technical'][self.language], self.font_size, color=QColor(155, 0, 0))
        report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['offline_report_defect_slider'][self.language], self.font_size, color=QColor(155, 0, 0))
        report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['offline_report_binary'][self.language], self.font_size, color=QColor(155, 0, 0))
        report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['offline_report_classification'][self.language], self.font_size, color=QColor(155, 0, 0))
        report.appendRow(austin)
        austin = StandardItem(help_texts.Titles['offline_report_width'][self.language], self.font_size, color=QColor(155, 0, 0))
        report.appendRow(austin)

        rootNode.appendRow(train_software)
        rootNode.appendRow(operator_software)

        self.treeView.setModel(treeModel)
        self.treeView.expandAll()
        self.treeView.doubleClicked.connect(self.getValue)

    def getValue(self, val):
        self.set_help(val.data())

    def set_help(self, name):
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Train Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

        help_image = None
        text = ''
        if name==help_texts.Titles['Live'][self.language]:
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['LIVE_PAGE'][self.language])
            text = help_texts.HELPS['LIVE_PAGE'][self.language]
        elif name==help_texts.Titles['Technical View'][self.language]:
            text = help_texts.HELPS['TECHNICAL_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['TECHNICAL_PAGE'][self.language])
        elif name==help_texts.Titles['Label'][self.language]:
            text = help_texts.HELPS['LABEL_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['LABEL_PAGE'][self.language])
        # elif name=='page_user_profile':
        #     stack_name = self.stackedWidget_2.currentWidget().objectName()
        elif name==help_texts.Titles['create_new_ds'][self.language] :
            text = help_texts.HELPS['PROFILE_CREATEDS_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['PROFILE_CREATEDS_PAGE'][self.language])
        elif name==help_texts.Titles['all_ds'][self.language] :
            text = help_texts.HELPS['PROFILE_ALLDS_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['PROFILE_ALLDS_PAGE'][self.language])
        elif name==help_texts.Titles['my_ds'][self.language]:
            text = help_texts.HELPS['PROFILE_MYDS_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['PROFILE_MYDS_PAGE'][self.language])
        elif name==help_texts.Titles['pipelines'][self.language]:
            text = help_texts.HELPS['PROFILE_MYPIP_PAGE'][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS['PROFILE_MYPIP_PAGE'][self.language])
        elif name==help_texts.Titles['Pipline'][self.language]:
            text = help_texts.HELPS["PBT_PIPLINE_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["PBT_PIPLINE_PAGE"][self.language])
        elif name==help_texts.Titles['Load Dataset'][self.language]:
            text = help_texts.HELPS["PBT_LOADDATASET_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["PBT_LOADDATASET_PAGE"][self.language])
        elif name==help_texts.Titles['History'][self.language]:
            text = help_texts.HELPS["PBT_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["PBT_HISTORY_PAGE"][self.language])
        elif name== help_texts.Titles['binary_list'][self.language]:
            text = help_texts.HELPS["BINARYLIST_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["BINARYLIST_PAGE"][self.language])
        elif name== help_texts.Titles['binary_training'][self.language]:
            text = help_texts.HELPS["BINARY_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["BINARY_TRAINING_PAGE"][self.language])
        elif name== help_texts.Titles["binary_history"][self.language]:
            text = help_texts.HELPS["BINARY_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["BINARY_HISTORY_PAGE"][self.language])
        elif name== help_texts.Titles['localization_training'][self.language]:
            text = help_texts.HELPS["LOC_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["LOC_TRAINING_PAGE"][self.language])
        elif name== help_texts.Titles['localization_history'][self.language]:
            text = help_texts.HELPS["LOC_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["LOC_HISTORY_PAGE"][self.language])
        elif name== help_texts.Titles['yolo_training'][self.language]:
            text = help_texts.HELPS["YOLO_TRAINING_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["YOLO_TRAINING_PAGE"][self.language])
        elif name== help_texts.Titles['yolo_history'][self.language]:
            text = help_texts.HELPS["YOLO_HISTORY_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["YOLO_HISTORY_PAGE"][self.language])
        elif name== help_texts.Titles['classes_list'][self.language]:
            text = help_texts.HELPS["CLASSLIST_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["CLASSLIST_PAGE"][self.language])
        # elif name=='page_Classification':
        #     stack_name = self.stackedWidget_classification.currentWidget().objectName()
        # if stack_name == 'page_classification_class_list':
        #         pass
        # elif stack_name == 'page_classification_training':
        #         pass
        # elif stack_name == 'page_classification_history':
        #         pass
        elif name== help_texts.Titles['settings'][self.language]:
            text = help_texts.HELPS["SETTINGS_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["SETTINGS_PAGE"][self.language])
        elif name== help_texts.Titles['load_sheet'][self.language]:
            text = help_texts.HELPS["LOADSHEET_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["LOADSHEET_PAGE"][self.language])
        elif name== help_texts.Titles['image_enlargement'][self.language]:
            text = help_texts.HELPS["IMAGEENLARGEMENT_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["IMAGEENLARGEMENT_PAGE"][self.language])
        elif name== help_texts.Titles['show_logs'][self.language]:
            text = help_texts.HELPS["SHOWLOGS_PAGE"][self.language]
            help_image = cv2.imread(help_texts.HELPS_ADDRESS["SHOWLOGS_PAGE"][self.language])

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Operator Help--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

        elif name== help_texts.Titles['settings_and_info'][self.language]:
             text = help_texts.HELPS['page_settings_and_info'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_settings_and_info"][self.language])

        elif name== help_texts.Titles['model_settings'][self.language]:
             text = help_texts.HELPS['page_model_settings'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_model_settings"][self.language])

        elif name== help_texts.Titles['detection'][self.language]:
             text = help_texts.HELPS['page_detection'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_detection"][self.language])

        elif name== help_texts.Titles['live'][self.language]:
             text = help_texts.HELPS['page_live'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_live"][self.language])

        elif name== help_texts.Titles['online_report_technical'][self.language]:
             text = help_texts.HELPS['page_online_report_technical'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_online_report_technical"][self.language])

        elif name== help_texts.Titles['online_report_binary'][self.language]:
             text = help_texts.HELPS['page_online_report_binary'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_online_report_binary"][self.language])

        elif name== help_texts.Titles['online_report_classification'][self.language]:
             text = help_texts.HELPS['page_online_report_classification'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_online_report_classification"][self.language])

        elif name== help_texts.Titles['online_report_width'][self.language]:
             text = help_texts.HELPS['page_online_report_width'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_online_report_width"][self.language])

        elif name== help_texts.Titles['offline_report_search'][self.language]:
             text = help_texts.HELPS['page_offline_report_search'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_search"][self.language])

        elif name== help_texts.Titles['offline_report_technical'][self.language]:
             text = help_texts.HELPS['page_offline_report_technical'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_technical"][self.language])

        elif name== help_texts.Titles['offline_report_defect_slider'][self.language]:
             text = help_texts.HELPS['page_offline_report_defect_slider'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_defect_slider"][self.language])

        elif name== help_texts.Titles['offline_report_binary'][self.language]:
             text = help_texts.HELPS['page_offline_report_binary'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_binary"][self.language])

        elif name== help_texts.Titles['offline_report_classification'][self.language]:
             text = help_texts.HELPS['page_offline_report_classification'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_classification"][self.language])

        elif name== help_texts.Titles['offline_report_width'][self.language]:
             text = help_texts.HELPS['page_offline_report_width'][self.language]
             help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_offline_report_width"][self.language])


#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

        if name == help_texts.Titles['page_dashboard'][self.language]:
                text = help_texts.HELPS["page_dashboard"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_dashboard"][self.language])

        if name == help_texts.Titles['page_camera'][self.language]:
                text = help_texts.HELPS["page_camera"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_camera"][self.language])

        if name == help_texts.Titles['page_defection'][self.language]:
                text = help_texts.HELPS["page_defection"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_defection"][self.language])

        if name == help_texts.Titles['page_level2'][self.language]:
                text = help_texts.HELPS["page_level2"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_level2"][self.language])

        if name == help_texts.Titles['page_calibration'][self.language]:
                text = help_texts.HELPS["page_calibration"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_calibration"][self.language])

        if name == help_texts.Titles['page_settings'][self.language]:
                text = help_texts.HELPS["page_settings"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_settings"][self.language])

        if name == help_texts.Titles['page_users'][self.language]:
                text = help_texts.HELPS["page_users"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_users"][self.language])

        if name == help_texts.Titles['page_storage'][self.language]:
                text = help_texts.HELPS["page_storage"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_storage"][self.language])
       
        if name == help_texts.Titles['page_plc'][self.language]:
                text = help_texts.HELPS["page_plc"][self.language]
                help_image = cv2.imread(help_texts.HELPS_ADDRESS["page_plc"][self.language])
        self.set_help_image(help_image, text)

    def set_help_image(self, help_image, text):
        if help_image is not None:
            self.textEdit.setText(text)
            image = QImage(help_image, help_image.shape[1], help_image.shape[0], help_image.strides[0],
                    QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(image))


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon('images/icons/icon_help.png'))
    win = help(lang='en')
    if len(sys.argv) > 1:
         win.set_language(sys.argv[1])
         if len(sys.argv) > 2 and sys.argv[2]:
              win.set_help(sys.argv[2])
    win.show()
    win.win_set_geometry(width=300, height=900)
    sys.exit(app.exec())
