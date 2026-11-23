# def __init__(self) icinde:
# Ara:
		if app.ENABLE_BIOLOG_RENEWAL:
			self.tooltipBiologist = MiniMapButtonToolTip()
			self.tooltipBiologist.SetText(localeInfo.MINIMAP_TOOLTIP_BIOLOGIST)

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.tooltipShopSearch = MiniMapButtonToolTip()
			self.tooltipShopSearch.SetText(localeInfo.MINIMAP_TOOLTIP_SHOP_SEARCH)


# def __Initialize(self) icinde:
# Ara:
		self.tooltipDungeonInfo = 0
		self.tooltiprank = 0
		self.btnRank = 0

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.shopSearchButton = 0
			self.tooltipShopSearch = 0


# def __LoadWindow(self) icinde:
# Ara:
			if app.__DUNGEON_INFO__:
				self.btnDungeonSystem = self.GetChild("DungeonSystemButton")

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				self.shopSearchButton = self.GetChild("PortableSearchButton")


# def __LoadWindow(self) icinde:
# Ara:
		if app.__DUNGEON_INFO__:
			self.btnDungeonSystem.SetEvent(ui.__mem_func__(self.OpenTableDungeonInfo))

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.shopSearchButton.SetEvent(ui.__mem_func__(self.OpenShopSearch))


# def __LoadWindow(self) icinde:
# Ara:
			if self.BiologistButton:
				(ButtonPosX, ButtonPosY) = self.BiologistButton.GetGlobalPosition()
				self.tooltipBiologist.SetTooltipPosition(ButtonPosX, ButtonPosY)

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.shopSearchButton:
				(ButtonPosX, ButtonPosY) = self.shopSearchButton.GetGlobalPosition()
				self.tooltipShopSearch.SetTooltipPosition(ButtonPosX, ButtonPosY)


# def OnUpdate(self) icinde:
# Ara:
				self.tooltipBiologist.Show()
			else:
				self.tooltipBiologist.Hide()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if self.shopSearchButton and True == self.shopSearchButton.IsIn():
				self.tooltipShopSearch.Show()
			else:
				self.tooltipShopSearch.Hide()


# class MiniMap(ui.ScriptWindow) icinde:
# Ara:
		def OpenBiologist(self):
			if self.interface:
				self.interface.ToggleBiologistWindow()

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def OpenShopSearch(self):
			if self.interface:
				self.interface.ToggleIkashopSearchShopBoard()
