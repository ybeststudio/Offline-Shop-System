if __USE_DYNAMIC_MODULE__:
	import pyapi

app = __import__(pyapi.GetModuleName("app"))
player = __import__(pyapi.GetModuleName("player"))

import ui
import localeInfo
import ime
import chat
import item
import wndMgr
import uiScriptLocale
import uiToolTip
import constInfo

class PopupDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		if app.ENABLE_IKASHOP_RENEWAL:
			self.autocloseTime = None
		self.__LoadDialog()

		self.acceptEvent = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.accceptButton = self.GetChild("accept")
			self.accceptButton.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		self.acceptEvent()

	def Destroy(self):
		self.Close()
		self.ClearDictionary()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SetText(self, text):
		self.message.SetText(text)

	def SetAcceptEvent(self, event):
		self.acceptEvent = event

	def SetButtonName(self, name):
		self.accceptButton.SetText(name)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnIMEReturn(self):
		self.Close()
		return TRUE

	if app.ENABLE_IKASHOP_RENEWAL:
		def SetAutoClose(self, seconds):
			self.autocloseTime = app.GetTime() + seconds

		def OnUpdate(self):
			if self.autocloseTime is not None:
				remainTime = max(0, self.autocloseTime - app.GetTime())
				if remainTime == 0:
					self.autocloseTime = None
					self.accceptButton.SetText(uiScriptLocale.OK)
					self.Close()
					return
				self.accceptButton.SetText(uiScriptLocale.OK + " ({:0.1f} s)".format(remainTime))

	def GetTextSize(self):
		if self.message:
			return self.message.GetTextSize()

		return (0,0)

	def GetLineHeight(self):
		if self.message:
			return self.message.GetLineHeight()

		return 0

	def SetLineHeight(self, Height):
		self.message.SetLineHeight(Height)

	def GetTextLineCount(self):
		return self.message.GetTextLineCount()

class InputDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialog.py")

		getObject = self.GetChild
		self.board = getObject("Board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputSlot = getObject("InputSlot")
		self.inputValue = getObject("InputValue")

	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.SetBoardWidth(max(width + 50, 160))
		self.SetSlotWidth(width)
		self.inputValue.SetMax(length)

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())
		if self.IsRTL():
			self.inputValue.SetPosition(self.inputValue.GetWidth(), 0)

	def SetBoardWidth(self, width):
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.board.SetSize(max(width + 50, 160), self.GetHeight())	
		if self.IsRTL():
			self.board.SetPosition(self.board.GetWidth(), 0)
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetText(self):
		return self.inputValue.GetText()

class InputDialogWithDescription(InputDialog):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description = getObject("Description")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription(self, text):
		self.description.SetText(text)

class InputDialogWithDescription2(InputDialog):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription2.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description1 = getObject("Description1")
			self.description2 = getObject("Description2")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription1(self, text):
		self.description1.SetText(text)

	def SetDescription2(self, text):
		self.description2.SetText(text)

class QuestionDialog(ui.ScriptWindow):
	def __init__(self, size = "default"):
		ui.ScriptWindow.__init__(self)
		self.size = size
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

		if self.size == "thin":
			self.SetSize(340, 70)
			self.board.SetSize(340, 70)
			self.textLine.SetPosition(0, 20)
			self.acceptButton.SetPosition(-40, 35)
			self.cancelButton.SetPosition(40, 35)

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def __SetTextButton(self, button, text):
		if text in (localeInfo.UI_ACCEPT, localeInfo.UI_DENY, localeInfo.UI_CLOSE, uiScriptLocale.YES, uiScriptLocale.NO):
			return
		button.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		button.SetText(text)

	def SetAcceptText(self, text):
		self.__SetTextButton(self.acceptButton, text)

	def SetCancelText(self, text):
		self.__SetTextButton(self.cancelButton, text)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

