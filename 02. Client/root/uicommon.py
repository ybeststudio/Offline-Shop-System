# def __init__(self) icinde:
# Ara:
class PopupDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.autocloseTime = None


# class PopupDialog(ui.ScriptWindow) icinde:
# Ara:
	def OnIMEReturn(self):
		self.Close()
		return TRUE

# Altina ekle:
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


# def __CreateDialog(self) icinde:
# Ara:
		self.inputValue.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.moneyText = getObject("MoneyValue")

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.inputValue.numberMode = False
			if app.EXTEND_IKASHOP_ULTIMATE:
				self.priceAverage = None


# class MoneyInputDialog(ui.ScriptWindow) icinde:
# Ara:
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

# Altina ekle:
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


# def Close(self) icinde:
# Ara:
		self.cancelButton = None
		self.inputValue = None
		self.Hide()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				if self.priceAverage:
					self.priceAverage.Destroy()
				self.priceAverage = None


# def SetValue(self, value) icinde:
# Ara:
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if value == "":
				self.inputValue.SetText("")
				self.__OnValueUpdate()
				ime.SetCursorPosition(0)
				return


# class MoneyInputDialog(ui.ScriptWindow) icinde:
# Ara:
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		ime.SetCursorPosition(len(value))

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def SoftClose(self):
			self.Hide()
			for child in vars(self).values():
				if isinstance(child, ui.EditLine):
					if child.IsFocus():
						child.KillFocus()


# def __OnValueUpdate(self) icinde:
# Ara:
		ui.EditLine.OnIMEUpdate(self.inputValue)

		text = self.inputValue.GetText()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			text = text.lower().replace("k", "000")
