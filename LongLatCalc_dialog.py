# -*- coding: utf-8 -*-
import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'LongLatCalc_dialog_base.ui'))

class LongLatCalcDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(LongLatCalcDialog, self).__init__(parent)
        
        self.setupUi(self)

        self.spbLongD.valueChanged.connect(self.longDMStoDD)
        self.spbLongM.valueChanged.connect(self.longDMStoDD)
        self.spbLongS.valueChanged.connect(self.longDMStoDD)
        self.cmbLong.currentTextChanged.connect(self.longDMStoDD)

        self.spbLongDD.editingFinished.connect(self.longDDtoDMS)

        self.spbLatD.valueChanged.connect(self.latDMStoDD)
        self.spbLatM.valueChanged.connect(self.latDMStoDD)
        self.spbLatS.valueChanged.connect(self.latDMStoDD)
        self.cmbLat.currentTextChanged.connect(self.latDMStoDD)

        self.spbLatDD.editingFinished.connect(self.latDDtoDMS)

    def longDMStoDD(self):
        d = self.spbLongD.value()
        m = self.spbLongM.value()
        s = self.spbLongS.value()
        hemisf = self.cmbLong.currentText()

        dd = float(d) + m/60 + s/3600
        if hemisf == "W":
            dd = dd *-1

        self.spbLongDD.setValue(dd)

    def latDMStoDD(self):
        d = self.spbLatD.value()
        m = self.spbLatM.value()
        s = self.spbLatS.value()
        hemisf = self.cmbLat.currentText()

        dd = float(d) + m/60 + s/3600
        if hemisf == "S":
            dd = dd *-1

        self.spbLatDD.setValue(dd)

    def longDDtoDMS(self):
        dd = self.spbLongDD.value()

        if dd < 0:
            self.cmbLong.setCurrentText("W")
            dd = dd *-1
        else:
            self.cmbLong.setCurrentText("E")

        d = int(dd)
        m = (dd - d) * 60
        s = (m - int(m)) * 60

        self.spbLongD.setValue(d)
        self.spbLongM.setValue(int(m))
        self.spbLongS.setValue(s)

    def latDDtoDMS(self):
        dd = self.spbLatDD.value()

        if dd < 0:
            self.cmbLat.setCurrentText("S")
            dd = dd *-1
        else:
            self.cmbLat.setCurrentText("N")

        d = int(dd)
        m = (dd - d) * 60
        s = (m - int(m)) * 60

        self.spbLatD.setValue(d)
        self.spbLatM.setValue(int(m))
        self.spbLatS.setValue(s)

