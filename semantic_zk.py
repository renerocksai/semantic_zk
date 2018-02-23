import sys
from PyQt5.Qt import QApplication, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


def viewhtml(html):
    app = QApplication([])

    view = QWebEngineView()
    view.setHtml(html)
    view.show()

    app.exec_()


def viewurl(url):
    app = QApplication([])

    view = QWebEngineView()
    view.load(url)
    view.show()

    app.exec_()


viewurl(QUrl('file:///Users/rs/projects/zk2setevi/output/out.html'))
