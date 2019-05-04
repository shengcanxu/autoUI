from pywinauto.application import Application
from ElementInfoWrapper import ElementInfoWrapper
import time
app = Application(backend="uia").connect(path="C:\Program Files (x86)\XunjiePDFConverter\pdfconverter.exe")

#app = Application(backend="uia").start("notepad.exe")

app.wait_for_process_exit()

print("process: %i" % app.process)

appWrapper = ElementInfoWrapper(app)

#Menu
# menuWrapper = appWrapper.filterTop(class_name="Qt5QWindowIcon",control_type="Pane")\
#     .filterDecendent(control_type="Custom",contain_point=(625,30))
# PDF_change = menuWrapper.filterDecendent(control_type="Button",contain_point=(240,30)).getObject()
# PDF_operate = menuWrapper.filterDecendent(control_type="Button",contain_point=(330,30)).getObject()
# WPS_change = menuWrapper.filterDecendent(control_type="Button",contain_point=(420,30)).getObject()
# WORD_change = menuWrapper.filterDecendent(control_type="Button",contain_point=(520,30)).getObject()
# CAD_change = menuWrapper.filterDecendent(control_type="Button",contain_point=(620,30)).getObject()
# SPECIAL_change = menuWrapper.filterDecendent(control_type="Button",contain_point=(710,30)).getObject()
#
# PDF_change.draw_outline()
# PDF_operate.draw_outline()
# WPS_change.draw_outline()
# WORD_change.draw_outline()
# CAD_change.draw_outline()
# SPECIAL_change.draw_outline()

#Left pannel
# leftWrapper = appWrapper.filterTop(class_name="Qt5QWindowIcon",control_type="Pane")\
#     .filterChildren(class_name="Qt5QWindowIcon", control_type="Pane",children_num=2)
# leftWrapper.dump()
#
# PDF2Others = leftWrapper.filterDecendent(control_type="Button", text="PDF转换其他").getObject()
# Others2PDF = leftWrapper.filterDecendent(control_type="Button", text="其他转PDF").getObject()
# if not leftWrapper.filterDecendent(text=u"文件转Word").exist():
#     PDF2Others.click()
#     time.sleep(1)
#
# file2word = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,130)).getObject()
# file2picture = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,160)).getObject()
# file2excel = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,200)).getObject()
# file2ppt = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,240)).getObject()
# file2txt = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,270)).getObject()
# file2html = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,310)).getObject()
#
# file2word.draw_outline()
# file2picture.draw_outline()
# file2excel.draw_outline()
# file2ppt.draw_outline()
# file2txt.draw_outline()
# file2html.draw_outline()

# if not leftWrapper.filterDecendent(text=u"图片转PDF").exist():
#     Others2PDF.click()
#     time.sleep(1)
#
# word2pdf = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,170)).getObject()
# picture2pdf = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,210)).getObject()
# excel2pdf = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,245)).getObject()
# ppt2pdf = leftWrapper.filterDecendent(control_type="Button", contain_point=(90,280)).getObject()
#
# word2pdf.draw_outline()
# picture2pdf.draw_outline()
# excel2pdf.draw_outline()
# ppt2pdf.draw_outline()

#content pannel
contentWrapper = appWrapper.filterTop(class_name="Qt5QWindowIcon",control_type="Pane")\
    .filterChildren(class_name="Qt5QWindowIcon", control_type="Pane", contain_point=(400,100))

toolbarwrapper = contentWrapper.filterChildren(control_type="Custom", contain_point=(400,100))\
    .filterChildren(control_type="Custom", contain_point=(400,100))
# addfilebtn = toolbarwrapper.filterChildren(control_type="Button", contain_point=(270,100)).getObject()
#
# addfilebtn.click()
# addfilebtn.draw_outline()


#open file dialogue
#openfileWrapper = appWrapper.filterDecendent(class_name="#32770",control_type="Window")

# addressbar = openfileWrapper.filterDecendent(class_name="ReBarWindow32", control_type="Pane")\
#         .filterDecendent(class_name="msctls_progress32", control_type="ProgressBar")
#
# addressBtn = addressbar.filterChildren(class_name="ToolbarWindow32", control_type="ToolBar")\
#         .filterDecendent(control_type="Button",index=1)
# addressBtn.getFirstObject().click()
# addressEdit = addressbar.filterDecendent(class_name="ComboBox",control_type="ComboBox")\
#         .filterDecendent(class_name="Edit",control_type="Edit")
# addressEdit.getFirstObject().draw_outline()
# addressEdit.getFirstObject().set_edit_text("D:\\project\\pywinauto").type_keys("{ENTER}")

# fileNameEdit = openfileWrapper.filterChildren(class_name="ComboBox",control_type="ComboBox")\
#         .filterChildren(class_name="Edit",control_type="Edit")
# fileNameEdit.getObject().draw_outline()
# fileNameEdit.getObject().set_edit_text(u"文字文稿3.pdf")
# openButton = openfileWrapper.filterChildren(class_name="Button", control_type="Button",text=u"打开(O)")
# openButton.getObject().draw_outline()
# openButton.getObject().click()

#change to output docx file
# toDocTypeRadio = contentWrapper.filterDecendent(control_type="RadioButton",text="DOCX")
# toDocTypeRadio.getObject().click()

#change output file dictory
# outputDirButton = contentWrapper.filterDecendent(control_type="Text", text=u"输出目录：")\
#         .getParent().filterChildren(index=1)
# outputDirButton.getObject().click()
# time.sleep(1)
#
# outputDirWrapper = appWrapper.filterDecendent(class_name="#32770",control_type="Window")
# outputDirWrapper.getObject().draw_outline()
# addressbar = outputDirWrapper.filterDecendent(class_name="ReBarWindow32", control_type="Pane")\
#         .filterDecendent(class_name="msctls_progress32", control_type="ProgressBar")
#
# addressBtn = addressbar.filterChildren(class_name="ToolbarWindow32", control_type="ToolBar")\
#         .filterDecendent(control_type="Button",index=1)
# addressBtn.getFirstObject().click()
# addressEdit = addressbar.filterDecendent(class_name="ComboBox",control_type="ComboBox")\
#         .filterDecendent(class_name="Edit",control_type="Edit")
# addressEdit.getFirstObject().draw_outline()
# addressEdit.getFirstObject().set_edit_text("D:\\project\\pywinauto\\gui-inspect-tool").type_keys("{ENTER}")
#
# chooseDirButton = outputDirWrapper.filterDecendent(class_name="Button", control_type="Button",text=u"选择文件夹")
# chooseDirButton.getObject().click()


#start change fileformat
# startButton = contentWrapper.filterDecendent(control_type="Text", text=u"输出目录：")\
#         .getParent().getParent().filterChildren(index=2).filterChildren(index=1)
# startButton.getObject().click()

#clear list
clearButton = toolbarwrapper.filterChildren(control_type="Button", contain_point=(540,100)).getObject()
clearButton.click()
time.sleep(1)
tipsWrapper = appWrapper.filterDecendent(class_name="Qt5QWindowIcon", control_type="Window", text=u"提示信息")
tipsOkButton = tipsWrapper.filterDecendent(control_type="Button", text=u"确定").getObject()
tipsOkButton.click()