class QuestionDialog2(QuestionDialog):
	def __init__(self):
		QuestionDialog.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def SetText1(self, text):
		self.textLine1.SetText(text)
		self.__FitWidth()

	def SetText2(self, text):
		self.textLine2.SetText(text)
		self.__FitWidth()

	def __FitWidth(self):
		width = max(self.textLine1.GetTextSize()[0], self.textLine2.GetTextSize()[0]) + 30
		width = max(width, 180)
		self.SetSize(width, self.GetHeight())
		self.board.SetSize(width, self.board.GetHeight())
		self.UpdateRect()

	if app.ENABLE_GROWTH_PET_SYSTEM:
		def GetTextSize1(self):
			if self.textLine1:
				return self.textLine1.GetTextSize()

			return (0, 0)

		def GetTextSize2(self):
			if self.textLine2:
				return self.textLine2.GetTextSize()

			return (0, 0)

class QuestionDialog2(QuestionDialog):

	def __init__(self):
		QuestionDialog.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def SetText1(self, text):
		self.textLine1.SetText(text)
		self.__FitWidth()

	def SetText2(self, text):
		self.textLine2.SetText(text)
		self.__FitWidth()

	def __FitWidth(self):
		width = max(self.textLine1.GetTextSize()[0], self.textLine2.GetTextSize()[0]) + 30
		width = max(width, 180)
		self.SetSize(width, self.GetHeight())
		self.board.SetSize(width, self.board.GetHeight())
		self.UpdateRect()

	if app.ENABLE_GROWTH_PET_SYSTEM:
		def GetTextSize1(self):
			if self.textLine1:
				return self.textLine1.GetTextSize()
				
			return (0,0)
			
		def GetTextSize2(self):
			if self.textLine2:
				return self.textLine2.GetTextSize()
				
			return (0,0)

class QuestionDialogWithMultiTextline(QuestionDialog):
	FIRST_LINE_Y = 38
	LINE_STEP = 16
	BUTTON_GAP = 25
	BOTTOM_PAD = 21
	MIN_WIDTH = 340

	def __init__(self):
		QuestionDialog.__init__(self)
		self.multiLineList = []

	def SetText(self, text):
		for line in self.multiLineList:
			line.Hide()
		self.multiLineList = []
		contentLines = text.split("\n")
		widest = 0
		for index, content in enumerate(contentLines):
			line = ui.TextLine()
			line.SetParent(self.board)
			line.SetWindowHorizontalAlignCenter()
			line.SetHorizontalAlignCenter()
			line.SetVerticalAlignCenter()
			line.SetPosition(0, self.FIRST_LINE_Y + index * self.LINE_STEP)
			line.SetText(content)
			line.Show()
			self.multiLineList.append(line)
			widest = max(widest, line.GetTextSize()[0])
		self.textLine.Hide()
		buttonY = self.FIRST_LINE_Y + (len(contentLines) - 1) * self.LINE_STEP + self.BUTTON_GAP
		self.acceptButton.SetPosition(-40, buttonY)
		self.cancelButton.SetPosition(40, buttonY)
		height = buttonY + self.acceptButton.GetHeight() + self.BOTTOM_PAD
		width = max(self.MIN_WIDTH, widest + 40)
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

class QuestionDialogWithTimeLimit(QuestionDialog2):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()
		self.endTime = 0
		self.timeoverMsg = None
		self.isCancelOnTimeover = FALSE

	def __del__(self):
		QuestionDialog2.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self, msg, timeout):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		self.SetText1(msg)
		self.endTime = app.GetTime() + timeout

	def OnUpdate(self):
		leftTime = max(0, self.endTime - app.GetTime())
		self.SetText2(localeInfo.UI_LEFT_TIME % (leftTime))
		if leftTime<0.5:
			if self.timeoverMsg:
				chat.AppendChat(chat.CHAT_TYPE_INFO, self.timeoverMsg)
			if self.isCancelOnTimeover:
				self.cancelButton.CallEvent()

	def SetTimeOverMsg(self, msg):
		self.timeoverMsg = msg

	def SetCancelOnTimeOver(self):
		self.isCancelOnTimeover = TRUE

