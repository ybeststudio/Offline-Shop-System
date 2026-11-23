# def __OnItemShortcut(self, eventName = "left", click = 0, itemIdx = 0) icinde:
# Ara:
		vnum = self.GetCapeVnum()
		if ctrl and alt and app.ENABLE_WIKI_SYSTEM:
			interface.SearchWikiForItem(vnum)

# Altina ekle:
		elif ctrl and not alt and app.ENABLE_IKASHOP_RENEWAL:
			interface.SearchShopForItem(vnum)


# def __OverInItem(self, slotIndex = 0) icinde:
# Ara:
		cost = "{:,}".format(CAPE_COST).replace(",", ".")
		tt.AppendTextLine(localeInfo.BRAVE_CAPE_TOOLTIP_COST % cost + " |Eemoji/money_icon|e", tt.COLOR_TEXT_SHORTCUT)
		rows = []

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			rows.append((("ctrl", "mouse_left"), localeInfo.TOOLTIP_SHORTCUT_SHOP_SEARCH))
