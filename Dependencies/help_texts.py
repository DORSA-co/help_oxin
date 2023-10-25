from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout

Titles = {

        'persian': {'fa': "فارسی",
                        'en': 'Persian'},

        'english': {'fa': "انگلیسی",
                        'en': 'English'},

        'font': {'fa': "فونت",
                        'en': 'Font'},

        'language': {'fa': "زبان",
                        'en': 'Language'},

        'Train Software': {'fa': "نرم افزار آموزشی",
                                'en': 'Train Software'},

        'Operator Software': {'fa': "نرم افزار اپراتور",
                                'en': 'Operator Software'},

        'Setting Software': {'fa': "نرم افزار تنظیمات",
                                'en': 'Setting Software'},

        'Data Auquzation': {'fa': "داده برداری",
                                'en': 'Data Auquzation'},

        'Label': {'fa': "برچسب گذاری",
                'en': 'Label'},

        ' Tuning': {'fa': "تیونینگ",
                        'en': ' Tuning'},

        'Pipline Build & Test': {'fa': "ساخت پایپ لاین و تست",
                                'en': 'Pipline Build and Test'},

        'show_logs': {'fa': "نمایش لاگ‌ها",
                        'en': 'Show Logs'},

        'Live': {'fa': 'نمایش زنده',
                'en': 'Live'},

        'Technical View': {'fa': 'نمای تکنیکال',
                        'en': 'Technical View'},

        'create_new_ds': {'fa': 'ایجاد مجموعه داده ی جدید',
                        'en': 'Create New Dataset'},

        'all_ds': {'fa': 'همه ی مجموعه داده ها',
                'en': 'All Datasets'},

        'my_ds': {'fa': 'مجموعه داده های من',
                'en': 'My Datasets'},

        'pipelines': {'fa': 'پایپ لاین ها',
                        'en': 'Pipelines'},

        'binary_list': {'fa': 'لیست باینری',
                        'en': 'Binary list'},

        'Binary': {'fa': 'باینری',
                        'en': 'Binary'},

        'Localization': {'fa': 'جایابی',
                        'en': 'Localization'},

        'Classification': {'fa': 'دسته بندی',
                        'en': 'Classification'},

        'Yolo2': {'fa': 'جایابی + دسته بندی',
                'en': 'Localization + Classification'},

        'training': {'fa': 'آموزش',
                        'en': 'Training'},

        'binary_training': {'fa': 'آموزش باینری',
                                'en': 'Binary Training'},

        'localization_training': {'fa': 'آموزش جایابی',
                                        'en': 'Localization Training'},

        'classification_training': {'fa': 'آموزش دسته‌بندی',
                                        'en': 'Classification Training'},

        'yolo_training': {'fa': 'آموزش جایابی و دسته‌بندی',
                                'en': 'Localization and Classification Training'},

        'history': {'fa': 'تاریخچه',
                        'en': 'History'},

        'binary_history': {'fa': 'تاریخچه باینری',
                                'en': 'Binary History'},

        'localization_history': {'fa': 'تاریخچه جایابی',
                                        'en': 'Localization History'},

        'classification_history': {'fa': 'تاریخچه دسته‌بندی',
                                        'en': 'Classification History'},

        'yolo_history': {'fa': 'تاریخچه جایابی و دسته‌بندی',
                                'en': 'Localization and Classification History'},

        'classes_list': {'fa': 'لیست کلاس ها',
                        'en': 'Classes list'},

        'Pipline': {'fa': 'پایپ لاین',
                                'en': 'Pipline'},
        'Load Dataset': {'fa': 'بارگذاری داده',
                                'en': 'Load Dataset'},
        'History':{'fa':'تاریخچه',
                        'en':'History'},

        'User Profile': {'fa': 'صفحه کاربر',
                                'en': 'User Profile'},

        'settings': {'fa': 'تنظیمات',
                        'en': 'Settings'},

        'load_sheet': {'fa': 'بارگذاری ورق',
                        'en': 'Load Sheet'},

        'image_enlargement': {'fa': 'بزرگنمایی تصویر',
                        'en': 'Image Enlargement'},

        'settings_page': {'fa': 'صفحه‌ی تنظیمات',
                        'en': 'Settings page'},

        'settings_and_info': {'fa': 'تنظیمات و اطلاعات',
                        'en': 'Settings and Information'},

        'detection': {'fa': 'تشخیص',
                        'en': 'Detection'},

        'model_settings': {'fa': 'تنظیمات مدل‌ها',
                        'en': 'Model Settings'},

        'live': {'fa': 'نمایش زنده‌ی دوربین‌ها',
                        'en': 'Cameras Live'},

        'offline_report': {'fa': 'گزارش‌گیری آفلاین',
                        'en': 'Offline Report'},

        'offline_report_search': {'fa': 'جست و جو',
                'en': 'Search'},
        
        'offline_report_report': {'fa': 'گزارش‌گیری',
                'en': 'Report'},

        'offline_report_technical': {'fa': 'گزارش‌ آفلاین نمای فنی',
                        'en': 'Technical View offline Report'},

        'offline_report_defect_slider': {'fa': 'گزارش‌ آفلاین عیوب',
                        'en': 'Defects Offline Report'},

        'offline_report_binary': {'fa': 'گزارش‌‌ آفلاین باینری',
                        'en': 'Binary Offline Report'},

        'offline_report_classification': {'fa': 'گزارش‌ آفلاین دسته‌بندی',
                        'en': 'Classification Online Report'},

        'offline_report_width': {'fa': 'گزارش‌ آفلاین عرض‌سنج',
                        'en': 'Width Offline Report'},

        'online_report': {'fa': 'گزارش‌گیری آنلاین',
                        'en': 'Online Report'},

        'online_report_technical': {'fa': 'گزارش‌ آنلاین نمای فنی',
                        'en': 'Technical View Online Report'},

        'online_report_binary': {'fa': 'گزارش‌‌ آنلاین باینری',
                        'en': 'Binary Online Report'},

        'online_report_classification': {'fa': 'گزارش‌ آنلاین دسته‌بندی',
                        'en': 'Classification Online Report'},

        'online_report_width': {'fa': 'گزارش‌ آنلاین عرض‌سنج',
                        'en': 'Width Online Report'},


#---------------------------------------------------------------------
#----------------------Setting Sofwtare-------------------------------
#---------------------------------------------------------------------

        'page_dashboard': {'fa': 'صفحه داشبورد',
                                'en': 'Dashboard'},  
        'page_camera': {'fa': 'صفحه دوربین',
                                'en': 'Camera'},  
        'page_defection': {'fa': 'صفحه عیوب',
                                'en': 'Defection'},  
        'page_level2': {'fa': 'صفحه ارتباطات',
                                'en': 'Level2'},  
        'page_calibration': {'fa': 'صفحه کالیبراسیون',
                                'en': 'Calibration'},  
        'page_settings': {'fa': 'صفحه تنظیمات',
                                'en': 'Setting'},  
        'page_users': {'fa': 'صفحه مدیریت کاربران',
                                'en': 'Users'},  
        'page_plc': {'fa': 'صفحه پی ال سی',
                                'en': 'PLC'},                        
        'page_storage': {'fa': 'صفحه حافظه',
                                'en': 'Storage'},                        
        'show_labels': {'fa': 'نمایش برچسب‌ها',
                                'en': 'Show Labels'},                       
}

