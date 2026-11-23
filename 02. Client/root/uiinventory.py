# Ara:
if app.ENABLE_STYLE_ATTRIBUTE_SYSTEM:
	import uiAttachBonus

# Altina ekle:
if app.ENABLE_IKASHOP_RENEWAL:
	import ikashop


# def __BindReferenceButtons(self) icinde:
# Ara:
		self.GetChild("ManageInventory").SetEvent(ui.__mem_func__(self.ManageInventory))
		self.GetChild("StackInventoryButton").SetEvent(ui.__mem_func__(self.StackInventory))
		self.GetChild("MyShopButton").SetEvent(ui.__mem_func__(self.ClickMyShopButton))

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			shopButton = self.GetChild("MyShopButton")
			if shopButton.ToolTipText:
				shopButton.ToolTipText.Hide()
			shopButton.ToolTipText = None
			shopButton.SetShowToolTipEvent(ui.__mem_func__(self.__ShowShopButtonToolTip))
			shopButton.SetHideToolTipEvent(ui.__mem_func__(self.__HideShopButtonToolTip))


# def ApplyInventorySearch(self) icinde:
# Ara:
		if not self.wndItem:
			return
		text = self.searchText

# Altina ekle:
		ikashopSelling = False
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_PRO:
				board = ikashop.GetBusinessBoard()
				ikashopSelling = board and (board.IsShow() or board.IsCreatingAuction())


# def ApplyInventorySearch(self) icinde:
# Ara:
		text = self.searchText
		for i in xrange(player.INVENTORY_PAGE_SIZE):
			vnum = player.GetItemIndex(self.__InventoryLocalSlotPosToGlobalSlotPos(i))

# Altina ekle:
			if ikashopSelling and vnum:
				item.SelectItem(vnum)
				if item.IsAntiFlag(item.ANTIFLAG_GIVE) or item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
					self.wndItem.DisableSlot(i)
					continue


# def ClickMyShopButton(self) icinde:
# Ara:
				self.wndItem.DisableSlot(i)

	def ClickMyShopButton(self):

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.IsPressed(app.DIK_LALT) or app.IsPressed(app.DIK_RALT):
				board = ikashop.GetBusinessBoard()
				name = ""
				if board:
					name = board.shopInfo.get('name', "")
				name = name or player.GetName()
				ime.PasteString("|cffffc700|Hikashop:%s|h[%s]|h|r" % (name, localeInfo.IKASHOP_SHOP_LINK_TEXT % name))
				return
			if self.interface:
				self.interface.ToggleIkashopBusinessBoard()

	if app.ENABLE_IKASHOP_RENEWAL:
		def __ShowShopButtonToolTip(self):
			if not self.shopButtonToolTip:
				self.shopButtonToolTip = uiToolTip.ToolTip()
			tip = self.shopButtonToolTip
			tip.ClearToolTip()
			tip.AutoAppendTextLine(localeInfo.IKASHOP_BUSINESS_BOARD_TITLE)
			tip.AppendSpace(4)
			tip.AutoAppendTextLine(localeInfo.IKASHOP_BUSINESS_BOARD_LINK_TOOLTIP)
			tip.AlignHorizonalCenter()
			tip.ShowToolTip()

		def __HideShopButtonToolTip(self):
			if self.shopButtonToolTip:
				self.shopButtonToolTip.HideToolTip()


# def ShowToolTip(self, slotIndex) icinde:
# Ara:
	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetInventoryItem(slotIndex)

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL:
				board = ikashop.GetBusinessBoard()
				if board and (board.IsShow() or board.IsCreatingAuction()):
					item.SelectItem(player.GetItemIndex(player.INVENTORY, slotIndex))
					if not item.IsAntiFlag(item.ANTIFLAG_GIVE) and not item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
						self.tooltipItem.AppendTextLine(localeInfo.IKASHOP_BUSINESS_SELL_ITEM_TOOLTIP)


# def UseItemSlot(self, slotIndex) icinde:
# Ara:
			return

		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			board = ikashop.GetBusinessBoard()
			if board:
				item.SelectItem(player.GetItemIndex(player.INVENTORY, slotIndex))
				if not item.IsAntiFlag(item.ANTIFLAG_GIVE) and not item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
					if board.IsCreatingAuction():
						ikashop.AddItemOnAuction(player.INVENTORY, slotIndex)
						return
					elif board.IsShow():
						ikashop.AddItemOnShop(player.INVENTORY, slotIndex)
						return

			if app.EXTEND_IKASHOP_ULTIMATE:
				itemVnum = player.GetItemIndex(player.INVENTORY, slotIndex)
				if itemVnum == 52000:
					shopSkinBoard = ikashop.GetShopSkinBoard()
					if shopSkinBoard:
						shopSkinBoard.Open()
					return
				elif itemVnum == 51998:
					if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
						for i in xrange(min(player.GetItemCount(player.INVENTORY, slotIndex), 10)):
							self.__UseItem(slotIndex)
						self.OverOutItem()
						return

		if (app.ENABLE_IKASHOP_RENEWAL and self.interface and
			(app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)) and
			not (app.IsPressed(app.DIK_LALT) or app.IsPressed(app.DIK_RALT)) and
			not app.IsPressed(app.DIK_X) and not shop.IsOpen() and
			not exchange.isTrading() and not mouseModule.mouseController.isAttached()):
			itemVnum = player.GetItemIndex(slotIndex)
			if itemVnum:
				self.interface.SearchShopForItem(itemVnum)
				return
