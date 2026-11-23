# Ara:
if app.ENABLE_RENDER_TARGET:
	import uiRenderTarget

# Altina ekle:
if app.ENABLE_IKASHOP_RENEWAL:
	import uiikashop


# def __init__(self) icinde:
# Ara:
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.wndIkashopBusiness = None
			self.wndIkashopSearchShop = None
			if app.EXTEND_IKASHOP_ULTIMATE:
				self.wndIkashopShopSkin = None


# def __MakeWindows(self) icinde:
# Ara:
			self.wndSafebox = wndSafebox

		self.wndChatLog = wndChatLog

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.wndIkashopBusiness = uiikashop.IkarusShopBusinessBoard()
			self.wndIkashopSearchShop = uiikashop.IkarusSearchShopBoard()
			if app.EXTEND_IKASHOP_PRO:
				from _weakref import proxy
				self.wndIkashopSearchShop.SetOpenWhisper(lambda name, _s = proxy(self) : _s.OpenWhisperDialog(name))
				self.wndIkashopSearchShop.SetOpenWhisperText(lambda name, text, _s = proxy(self) : _s.OpenWhisperWithText(name, text))
			if app.EXTEND_IKASHOP_ULTIMATE:
				self.wndIkashopShopSkin = uiikashop.IkarusShopSkinBoard()


# def MakeHyperlinkTooltip(self, hyperlink) icinde:
# Ara:
			elif "wiki" == type:
				self.OpenWikiWindow()
				self.wndWiki.OpenRules()

# Altina ekle:
			elif "ikashop" == type and app.ENABLE_IKASHOP_RENEWAL:
				if len(tokens) > 1 and self.wndIkashopSearchShop and uiikashop.SEARCH_SHOP_RENEWAL:
					self.wndIkashopSearchShop.SearchSeller(":".join(tokens[1:]))
			elif "shop" == type and app.ENABLE_AUTO_CHAT:
				if len(tokens) > 1 and str(tokens[1]) != player.GetMainCharacterName():
					self.OpenWhisperDialog(str(tokens[1]))


# def Close(self) icinde:
# Ara:
			self.wndParty.Destroy()


		if self.wndCube:
			self.wndCube.Destroy()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.wndIkashopBusiness:
				self.wndIkashopBusiness.Destroy()
				self.wndIkashopBusiness = None
			if self.wndIkashopSearchShop:
				self.wndIkashopSearchShop.Destroy()
				self.wndIkashopSearchShop = None
			if app.EXTEND_IKASHOP_ULTIMATE:
				if self.wndIkashopShopSkin:
					self.wndIkashopShopSkin.Destroy()
					self.wndIkashopShopSkin = None


# def __HideWindows(self) icinde:
# Ara:
		if app.ENABLE_RANKING:
			if self.wndRanking:
				hideWindows += self.wndRanking,

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			hideWindows += self.wndIkashopBusiness, self.wndIkashopSearchShop
			if app.EXTEND_IKASHOP_ULTIMATE:
				hideWindows += self.wndIkashopShopSkin,


# class Interface(object) icinde:
# Ara:
		def OpenRenderTargetWindow(self, renderType = 0, renderVnum = 11299):
			self.MakeRenderTargetWindow()
			self.wndRenderTarget.Open(renderType, renderVnum)

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def ToggleIkashopBusinessBoard(self):
			self.wndIkashopBusiness.Toggle()

		def ToggleIkashopSearchShopBoard(self):
			self.wndIkashopSearchShop.Toggle()

		def SearchShopForItem(self, itemVnum):
			board = self.wndIkashopSearchShop
			if not itemVnum or not board:
				return
			import item
			item.SelectItem(itemVnum)
			itemName = item.GetItemName()
			if not itemName:
				board.Open()
				return
			board._OnClickResetFilters()
			board.inputNameEdit.SetText(itemName)
			board._OnClickSearchButton()