HELPS = {
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Trainig Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    'SETTINGS_PAGE': {'fa': 'صفحه‌ی تنظیمات \n این صفحه مربوط به تنظیمات نرم افزار از جمله تنظیمات ظاهری، تنظیمات پی ال سی و تنظیمات تصویربرداری است.',
                'en': 'Settings Page \n This page is related to software settings including appearance settings, PLC settings and cameras settings.'},

    'LIVE_PAGE': {'fa': 'صفحه ی نمایش زنده \n این صفحه مربوط به مدیریت اتصال دوربین ها و ذخیره سازی و نمایش زنده ی تصاویر گرفته شده توسط آن هاست.',
                'en': 'Live Page \n This page is related to the management of the connection of cameras and the storage and live display of the images taken by them.'},
    'TECHNICAL_PAGE': {'fa': 'صفحه ی نمای فنی \n این صفحه مربوط به بارگذاری ورق و مشاهده ی تصاویر مربوط به آن و همچنین انتخاب تصاویر برای برچسب زدن است.',
                'en': 'Thechnical View Page \n This page is about loading the sheet and viewing related images as well as selecting images for labeling.'},
    'LABEL_PAGE': {'fa': 'صفحه ی برچسب زدن \n این صفحه مربوط به برچسب زدن تصاویر ورق ها است.',
                'en': 'Label Page \n This page is about labeling sheet images.'},
    'PROFILE_CREATEDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_ALLDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_MYDS_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'PROFILE_MYPIP_PAGE': {'fa': 'صفحه ی پروفایل کاربر \n این صفحه مربوط به اطلاعات کاربر و مجموعه داده ها است.',
                            'en': 'User Profile Page \n This page is about user information and datasets.'},
    'BINARY_TRAINING_PAGE': {'fa': 'صفحه ی آموزش باینری \n این صفحه مربوط به آموزش مدل‌های باینری است.',
                            'en': 'Binary Training Page \n This page is about training binary models.'},
    'BINARY_HISTORY_PAGE': {'fa': 'صفحه ی تاریخچه ی آموزش باینری \n این صفحه مربوط به تاریخچه ی آموزش مدل‌های باینری است.',
                            'en': 'Binary History Page \n This page is about history of training binary models.'},
    'BINARYLIST_PAGE': {'fa': 'صفحه ی لیست باینری \n این صفحه مربوط به مشاهده ی جزئیات مجموعه داده های باینری موجود است.',
                            'en': 'Binary List Page \n This page is about viewing the details of the available binary datasets.'},
    'LOC_TRAINING_PAGE': {'fa': 'صفحه ی آموزش جایابی \n این صفحه مربوط به آموزش مدل‌های جایابی است.',
                            'en': 'Localization Training Page \n This page is about training localization models.'},
    'LOC_HISTORY_PAGE': {'fa': 'صفحه ی تاریخچه ی آموزش جایابی \n این صفحه مربوط به تاریخچه ی آموزش مدل‌های جایابی است.',
                            'en': 'Localization History Page \n This page is about history of training localization models.'},
    'CLASSLIST_PAGE': {'fa': 'صفحه ی لیست کلاس‌ها \n این صفحه مربوط به مشاهده ی جزئیات مجموعه داده های دسته‌بندی موجود است.',
                            'en': 'Classes List Page \n This page is about viewing the details of the available classification datasets.'},
    'YOLO_HISTORY_PAGE': {'fa': 'صفحه ی تاریخچه ی آموزش جایابی و دسته‌بندی \n این صفحه مربوط به تاریخچه ی آموزش مدل‌های جایابی و دسته‌بندی است.',
                            'en': 'Localization and Classification History Page \n This page is about history of training localization and classification models.'},
    'YOLO_TRAINING_PAGE': {'fa': 'صفحه ی آموزش جایابی و دسته‌بندی \n این صفحه مربوط به آموزش مدل‌های جایابی و دسته‌بندی است.',
                            'en': 'Localization and Classification Training Page \n This page is about training localization and classification models.'},

    'PBT_PIPLINE_PAGE':{'fa':'این صفحه برای ساخت پایپ لاین سفارشی شده است\nبه این صورت که با استفاده از سه لیست زیر ،مدل های از قبل آموزش دیده شده موجود در نرم افزار  را براساس معماری آنها فیلتر کرده\nو در جدول زیر لیست ها  عملکرد هر مدل  بر اساس معماری انتخاب شده نمایش داده میشود\nو از طریق جدول، مدل هر جز از پایپ لاین را انتخاب کرده \nو در پایان،در جای خالی زیر صفحه یک نام برای پایپ لاین انتخاب کرده و با زدن دکمه اعمال پایپ لاین راساخته.',
                        'en':'this page is for a customized pipline. \nIn such a way that: useing the following three list,fliter the pre-trained models in the software based on their architecture,\nthe performace of each model is shown in the table blow the lists, \nuseing the model table,select each part, \nfinaly choose a suitable name for pipeline in the empty space below and hit the apply buttom and build the pipline '},
    'PBT_LOADDATASET_PAGE' :{'fa':'این صفحه برای اعتبار سنجی پایپ لاین های موجود در نرم افزار بر روی مجموعه داده های موجود است.\n به این صورت که،ابتدا از قسمت بالا سمت چپ نرم افزار تنظیمات مربوط به بارگذاری مجموعه داده ها را انجام داده\n سپس با استفاده از لیست سمت راست،پایپ لاین مورد نظر را انتخاب کرده\n با فشردن دکمه اعتبار سنجی عملیات را انجام داده.',
                              'en':'This page is for validating pipelines in the software on existing data sets.\nIn this way, first of all, from the upper left part of the software, the settings related to loading the data set have been made\nThen, using the list on the right, select the desired pipeline\nBy pressing the evaluate button, the evaluating operation is done'},
    'PBT_HISTORY_PAGE':{'fa':' این صفحه برای مشاهده تاریخچه تمامی اعتبار سنجی های انجام شده در نرم افزار است،\nکه این تاریخچه با استفاده ابزار سمت چپ صفحه قابل فیلتر است.',
                        'en':'This page is for viewing the history of all evaluating , done in the software.\nThis history can be filtered using the tool on the left side of the page.'},

    'LOADSHEET_PAGE':{'fa': 'صفحه ی بارگذاری ورق \n این صفحه مربوط به بارگذاری ورق برای مشاهده‌ و برچسب‌زدن تصاویر آن است.',
                        'en': "Load Sheet Page \n This page is about loading the sheet for viewing and labeling it's images."},

    'IMAGEENLARGEMENT_PAGE':{'fa': 'صفحه ی بزرگنمایی تصویر \n این صفحه مربوط به بزرگنمایی و تمام صفحه کردن تصاویری است که در نرم‌افزار با اندازه‌ی کوچک نمایش داده شده‌اند و با دابل کلیک کردن روی تصاویر کوچک نمایان می‌شود.',
                                'en': 'Image Enlargement Page \n This page is about zooming and full-screen images that are displayed in the software with a small size and can be displayed by double-clicking on the small images.'},

    'SHOWLOGS_PAGE':{'fa': 'صفحه ی نمایش لاگ‌ها \n این صفحه مربوط به جست‌وجو و نمایش لاگ‌های ذخیره شده است.',
                                'en': 'Show Logs Page \n This page is about searching and displaying saved logs.'},

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Operator Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    "page_settings_and_info": {
        "fa": "صفحه‌ی تنظیمات \n این صفحه مربوط به تنظیمات نرم افزار از جمله تنظیمات دوربین‌ها، تنظیمات پی ال سی و ... و نمایش اطلاعاتی درمورد لول ۲ و دما است.",
        "en": "Settings Page \n This page is related to software settings, including camera settings, PLC settings, etc., and displaying information about Level2 and Temperature.",
    },

    'page_model_settings': {'fa': 'صفحه‌ی تنظیمات مدل‌ها \n این صفحه مربوط به تنظیمات مدل‌های تشخیص است.',
                'en': 'Model Settings Page \n This page is related to the settings of the detection models.'},

    "page_detection": {
        "fa": "صفحه‌ی تشخیص \n این صفحه مربوط به آغاز تصویر برداری و تشخیص نرم افزار و همچنین نمایش نتایج به صورت برخط است.",
        "en": "Detection Page \n This page is related to the start of imaging and software detection, as well as displaying the results online.",
    },

    "page_live": {
        "fa": "صفحه‌ی نمایش زنده \n این صفحه مربوط به نمایش زنده‌ی تصاویر دوربین‌ها است.",
        "en": "Live Page \n This page is related to the live display of camera images.",
    },

    "page_offline_report_search": {
        "fa": "صفحه‌ی تشخیص \n این صفحه مربوط به فیلتر کردن و جست و جو ی ورق‌ها برای گزارش‌گیری است.",
        "en": "Offline Report Search Page \n This page is related to filtering and searching sheets for reporting.",
    },

    'page_offline_report_technical': {'fa': 'صفحه‌ی نمای تکنیکال گزارش آفلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات مربوط به نمای تکنیکال ورق است.',
                    'en': 'Offline Report Technical Page \n This page is related to the technical view of the sheet.'},

    'page_offline_report_defect_slider': {'fa': 'صفحه‌ی نمایش عیوب گزارش آفلاین \n این صفحه مربوط به مشاهده‌ی تصاویر عیوب تشخیص داده شده در ورق است.',
                    'en': 'Offline Report Show Defects Page \n This page is related to viewing the images of defects detected in the sheet.'},

    'page_offline_report_binary': {'fa': 'صفحه‌ی باینری گزارش آفلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار عیوب تشخیص داده شده در ورق است.',
                    'en': 'Offline Report Binary Page \n This page is related to viewing the information and statistics of defects detected in the sheet.'},

    'page_offline_report_classification': {'fa': 'صفحه‌ی دسته‌بندی گزارش آفلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار دسته‌های عیب تشخیص داده شده در ورق است.',
                    'en': 'Offline Report Classification Page \n This page is related to viewing the information and statistics of the defect classes detected in the sheet.'},

    'page_offline_report_width': {'fa': 'صفحه‌ی عرض‌سنج گزارش آفلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار عرض ورق است.',
                    'en': 'Offline Report Width Page \n This page is related to viewing the information and statistics of the sheet width.'},

    'page_online_report_technical': {'fa': 'صفحه‌ی نمای تکنیکال گزارش آنلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات مربوط به نمای تکنیکال ورق به صورت برخط است.',
                    'en': 'Online Report Technical Page \n This page is related to the online technical view of the sheet.'},

    'page_online_report_binary': {'fa': 'صفحه‌ی باینری گزارش آنلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار عیوب تشخیص داده شده در ورق به صورت برخط است.',
                    'en': 'Online Report Binary Page \n This page is related to viewing the online information and statistics of defects detected in the sheet.'},

    'page_online_report_classification': {'fa': 'صفحه‌ی دسته‌بندی گزارش آنلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار دسته‌های عیب تشخیص داده شده در ورق به صورت برخط است.',
                    'en': 'Online Report Classification Page \n This page is related to viewing the online information and statistics of the defect classes detected in the sheet.'},

    'page_online_report_width': {'fa': 'صفحه‌ی عرض‌سنج گزارش آنلاین \n این صفحه مربوط به مشاهده‌ی اطلاعات و آمار عرض ورق به صورت برخط است.',
                    'en': 'Online Report Width Page \n This page is related to viewing the online information and statistics of the sheet width.'},



