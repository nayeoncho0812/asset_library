from Qt.QtWidgets import QLabel
from Qt.QtGui import QFont
from Qt.QtCore import Qt


class DynamicCircleLabel(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Pretendard", 7, QFont.Weight.Thin))  # 글꼴 설정
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 텍스트 중앙 정렬
        self.setStyleSheet("""
            background-color: #6058EB;
            color: white;
            border-radius: 4px;
        """)  
        self.update_size()

    def update_size(self):
        """ 텍스트 길이에 따라 QLabel 크기 조정 """
        text_width = self.fontMetrics().horizontalAdvance(self.text())  # 텍스트 너비 계산
        self.setFixedWidth(max(6, text_width + 6))  # 최소 8px 유지, 텍스트 크기에 맞게 확장
        self.setFixedHeight(11)  # 높이는 고정
