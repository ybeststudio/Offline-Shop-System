# def SetBlessing(self, index) icinde:
# Ara:
		self.AppendSpace(2)
		self.AppendTextLine(localeInfo.GUILD_WINDOW_BLESSING_DURATION, BLESSING_TIME_COLOR)
		rows = []

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))


# def OnOverInDonation(self, index) icinde:
# Ara:
		for line in localeInfo.GUILD_SKILL_DONATION_ITEM_DESC.split("#"):
			tooltip.AppendTextLine(line, BLESSING_DESC_COLOR)
		rows = []

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))


# def OnOverInItem(self, vnum, count, price, kind, locked) icinde:
# Ara:
		tooltip.toolTipWidth = SHOP_TOOLTIP_WIDTH
		tooltip.AddItemData(vnum, [0, 0, 0, 0, 0, 0], 0)
		rows = []

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			rows.append((("ctrl", "mouse_right"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))
