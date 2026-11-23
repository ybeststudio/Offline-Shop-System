# def __init__(self, layer = "UI") icinde:
# Ara:
		self.statusDefaultPos = None
		self.onMouseLeftButtonUpEvent = None
		self.onRunMouseWheelEvent = None

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.mouseWheelEvent = None


# class Window(object) icinde:
# Ara:
	def SetOnRunMouseWheelEvent(self, event):
		self.onRunMouseWheelEvent = event

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def SetMouseWheelEvent(self, event):
			self.mouseWheelEvent = event


# def OnRunMouseWheel(self, nLen) icinde:
# Ara:
		if self.onRunMouseWheelEvent:
			apply(self.onRunMouseWheelEvent, (bool(nLen < 0), ))
			return TRUE

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.mouseWheelEvent:
				return bool(self.mouseWheelEvent(nLen))


# class TextLine(Window) icinde:
# Ara:
	def GetTextSize(self):
		return wndMgr.GetTextSize(self.hWnd)

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def FitText(self):
			self.SetSize(*self.GetTextSize())


# def __init__(self) icinde:
# Ara:
		self.useIME = TRUE

		self.bCodePage = FALSE

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.updateEvent = None


# class EditLine(TextLine) icinde:
# Ara:
	def SetTabEvent(self, event):
		self.eventTab = event

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def SetFocusUpdateEvent(self, event):
			self.updateEvent = event


# def OnSetFocus(self) icinde:
# Ara:
			ime.DisableIME()
		wndMgr.ShowCursor(self.hWnd, TRUE)
		self.__RefreshOverlay()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.updateEvent:
				self.updateEvent(True)


# def OnKillFocus(self) icinde:
# Ara:
		ime.DisableCaptureInput()
		wndMgr.HideCursor(self.hWnd)
		self.__RefreshOverlay()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.updateEvent:
				self.updateEvent(False)


# def OnIMEUpdate(self) icinde:
# Ara:
		self.__RefreshOverlay()

		if self.eventUpdate:
			self.eventUpdate()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.updateEvent:
				self.updateEvent(self.IsFocus())


# class ScrollBar(Window) icinde:
# Ara:
	def UpdateBarSlot(self):
		self.barSlot.SetPosition(0, self.SCROLLBAR_BUTTON_HEIGHT)
		self.barSlot.SetSize(self.GetWidth() - 2, self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2 - 2)

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def UpdateScrollbarLenght(self, scrollableSpace):
			minheight = self.GetHeight() - self.downButton.GetHeight()*2
			scrollable = max(minheight, scrollableSpace)
			scale = float(scrollable) / max(1, minheight)
			scale = 1.0 / max(1.0, scale)
			scale = max(0.08, scale)
			self.SetScrollStep(scale/3.0)
			self.SetMiddleBarSize(scale)
