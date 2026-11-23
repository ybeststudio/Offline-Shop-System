# def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY) icinde:
# Ara:
				itemVnum = player.GetItemIndex(player.INVENTORY, slotIndex)

		self.ClearToolTip()

# Altina ekle:
		if window_type == player.INVENTORY and (app.ENABLE_IKASHOP_RENEWAL or app.ENABLE_WIKI_SYSTEM):
			self.toolTipWidth = max(self.toolTipWidth, 310)
			self.ResizeToolTip()


# def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY) icinde:
# Ara:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, window_type, slotIndex, 0, set_value)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, window_type, slotIndex, 0, set_value)

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				if itemVnum == 51998:
					self.AppendTextLine(localeInfo.IKASHOP_ULTIMATE_SHOP_PRIVATE_KEY_MULTIUSE_TOOLTIP)


# def SetShopItemMultiPrice(self, slotIndex) icinde:
# Ara:
			item.SelectItem(itemVnum)
			if item.IsFlag(item.ITEM_FLAG_STACKABLE):
				rows.append((("alt", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_MULTI_BUY_SHOP))

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))


# def SetShopItemMultiPrice(self, slotIndex) icinde:
# Ara:
				rows.append((("alt", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_MULTI_BUY_SHOP))
			if app.ENABLE_WIKI_SYSTEM:
				rows.append((("ctrl", "alt", "mouse_left"), localeInfo.TOOLTIP_SHORTCUT_WIKI))

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				for (n, vnum) in enumerate([v for (v, c) in prices if v != 1][:5]):
					item.SelectItem(vnum)
					rows.append((("ctrl", str(n + 1)), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH_PRICE % item.GetItemName()))


# class ItemToolTip(ToolTip) icinde:
# Ara:
		if magicDefencePower > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_DEF_POWER % magicDefencePower, self.GetChangeTextLineColor(magicDefencePower))

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def AppendAttributes(self, attrs):
			attrs = list(attrs)
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM - len(attrs)):
				attrs.append((0,0))
			self.__AppendAttributeInformation(attrs)


# def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0, window_type = player.INVENTORY, slotIndex = -1, window_open = 0, set_value = 0) icinde:
# Ara:
		if slotIndex >= 0 and window_type == player.INVENTORY and not self.isShopItem:
			shortcutRows = []

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				shortcutRows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))


# def AppendCompanionShortcutTable(self) icinde:
# Ara:
		def AppendCompanionShortcutTable(self):
			rows = []

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))
