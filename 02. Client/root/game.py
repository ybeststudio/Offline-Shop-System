# def Open(self) icinde:
# Ara:
		self.cubeInformation = {}
		self.currentCubeNPC = 0

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				self.affectShower.SetSearchShopBoard(self.interface.wndIkashopSearchShop)


# class GameWindow(ui.ScriptWindow) icinde:
# Ara:
		def OpenRanking(self):
			if self.interface:
				self.interface.OpenRanking()

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		def __AnkaOpenShopResult(self, result):
			if str(result) == "0":
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.WHISPER_MESSENGER_NO_SHOP)

		def __IkashopSold(self, vnum):
			if self.interface and self.interface.wndShopSoldNotice:
				self.interface.wndShopSoldNotice.ShowSold(int(vnum))
			import advanced_option_notifications
			item.SelectItem(int(vnum))
			advanced_option_notifications.Record("market_sales", localeInfo.DROP_INFO_SHOP_SOLD % item.GetItemName())


# def __BuildKeyDict(self) icinde:
# Ara:
		if app.ENABLE_TRACK_WINDOW:
			onPressKeyDict[app.DIK_F10]	= lambda : self.interface.OpenDungeonInfo()

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			onPressKeyDict[app.DIK_F12]	= lambda : self.interface.ToggleIkashopSearchShopBoard()


# def __ServerCommand_Build(self) icinde:
# Ara:
			serverCommandList["PetSkillSlotResult"] = self.PetSkillSlotResult
		if app.ENABLE_TELEPORT_MAP_WINDOW:
			serverCommandList["TeleportMapResult"] = self.__TeleportMapResult

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			serverCommandList["ikashop_sold"] = self.__IkashopSold
			serverCommandList["AnkaOpenShopResult"] = self.__AnkaOpenShopResult
