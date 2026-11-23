# def __OnRightClickItemSlot(self, slotIndex) icinde:
# Ara:
		entry = self.__GetEntryBySlot(slotIndex)
		if not entry:
			return

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL and self.interface and self.__IsCtrl() and not self.__IsAlt():
			self.interface.SearchShopForItem(entry.vnum)
			return


# def __AppendShortcuts(self, tooltip) icinde:
# Ara:
	def __AppendShortcuts(self, tooltip):
		rows = []

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))
