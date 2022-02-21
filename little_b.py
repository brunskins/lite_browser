from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

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

        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://duckduckgo.com"))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        if "https://" not in url:
            if "http://" not in url:
                url = "https://" + url
        self.browser.setUrl(QUrl(url))
app = QApplication(sys.argv)
QApplication.setApplicationName("little b")
window = MainWindow()
app.exec_()
