import sys,os
import wavedrom
from agileWaveDrom import *
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QHBoxLayout,QPlainTextEdit,QVBoxLayout,QPushButton
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QUrl,Qt
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.editor = QPlainTextEdit()
        self.wave_shower = QWebEngineView()
        self.wave_shower.load(QUrl(''))
        self.hspliter = QSplitter(Qt.Horizontal)
        self.hspliter.addWidget(self.editor)
        self.hspliter.addWidget(self.wave_shower)
        self.hspliter.setStretchFactor(0,4)
        self.hspliter.setStretchFactor(1,2)

        self.gen_button = QPushButton('Agile-Wavedrom预览')
        self.drom_button= QPushButton('Wavedrom切换')
        self.hbox_button=QHBoxLayout()
        self.hbox_button.addWidget(self.gen_button)
        self.hbox_button.addWidget(self.drom_button)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.hspliter)
        self.vbox.addLayout(self.hbox_button)
        self.setLayout(self.vbox)

        self.gen_button.clicked.connect(self.fresh_code)
        self.drom_button.clicked.connect(self.switch_wavedrom)

        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle('Agile-Wavedrom')
        self.setGeometry(400,400,1300,500)
        #self.setWindowIcon(QIcon('tree.jpg'))
        self.gen_button.setFont(QFont("Consolas", 12))
        self.drom_button.setFont(QFont("Consolas", 12))
        self.editor.setFont(QFont("Consolas", 12))
        self.InitDescription()
    def fresh_code(self):
        plain_text = self.editor.toPlainText()
        wave_text = extractSignal(plain_text.split('\n'))
        try:
            svg = wavedrom.render(wave_text)
            svg.saveas('wave.svg')
            url = QUrl.fromLocalFile(os.getcwd()+'\wave.svg')
            if url.isValid():
                self.wave_shower.load(url)
                with open('wave.dat','w') as f: f.write(plain_text)
            else: self.wave_shower.setHtml("""<h2> Error: SVG文件无效 ！</h2>""")
        except:
            self.wave_shower.setHtml("""<h2> Error: check Edge format, all edges exist?</h2>""")
    def switch_wavedrom(self):
        self.wave_shower.load(QUrl('https://wavedrom.com/editor.html'))
    def InitDescription(self):
        self.editor.setPlainText('''示例：
clk: p . . . . . . . .;
A: 0 1 . .-c . ;
B: x D0 1 0-y z .;
C: 0 . .  1-d 0 D1-x;
EDGE: x-y c-d;

1. 信号名：[每个cycle的值-<标签>] [cycle2], 以“；”结束
2. 画线固定使用：EDGE: [node连线1] [连线2]
3. 注释可以不删除，自动保存为wave.dat和wave.svg
''')
        #self.editor.setPlaceholderText('Input wave description here....')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())