#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


    'page_dashboard': {'fa': 'در این صفحه تمام پارامتر به اختصار نمایش داده میشوند و برای دسترسی به نرم افزار نیاز به لاگین میباشد \n این صفحه اولین صفحه نرم افزار است.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_camera': {'fa': 'در این صفحه تمام تنظیمات مربوط به دوربین صورت میگیرد و هر دوربین به صورت مجزا یا گروهی مقادیر خود را میگیرد و در نهایت در دیتابیس ذخیره میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_users': {'fa': 'در این صفحه کاربران نرم افزار تعریف میشوند این کاربران در هر سه نرم افزار دسترسی دارند و سطح دسترسی آنها مشخص میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_settings': {'fa': 'در این صفحه تنظیمات کلی مربوط به نزم افزار تنظیمات مشخص میشود .',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_calibration': {'fa': 'در این صفحه پارامتر های مروبط به الگوریتم پردازش تصویر و عرض سنج مشخص میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_level2': {'fa': 'در این صفحه نوع ارتباط و پارامتر های ارتباط نرم افزار تنظیمات با کارخانه مشخص و اعمال میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},

    'page_defection': {'fa': 'در این صفحه عیوب و دسته بندی ورق تعریف میشوند .',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_plc': {'fa': 'در این صفحه آی پی پی ال سی و حافظه های آن نمایش و ذخیره میشوند.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
    'page_storage': {'fa': 'در این صفحه تنظیمات مربوط به حافظه برای حذف داده های قدیمی اعمال میشود.',
                            'en': 'Dashboard Page \n This page is main page and show the brief content of all program.'},
}

HELPS_ADDRESS = {
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Training Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
    'SETTINGS_PAGE': {'fa': 'images/helps/settings_page_fa.png',
                    'en': 'images/helps/settings_page.png'},
    'LIVE_PAGE': {'fa': 'images/helps/live_page_fa.png',
                    'en': 'images/helps/live_page.png'},
    'TECHNICAL_PAGE': {'fa': 'images/helps/technical_page_fa.png',
                    'en': 'images/helps/technical_page.png'},
    'LABEL_PAGE': {'fa': 'images/helps/label_page_fa.png',
                    'en': 'images/helps/label_page.png'},
    'PROFILE_CREATEDS_PAGE': {'fa': 'images/helps/profile_createds_fa.png',
                            'en': 'images/helps/profile_createds.png'},
    'PROFILE_ALLDS_PAGE': {'fa': 'images/helps/profile_allds_fa.png',
                            'en': 'images/helps/profile_allds.png'},
    'PROFILE_MYDS_PAGE': {'fa': 'images/helps/profile_myds_fa.png',
                            'en': 'images/helps/profile_myds.png'},
    'PROFILE_MYPIP_PAGE': {'fa': 'images/helps/profile_mypip_fa.png',
                            'en': 'images/helps/profile_mypip.png'},
    'BINARY_TRAINING_PAGE': {'fa': 'images/helps/binary_training_page_fa.png',
                            'en': 'images/helps/binary_training_page.png'},
    'BINARY_HISTORY_PAGE': {'fa': 'images/helps/binary_history_page_fa.png',
                            'en': 'images/helps/binary_history_page.png'},
    'BINARYLIST_PAGE': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'LOC_TRAINING_PAGE': {'fa': 'images/helps/loc_training_page_fa.png',
                            'en': 'images/helps/loc_training_page.png'},
    'LOC_HISTORY_PAGE': {'fa': 'images/helps/loc_history_page_fa.png',
                            'en': 'images/helps/loc_history_page.png'},
    'CLASSLIST_PAGE': {'fa': 'images/helps/classlist_page_fa.png',
                            'en': 'images/helps/classlist_page.png'},
    'YOLO_TRAINING_PAGE': {'fa': 'images/helps/yolo_training_page_fa.png',
                            'en': 'images/helps/yolo_training_page.png'},
    'YOLO_HISTORY_PAGE': {'fa': 'images/helps/yolo_history_page_fa.png',
                            'en': 'images/helps/yolo_history_page.png'},
    'PBT_PIPLINE_PAGE':{'fa':'images/helps/PBT_pipline_page.png',
                        'en':'images/helps/PBT_pipline_page.png'},
    'PBT_LOADDATASET_PAGE' :{'fa':'images/helps/PBT_loaddataset_page.png',
                              'en':'images/helps/PBT_loaddataset_page.png'},
    'PBT_HISTORY_PAGE':{'fa':'images/helps/PBT_history_page.png',
                        'en':'images/helps/PBT_history_page.png'},
    'LOADSHEET_PAGE':{'fa':'images/helps/loadsheet_page_fa.png',
                        'en':'images/helps/loadsheet_page.png'},
    'IMAGEENLARGEMENT_PAGE': {'fa':'images/helps/imageenlargement_page_fa.png',
                                'en':'images/helps/imageenlargement_page.png'},
    'SHOWLOGS_PAGE': {'fa':'images/helps/showlogs_page_fa.png',
                                'en':'images/helps/showlogs_page.png'},


#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Operator Help--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    "page_settings_and_info": {
        "fa": "images/helps/operator_setting_page_fa.jpg",
        "en": "images/helps/operator_setting_page.jpg",
    },

    'page_model_settings': {
        "fa": "images/helps/operator_setting_page_fa.jpg",
        "en": "images/helps/operator_setting_page.jpg",
    },
    
    "page_detection": {
        "fa": "images/helps/operator_detection_page_fa.jpg",
        "en": "images/helps/operator_detection_page.jpg",
    },
    
    "page_live": {
        "fa": "images/helps/operator_live_page_fa.jpg",
        "en": "images/helps/operator_live_page.jpg",
    },

    "page_offline_report_search": {
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },

    'page_offline_report_technical': {
        "fa": "images/helps/operator_technical_view_report_fa.jpg",
        "en": "images/helps/operator_technical_view_report.jpg",
    },

    'page_offline_report_defect_slider': {
        "fa": "images/helps/operator_defect_slider_fa.jpg",
        "en": "images/helps/operator_defect_slider.jpg",
    },

    'page_offline_report_binary': {
        "fa": "images/helps/operator_binary_report_fa.jpg",
        "en": "images/helps/operator_binary_report.jpg",
    },

    'page_offline_report_classification': {
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },

    'page_offline_report_width': {
        "fa": "images/helps/operator_width_report_fa.jpg",
        "en": "images/helps/operator_width_report.jpg",
    },

    "page_online_report": {
        "fa": "صفحه‌ی تشخیص \n این صفحه مربوط به مشاهده‌ی گزارش ورق‌ها به صورت بر‌خط است.",
        "en": "Detection Page \n This page is related to viewing the sheets online reports.",
    },

    'page_online_report_technical': {
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },
    'page_online_report_binary': {
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },

    'page_online_report_classification': {
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },

    'page_online_report_width':{
        "fa": "images/helps/operator_offline_report_search_page_fa.jpg",
        "en": "images/helps/operator_offline_report_search_page.jpg",
    },

    "page_online_report": {
        "fa": "images/helps/operator_online_report_page_fa.jpg",
        "en": "images/helps/operator_online_report_page.jpg",
    },

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Setting Help---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    'page_dashboard': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_camera': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_defection': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},
    'page_level2': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'},                        
    'page_calibration': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_settings': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_users': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_plc': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
    'page_storage': {'fa': 'images/helps/binarylist_page_fa.png',
                        'en': 'images/helps/binarylist_page.png'}, 
}

def set_help_title(self, lang):
    self.font_label.setText(Titles['font'][lang])
    self.lang_label.setText(Titles['language'][lang])
    languages = [Titles['persian'][lang], Titles['english'][lang]]
    self.lang_comboBox.setItemText(0, languages[0])
    self.lang_comboBox.setItemText(1, languages[1])