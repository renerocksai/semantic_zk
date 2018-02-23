import sys
import os
from PyQt5.Qt import  QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSplitter, QFrame, \
                            QProgressBar, QApplication, QComboBox, QFileDialog, QMessageBox
from libzk2setevi.zk2setevi import Zk2Setevi


class Semantic_ZK(QWidget):
    def __init__(self):
        super().__init__()
        self.linkstyle_list = ['single', 'double', '§']
        self.parser_list = ['native', 'mmd', 'pandoc']

        main_split = QSplitter(Qt.Horizontal)

        # Left Side
        left_widget = QWidget()
        left_vlay = QVBoxLayout()
        left_widget.setLayout(left_vlay)

        # ZK Folder
        zk_lbl_folder = QLabel('ZK Folder')
        zk_hlay = QHBoxLayout()
        zk_ed_folder = QLineEdit('(please select)')
        zk_bt_folder = QPushButton('...')
        zk_hlay.addWidget(zk_ed_folder)
        zk_hlay.addWidget(zk_bt_folder)
        left_vlay.addWidget(zk_lbl_folder)
        left_vlay.addLayout(zk_hlay)

        # Output Folder
        out_lbl_folder = QLabel('Output Folder')
        out_hlay = QHBoxLayout()
        out_ed_folder = QLineEdit('(please select)')
        out_bt_folder = QPushButton('...')
        out_hlay.addWidget(out_ed_folder)
        out_hlay.addWidget(out_bt_folder)
        left_vlay.addWidget(out_lbl_folder)
        left_vlay.addLayout(out_hlay)

        # Bib File
        bib_lbl = QLabel('Bib File')
        bib_hlay = QHBoxLayout()
        bib_ed = QLineEdit('(auto)')
        bib_bt = QPushButton('...')
        bib_hlay.addWidget(bib_ed)
        bib_hlay.addWidget(bib_bt)
        left_vlay.addWidget(bib_lbl)
        left_vlay.addLayout(bib_hlay)

        # Extension
        ext_hlay = QHBoxLayout()
        ext_lbl = QLabel('Markdown Extension')
        ext_ed = QLineEdit('.md')
        ext_hlay.addWidget(ext_lbl)
        ext_hlay.addStretch(1)
        ext_hlay.addWidget(ext_ed)
        left_vlay.addLayout(ext_hlay)

        # Link Style
        lstyle_hlay = QHBoxLayout()
        lstyle_lbl = QLabel('Link Style')
        lstyle_choice = QComboBox()
        lstyle_choice.addItems(self.linkstyle_list)
        lstyle_choice.setCurrentIndex(1)
        lstyle_hlay.addWidget(lstyle_lbl)
        lstyle_hlay.addWidget(lstyle_choice)
        left_vlay.addLayout(lstyle_hlay)

        # Parser
        parser_hlay = QHBoxLayout()
        parser_lbl = QLabel('Parser')
        parser_choice = QComboBox()
        parser_choice.addItems(self.parser_list)
        parser_choice.setCurrentIndex(1)
        parser_hlay.addWidget(parser_lbl)
        parser_hlay.addWidget(parser_choice)
        left_vlay.addLayout(parser_hlay)

        # Separator
        sep = self.hline()
        left_vlay.addStretch(1)
        left_vlay.addWidget(sep)

        # Convert Button
        convert_hlay = QHBoxLayout()
        convert_bt = QPushButton('Convert!')
        convert_hlay.setAlignment(Qt.AlignHCenter)
        convert_hlay.addWidget(convert_bt)
        left_vlay.addLayout(convert_hlay)

        # Progress
        progress_hlay = QHBoxLayout()
        progress_lbl = QLabel('Progress')
        progress_prg = QProgressBar()
        progress_hlay.addWidget(progress_lbl)
        progress_hlay.addWidget(progress_prg)
        left_vlay.addLayout(progress_hlay)

        # Info
        info_hlay = QHBoxLayout()
        info_lbl = QLabel('Info:')
        info_txt = QLabel()
        info_hlay.addWidget(info_lbl)
        info_hlay.addWidget(info_txt)
        info_hlay.addStretch(1)
        left_vlay.addLayout(info_hlay)

        # HTML view
        self.html_view = QWebEngineView()
        self.html_view.setHtml('<center><h2>Preview</h2></center>')

        # Add to splitter
        main_split.addWidget(left_widget)
        main_split.addWidget(self.html_view)

        # Add to self
        lay_all = QHBoxLayout()
        lay_all.addWidget(main_split)
        self.setLayout(lay_all)

        # What to keep?
        self.info_txt = info_txt
        self.progressbar = progress_prg
        self.ed_zk_folder = zk_ed_folder
        self.ed_output_folder = out_ed_folder
        self.ed_bibfile = bib_ed
        self.ed_extension = ext_ed
        self.sel_linkstyle = lstyle_choice
        self.sel_parser = parser_choice

        # Connections
        convert_bt.clicked.connect(self.on_convert_clicked)
        zk_bt_folder.clicked.connect(self.on_zk_folder_clicked)
        out_bt_folder.clicked.connect(self.on_output_folder_clicked)
        bib_bt.clicked.connect(self.on_bibfile_clicked)


    def on_convert_clicked(self):
        bibfile = None
        error_lines = []
        if os.path.exists(self.ed_bibfile.text()):
            bibfile = self.ed_bibfile.text()
        if not os.path.exists(self.ed_zk_folder.text()):
            error_lines.append('The Zettelkasten folder is invalid')
        if not os.path.exists(self.ed_output_folder.text()):
            error_lines.append('The output folder is invalid')
        extension = self.ed_extension.text()
        if extension:
            if not extension.startswith('.'):
                error_lines.append('The markdown extension does not start with a dot')
            bad_chars = []
            invalid_chars = '*?/\\:'
            for char in extension:
                if char in invalid_chars:
                    bad_chars.append(char)
            for char in bad_chars:
                error_lines.append('The markdown extension contains a ' + char)
        else:
            error_lines.append('The markdown extension is empty')
        if error_lines:
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Critical)
            mb.setWindowTitle('Invalid settings')
            mb.setText('Some of the settings are invalid')
            mb.setDetailedText('\n'.join(error_lines))
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()
            return

        # everything ok
        zk_folder = self.ed_zk_folder.text()
        output_folder = self.ed_output_folder.text()
        linkstyle = self.linkstyle_list[self.sel_linkstyle.currentIndex()]
        parser = self.parser_list[self.sel_parser.currentIndex()]
        # try to find out our home
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        converter = Zk2Setevi(home=bundle_dir, folder=zk_folder, out_folder=output_folder,
                              bibfile=bibfile, extension=extension,
                              linkstyle=linkstyle, parser=parser,
                              progress_callback=self.progress_callback, finish_callback=self.finish_callback)
        converter.create_html()
        if False:
            with open(os.path.join(output_folder, 'out.html'), mode='r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
                self.html_view.setHtml(html)
        else:
            url = 'file:///' + output_folder + '/out.html'
            qurl = QUrl(url)
            self.html_view.load(qurl)

    def on_zk_folder_clicked(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file:
            self.ed_zk_folder.setText(file)

    def on_output_folder_clicked(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file:
            self.ed_output_folder.setText(file)

    def on_bibfile_clicked(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Bibliography files (*.bib)")
        if file:
            self.ed_bibfile.setText(file)

    def progress_callback(self, counter, count, msg):
        percent = int(counter / count * 100)
        self.progressbar.setValue(percent)
        self.info_txt.setText(msg)

    def finish_callback(self):
        self.progressbar.setValue(100)
        self.info_txt.setText('Finished!')

    @staticmethod
    def hline():
        h = QFrame()
        h.setFrameShape(QFrame.HLine)
        h.setFrameShadow(QFrame.Sunken)
        return h


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Semantic_ZK()
    mainwindow.setWindowTitle('Semantic ZK')
    mainwindow.show()
    mainwindow.setFocus()
    app.exec_()