class QuestionDialogWithTimeLimit2(QuestionDialog2):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()
		self.endTime = 0
		self.timeOverMsg = 0
		self.timeOverEvent = None
		self.timeOverEventArgs = None

	def __del__(self):
		QuestionDialog2.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self, timeout):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		self.endTime = app.GetTime() + timeout

	def SetTimeOverEvent(self, event, *args):
		self.timeOverEvent = event
		self.timeOverEventArgs = args

	def SetTimeOverMsg(self, msg):
		self.timeOverMsg = msg

	def OnTimeOver(self):
		if self.timeOverEvent:
			apply(self.timeOverEvent, self.timeOverEventArgs)
		if self.timeOverMsg:
			chat.AppendChat(chat.CHAT_TYPE_INFO, self.timeOverMsg)

	def OnUpdate(self):
		leftTime = max(0, self.endTime - app.GetTime())
		self.SetText2(localeInfo.UI_LEFT_TIME % (leftTime))
		if leftTime <= 0:
			self.OnTimeOver()

class MoneyInputDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
		self.__CreateDialog()
		if app.ENABLE_GOLD_LIMIT:
			self.SetMaxLength(16)
		else:
			self.SetMaxLength(9)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/moneyinputdialog.py")

		getObject = self.GetChild
		self.board = self.GetChild("board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputValue = getObject("InputValue")
		self.inputValue.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.moneyText = getObject("MoneyValue")

		if app.ENABLE_IKASHOP_RENEWAL:
			self.inputValue.numberMode = False
			if app.EXTEND_IKASHOP_ULTIMATE:
				self.priceAverage = None

	def Open(self):
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	if app.ENABLE_IKASHOP_RENEWAL:
		if app.EXTEND_IKASHOP_ULTIMATE:
			def SetPriceAverage(self, price):
				if not self.priceAverage:
					self.priceAverage = ui.TextLine()
					self.priceAverage.SetParent(self)
					self.priceAverage.SetPosition(self.GetWidth()/2, 30)
					self.priceAverage.SetHorizontalAlignCenter()
					self.priceAverage.Show()

					for child in self.board.Children:
						cx, cy = child.GetLocalPosition()
						child.SetPosition(cx, cy+15)
					self.SetSize(self.GetWidth(), self.GetHeight() + 15)
					self.board.SetSize(self.board.GetWidth(), self.board.GetHeight() + 15)

				if price == -1:
					self.priceAverage.SetText(localeInfo.IKASHOP_ULTIMATE_PRICE_AVERAGE_REQUESTING)
				elif price == 0:
					self.priceAverage.SetText(localeInfo.IKASHOP_ULTIMATE_PRICE_AVERAGE_NOT_AVAILABLE)
				else:
					self.priceAverage.SetText(localeInfo.IKASHOP_ULTIMATE_PRICE_AVERAGE_VALUE.format(localeInfo.NumberToMoneyString(price)))

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputValue = None
		self.Hide()

		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				if self.priceAverage:
					self.priceAverage.Destroy()
				self.priceAverage = None

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		if app.ENABLE_GOLD_LIMIT:
			length = min(16, length)
		else:
			length = min(9, length)
		self.inputValue.SetMax(length)

	def SetMoneyHeaderText(self, text):
		self.moneyHeaderText = text

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):
		if app.ENABLE_IKASHOP_RENEWAL:
			if value == "":
				self.inputValue.SetText("")
				self.__OnValueUpdate()
				ime.SetCursorPosition(0)
				return

		value=str(value)
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		ime.SetCursorPosition(len(value))

	if app.ENABLE_IKASHOP_RENEWAL:
		def SoftClose(self):
			self.Hide()
			for child in vars(self).values():
				if isinstance(child, ui.EditLine):
					if child.IsFocus():
						child.KillFocus()

	def GetText(self):
		return self.inputValue.GetText()

	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.inputValue)

		text = self.inputValue.GetText()

		if app.ENABLE_IKASHOP_RENEWAL:
			text = text.lower().replace("k", "000")

		money = 0
		if text and text.isdigit():
			try:
				if app.ENABLE_GOLD_LIMIT:
					money = min(1000000000000000, long(text))
				else:
					money = min(199999999, int(text))
			except ValueError:
				money = 1999999999

		self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(money))

