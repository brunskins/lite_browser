from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys
global current_tab
global tab_count
global tab_urls
current_tab=0
tab_count=0
tab_urls=["http://duckduckgo.com"]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://duckduckgo.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        #nav bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


        forward_btn = QAction("forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search_for)
        self.search_bar.resize(10 , 10)
        navbar.addWidget(self.search_bar)

        
        #tab bar
        tabbar = QToolBar()
        self.addToolBar(tabbar)

        new_tab_btn = QAction("new tab", self)
        new_tab_btn.triggered.connect(self.new_tab)
        tabbar.addAction(new_tab_btn)

        next_tab_btn = QAction("next tab", self)
        next_tab_btn.triggered.connect(self.next_tab)
        tabbar.addAction(next_tab_btn)

        previous_tab_btn = QAction("previous tab", self)
        previous_tab_btn.triggered.connect(self.previous_tab)
        tabbar.addAction(previous_tab_btn)

        self.browser.urlChanged.connect(self.update_url)

    def new_tab(self, url):
        global current_tab
        global tab_count
        global tab_urls
        print("new tab")
        tab_count=tab_count+1
        tab_urls.append("http://duckduckgo.com")
        current_url = self.browser.url()
        print(current_url)
        tab_urls[current_tab] = current_url.toString()
        print(tab_urls)
        current_tab=tab_count
        self.browser.setUrl(QUrl(tab_urls[tab_count]))

    def next_tab(self, url):
        global current_tab
        global tab_count
        global tab_urls
        print("alive")
        current_url = self.browser.url()
        tab_urls[current_tab] = current_url.toString()
        print("next tab")
        current_tab=current_tab+1
        if current_tab > tab_count:
            current_tab=0
        print("current tab is ", current_tab)
        print("total tabs is ", tab_count)
        print(tab_urls)
        self.browser.setUrl(QUrl(tab_urls[current_tab]))

    def previous_tab(self, url):
        global current_tab
        global tab_count
        global tab_urls
        print("alive")
        current_url = self.browser.url()
        tab_urls[current_tab] = current_url.toString()   
        print("previous tab")
        current_tab=current_tab-1
        if current_tab < 0:
            current_tab=tab_count
        print("current tab is ", current_tab)
        print("total tabs is ", tab_count)
        self.browser.setUrl(QUrl(tab_urls[current_tab]))

    def search_for(self):
        url = self.search_bar.text()
        url2= 'https://duckduckgo.com/?q=' + url + '&t=h_&ia=web'
        self.browser.setUrl(QUrl(url2))
    
    def navigate_home(self, url):
        self.browser.setUrl(QUrl("http://duckduckgo.com"))

    def update_url(self):
        url= self.browser.url()
        self.url_bar.setText(url.toString())

    def navigate_to_url(self):
        print("alive")
        url = self.url_bar.text()
        if "https://" not in url:
            if "http://" not in url:
                url = "https://" + url
        self.browser.setUrl(QUrl(url))
        print("alive 2")
    
app = QApplication(sys.argv)
QApplication.setApplicationName("little b")
window = MainWindow()
app.exec_()
