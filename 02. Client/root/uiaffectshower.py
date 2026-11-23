# class AffectShower(ui.Window) icinde:
# Ara:
	if app.ENABLE_SUNG_MAHI_TOWER:
		AFFECT_DATA_DICT[chr.NEW_AFFECT_SUNG_MAHI_CURSE] = (localeInfo.SUNG_MAHI_CURSE_TOOLTIP, "d:/ymir work/ui/skill/common/affect/sungmahee_tower_debuff.sub",)

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		if app.EXTEND_IKASHOP_ULTIMATE:
			AFFECT_DATA_DICT[chr.NEW_AFFECT_SEARCH_SHOP_PREMIUM] = (localeInfo.IKASHOP_ULTIMATE_PREMIUM_AFFECT_DESCRIPTION, "ikashop/ultimate/search_shop_preium_affect.png")


# def __init__(self) icinde:
# Ara:
		self.multiFarmPremiumSlots = 0
		ui.Window.__init__(self)
		self.isShowingAffects = True

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			self.searchShopBoard = None


# class AffectShower(ui.Window) icinde:
# Ara:
				image.toolTip.HideToolTip()
		self.affectImageDict = self.living_affectImageDict
		self.__ArrangeImageList()

# Altina ekle:
	if app.ENABLE_IKASHOP_RENEWAL:
		if app.EXTEND_IKASHOP_ULTIMATE:
			def SetSearchShopBoard(self, board):
				from _weakref import proxy
				self.searchShopBoard = proxy(board)


# def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration, castStat = 0) icinde:
# Ara:
				self.skillAffectCastStat[type] = castStat
			self.__RefreshSkillAffectToolTip(type)
			return

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				if type == chr.NEW_AFFECT_SEARCH_SHOP_PREMIUM and self.searchShopBoard is not None:
					self.searchShopBoard.ActiveSortByPriceFeature()


# def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration, castStat = 0) icinde:
# Ara:
				print "except Aff auto potion affect ", e
				pass

		else:

# Altina ekle:
			isIkashopPremium = False
			if app.ENABLE_IKASHOP_RENEWAL:
				if app.EXTEND_IKASHOP_ULTIMATE:
					isIkashopPremium = (affect == chr.NEW_AFFECT_SEARCH_SHOP_PREMIUM)
			if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY and not isIkashopPremium:
				if isinstance(description, str) or isinstance(description, unicode):
					try:
						if '%' in description:
							placeholder_count = description.count('%') - description.count('%%')
							if placeholder_count > 0:
								description = description % float(value)
							else:
								description = description + " " + str(float(value))
						else:
							description = description + " " + str(float(value))
					except (TypeError, ValueError):
						description = str(description)
				else:
					description = description(float(value))


# def BINARY_NEW_RemoveAffect(self, type, pointIdx) icinde:
# Ara:
			affect = self.DEW_EX_DESC_IDX_START + pointIdx
		else:
			affect = type

# Altina ekle:
		if app.ENABLE_IKASHOP_RENEWAL:
			if app.EXTEND_IKASHOP_ULTIMATE:
				if type == chr.NEW_AFFECT_SEARCH_SHOP_PREMIUM and self.searchShopBoard is not None:
					self.searchShopBoard.DeactiveSortByPriceFeature()
