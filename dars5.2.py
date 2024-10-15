import sys
from PyQt6.QtWidgets import  QWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication


class VideoThumbnail(QWidget):
    def __init__(self,thumbnail, duration, title, channel_logo, channel_name, views, time_ago) :
        super().__init__()

        thumbnail_label = QLabel()
        pixmap = QPixmap(thumbnail)
        thumbnail_label.setPixmap(pixmap.scaled(320, 180, Qt.AspectRatioMode.KeepAspectRatio))
        thumbnail_label.setFixedSize(320, 180)

        duration_label = QLabel(duration)
        duration_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        duration_label.setStyleSheet("background-color:black; color: white; padding: 2px")

        thumbnail_container = QWidget()
        thumbnail_container_layout=QVBoxLayout()
        thumbnail_container_layout.addWidget(thumbnail_label)
        thumbnail_container_layout.addWidget(duration_label,alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        thumbnail_container.setLayout(thumbnail_container_layout)

        title_label = QLabel(title)
        title_label.setWordWrap(True)
        channel_logo_label = QLabel(channel_logo)
        pixmap = QPixmap(channel_logo)
        channel_logo_label.setPixmap(pixmap.scaled(320, 180, Qt.AspectRatioMode.KeepAspectRatio))
        channel_logo_label.setFixedSize(40, 40)
        channel_name_label = QLabel(channel_name)

        channel_info_layout = QHBoxLayout()
        channel_info_layout.addWidget(channel_logo_label)
        channel_info_layout.addWidget(channel_name_label)

        views_and_time_layout = QHBoxLayout()
        views_label = QLabel(views)
        time_ago_label = QLabel(time_ago)
        views_and_time_layout.addWidget(views_label)
        views_and_time_layout.addWidget(time_ago_label)

        video_layout = QVBoxLayout()
        video_layout.addWidget(thumbnail_container)
        video_layout.addWidget(title_label)
        video_layout.addLayout(channel_info_layout)
        video_layout.addLayout(views_and_time_layout)

        self.setLayout(video_layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        grid.addWidget(VideoThumbnail("assets/wings.webp", "5:53", "wings | animated short Film | SVA thesis",
                                      "assets/gf_channel.jpg","GothFrog",
                                      "9.4M views",
                                      "5 years ago"),0,0)
        grid.addWidget(VideoThumbnail("assets/57.webp","22:44","I'm 57.If you're in your 20's please watch this",
                                      "channel Logo 2","Mark"
                                                       "Tilbury","1.5M views","2weeks ago"),0,1)
        grid.addWidget(
        VideoThumbnail("assets/ten_tips.webp", "9:44", "10 Tools Every Blender Noob Should Learn",
                                   "Channel Logo 3", "Brad Colbow", "965K views", "2 years ago"), 0, 2)
        grid.addWidget(
        VideoThumbnail("assets/blender.webp", "19:11", "Making a Chocolate CAKE in Blender is so easy",
                                   "Channel Logo 4", "Ali Khoshnazar", "1.1K views", "1 day ago"), 1, 0)
        grid.addWidget(VideoThumbnail("assets/al_xooliq.webp", "28:38", "91-Дарс АЛ-ХООЛИК (1-КИСМ)",
                                              "Channel Logo 5", "Ilmnuri Official", "3.5K views", "1 day ago"), 1, 1)
        grid.addWidget(
        VideoThumbnail("assets/andijondagi.webp", "25:58", "Andijondagi hech kim bilmagan mo'jiza",
                                   "Channel Logo 6", "Sardor Rahimxon", "353K views", "1 month ago"), 1, 2)

        self.setWindowTitle("Hello, PyQt6")

        self.setGeometry(100, 100, 1366, 768)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())