if app.ENABLE_DROP_DIALOG_RENEWAL:
	class QuestionDropDialog(ui.ScriptWindow):
		NAME_COLOR = 0xffc79e65

		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.windowType = 0
			self.slotPos = 0
			self.cancelEvent = None
			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.HideToolTip()
			self.__CreateDialog()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def __CreateDialog(self):
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/questiondropdialog.py")
			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.itemName = self.GetChild("message_2")
			self.itemSlot = self.GetChild("ItemSlot")
			self.acceptButton = self.GetChild("accept")
			self.destroyButton = self.GetChild("destroy")
			self.cancelButton = self.GetChild("cancel")
			self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.__OverInItem))
			self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutItem))
			if not app.ENABLE_DESTROY_DIALOG:
				self.destroyButton.Hide()

		def SetItemSlot(self, windowType, slotPos, itemVnum, itemCount):
			self.windowType = windowType
			self.slotPos = slotPos
			item.SelectItem(itemVnum)
			self.itemName.SetText("%s x%d" % (item.GetItemName(), itemCount))
			self.itemName.SetPackedFontColor(self.NAME_COLOR)
			for index in xrange(3):
				self.itemSlot.ClearSlot(index)
			self.itemSlot.SetItemSlot(0, itemVnum, itemCount)
			self.itemSlot.RefreshSlot()

			if item.IsAntiFlag(item.ANTIFLAG_DROP):
				self.acceptButton.Disable()
			else:
				self.acceptButton.Enable()
			if app.ENABLE_DESTROY_DIALOG:
				if item.IsAntiFlag(item.ANTIFLAG_DESTROY):
					self.destroyButton.Disable()
				else:
					self.destroyButton.Enable()

		def SetText(self, text):
			self.message.SetText(text)

		def SetAcceptEvent(self, event):
			self.acceptButton.SetEvent(event)

		def SetDestroyEvent(self, event):
			self.destroyButton.SetEvent(event)

		def SetCancelEvent(self, event):
			self.cancelEvent = event
			self.cancelButton.SetEvent(event)

		def Open(self):
			self.SetCenterPosition()
			self.SetTop()
			self.Show()

		def Close(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()
			self.Hide()

		def Destroy(self):
			self.Close()
			self.ClearDictionary()
			self.cancelEvent = None
			self.tooltipItem = None

		def OnPressEscapeKey(self):
			if self.cancelEvent:
				self.cancelEvent()
			else:
				self.Close()
			return True

		def __OverInItem(self, slotIndex):
			if not self.tooltipItem:
				return
			if self.windowType == 0:
				self.tooltipItem.SetInventoryItem(self.slotPos)
			else:
				self.tooltipItem.SetInventoryItem(self.slotPos, self.windowType)

		def __OverOutItem(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()

class ItemQuestionDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

		self.tooltipItem = uiToolTip.ItemToolTip()
		self.window_type = 0
		self.count = 0
		self.height = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogitem.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")
		self.sellButton = self.GetChild("sell")
		if app.ENABLE_DESTROY_DIALOG:
			self.destroyButton = self.GetChild("destroy")

		self.titleBar = ui.TitleBar()
		self.titleBar.SetParent(self.board)
		self.titleBar.MakeTitleBar(254, "yellow")
		self.titleBar.SetPosition(8, 7)
		if app.ENABLE_DETAILS_UI:
			self.titleBar.CloseButtonHide()
		self.titleBar.Show()

		self.titleName = ui.TextLine()
		self.titleName.SetParent(self.titleBar)
		self.titleName.SetPosition(0, 4)
		self.titleName.SetWindowHorizontalAlignCenter()
		self.titleName.SetHorizontalAlignCenter()
		self.titleName.Show()

		self.slotList = []
		for i in xrange(3):
			slot = ui.ImageBox()
			slot.LoadImage("d:/ymir work/ui/public/slot_base.sub")
			slot.SetParent(self)
			slot.SetWindowHorizontalAlignCenter()
			self.slotList.append(slot)

	def Open(self, vnum, slot, type_w, text="", mode = 0):
		item.SelectItem(vnum)
		xSlotCount, ySlotCount = item.GetItemSize()
		self.window_type = type_w
		metinSlot = [player.GetItemMetinSocket(type_w, slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.count = player.GetItemCount(type_w, slot)

		if type_w == 20:
			del metinSlot[:]
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(shop.GetItemMetinSocket(slot, i))

		self.titleName.SetText(item.GetItemName())

		if text:
			textLine2 = ui.TextLine()
			textLine2.SetPosition(0, 80 + 32*ySlotCount)
			textLine2.SetWindowHorizontalAlignCenter()
			textLine2.SetHorizontalAlignCenter()
			textLine2.SetVerticalAlignCenter()
			textLine2.SetParent(self.board)
			textLine2.SetText(text)
			textLine2.Hide()
			self.textLine2 = textLine2
			self.textLine.SetText(text)

		slotGrid = ui.SlotWindow()
		slotGrid.SetParent(self)
		slotGrid.SetPosition(-16, 60)
		slotGrid.SetWindowHorizontalAlignCenter()
		slotGrid.AppendSlot(0, 0, 0, 32*xSlotCount, 32*ySlotCount)
		slotGrid.AddFlag("not_pick")
		slotGrid.Show()
		self.slotGrid = slotGrid

		if self.count > 1:
			self.slotGrid.SetItemSlot(0, vnum, self.count)
		else:
			self.slotGrid.SetItemSlot(0, vnum)

		if text:
			self.height -= 10

		self.SetSize(270, 110 + 8 + 32*ySlotCount + self.height)
		self.board.SetSize(270, 110 + 8 + 32*ySlotCount + self.height)
		self.board.AddFlag("not_pick")
		self.textLine.SetPosition(0, 42)

		for i in xrange(min(3, ySlotCount)):
			self.slotList[i].SetPosition(0, 28 + ySlotCount*32 - i*32)
			self.slotList[i].OnMouseOverIn = lambda arg = slot: self.OverInItem(arg)
			self.slotList[i].OnMouseOverOut = lambda arg = self.tooltipItem: self.OverOutItem(arg)
			self.slotList[i].Show()

		if type_w == 0:
			self.GetChild("accept").SetPosition(-94, 74 + 8 + 32*ySlotCount + self.height)
			self.GetChild("accept").SetToolTipText(localeInfo.TOOLTIP_ANTIFLAG_DROP)
			self.GetChild("cancel").SetPosition(93, 74 + 8+ 32*ySlotCount + self.height)
			self.GetChild("cancel").SetToolTipText(localeInfo.UI_CANCEL)
			self.GetChild("sell").SetPosition(-32, 74 + 9+ 32*ySlotCount + self.height)
			self.GetChild("sell").SetToolTipText(localeInfo.TOOLTIP_ANTIFLAG_SELL)
			if app.ENABLE_DESTROY_DIALOG:
				self.GetChild("destroy").SetPosition(31, 74 + 9+ 32*ySlotCount + self.height)
				self.GetChild("destroy").SetToolTipText(localeInfo.TOOLTIP_ANTIFLAG_DESTROY)
		else:
			self.GetChild("accept").SetPosition(-35, 74 + 8 + 32*ySlotCount + self.height)
			self.GetChild("cancel").SetPosition(35, 74 + 8+ 32*ySlotCount + self.height)

			if mode == 3:
				self.GetChild("accept").SetText(localeInfo.AUTO_BUY)
			else:
				self.GetChild("accept").SetText(localeInfo.AUTO_SELL)

		if app.ENABLE_DESTROY_DIALOG:
			if type_w == 20 or mode == 1 or mode == 2:
				self.GetChild("destroy").Hide()
			else:
				self.GetChild("destroy").Show()	

		if mode == 1:
			self.GetChild("accept").SetPosition(-35, 74 + 8 + 32*ySlotCount + self.height)
			self.GetChild("cancel").SetPosition(35, 74 + 8+ 32*ySlotCount + self.height)

		if mode == 2:
			self.GetChild("accept").SetPosition(-35, 74 + 8 + 32*ySlotCount + self.height)
			self.GetChild("accept").SetText(localeInfo.AUTO_SELL)
			self.GetChild("cancel").SetPosition(35, 74 + 8+ 32*ySlotCount + self.height)

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		if not type_w == 20 and item.IsAntiFlag(item.ANTIFLAG_DROP):
			self.GetChild("accept").Disable()

		if app.ENABLE_DESTROY_DIALOG:
			if not type_w == 20 and item.IsAntiFlag(item.ANTIFLAG_DESTROY):
				self.GetChild("destroy").Disable()

		if not type_w == 20 and item.IsAntiFlag(item.ANTIFLAG_SELL):
			self.GetChild("sell").Disable()

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def SetCloseEvent(self, event):
		self.titleBar.SetCloseEvent(event)

	def SetMessage(self, text):
		self.textLine.SetText(text)

	def OverInItem(self, slot):
		if self.window_type == 0:
			self.tooltipItem.SetInventoryItem(slot)
		elif self.window_type == 20:
			self.tooltipItem.SetShopItem(slot)
		else:
			self.tooltipItem.SetInventoryItem(slot, self.window_type)

	def OverOutItem(self, tooltipItem):
		if 0 != tooltipItem:
			self.tooltipItem.HideToolTip()
			self.tooltipItem.ClearToolTip()

	def Close(self):
		if self.tooltipItem and self.tooltipItem != 0:
			self.tooltipItem.HideToolTip()
			self.tooltipItem.ClearToolTip()
		
		self.ClearDictionary()
		self.slotList = []
		self.titleBar = None
		self.titleName = None
		self.textLine2 = None
		self.slotGrid = None
		self.tooltipItem = 0
		self.Hide()
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetAcceptEvent_Shop(self, event):
		self.acceptButton.SetEvent(event)

	if app.ENABLE_DESTROY_DIALOG:
		def SetDestroyEvent(self, event):
			self.destroyButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetSellEvent(self, event):
		self.sellButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()

		return TRUE

class OnlinePopup(ui.BorderB):
	def __init__(self):
		ui.BorderB.__init__(self)

		self.isActiveSlide = FALSE
		self.isActiveSlideOut = FALSE
		self.endTime = 0
		self.wndWidth = 0

		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.SetPosition(13, 0)
		self.textLine.Show()

		self.onlineImage = ui.ImageBox()
		self.onlineImage.SetParent(self)
		self.onlineImage.SetPosition(8, 8)
		self.onlineImage.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		self.onlineImage.Show()

	def __del__(self):
		ui.BorderB.__del__(self)

	def SlideIn(self):
		self.SetTop()
		self.Show()

		self.isActiveSlide = TRUE
		self.endTime = app.GetGlobalTimeStamp() + 5

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Close()

	def SetUserName(self, name):
		self.textLine.SetText(localeInfo.ONLINE_PLAYER_NOTICE % str(name))

		self.wndWidth = self.textLine.GetTextSize()[0] + 40
		self.SetSize(self.wndWidth, 25)
		self.SetPosition(-self.wndWidth, wndMgr.GetScreenHeight() - 200)

	def OnUpdate(self):
		if self.isActiveSlide and self.isActiveSlide == TRUE:
			x, y = self.GetLocalPosition()
			if x < 0:
				self.SetPosition(x + 4, y)

		if self.endTime - app.GetGlobalTimeStamp() <= 0 and self.isActiveSlideOut == FALSE and self.isActiveSlide == TRUE:
			self.isActiveSlide = FALSE
			self.isActiveSlideOut = TRUE

		if self.isActiveSlideOut and self.isActiveSlideOut == TRUE:
			x, y = self.GetLocalPosition()
			if x > -(self.wndWidth):
				self.SetPosition(x - 4, y)

			if x <= -(self.wndWidth):
				self.isActiveSlideOut = FALSE
				self.Close()

