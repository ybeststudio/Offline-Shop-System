# def __CheckPriceSearchKeys(self) icinde:
# Ara:
				pressed = 5
		if pressed and pressed != self.priceSearchKey and pressed <= len(items):
			interface = self.interface

# Altina ekle:
			if interface and app.ENABLE_IKASHOP_RENEWAL:
				interface.SearchShopForItem(items[pressed - 1])


# def OnUpdate(self) icinde:
# Ara:
		self.priceSearchKey = pressed

	def OnUpdate(self):

# Altina ekle:
		if app.ENABLE_SHOPEX_EXTRA_PRICE and app.ENABLE_IKASHOP_RENEWAL:
			self.__CheckPriceSearchKeys()
