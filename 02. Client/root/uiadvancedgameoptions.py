# def getOpt(name) icinde:
# Ara:
				sr_slider = getOpt("shop_range_slider")
				if sr_slider:

# Altina ekle:
					if app.ENABLE_IKASHOP_RENEWAL and app.EXTEND_IKASHOP_PRO:
						sr_slider.SetSliderPos((systemSetting.GetShopRangeView() - 600.0) / 4400.0)
					else:
						sr_slider.SetSliderPos(GetOptSetting("shop_range_pos", 1.0))


# def OnChangeShopRange(self) icinde:
# Ara:
		ctrl = window.GetChild2("shop_range_slider") if window else None
		if ctrl:
			SetOptSetting("shop_range_pos", ctrl.GetSliderPos())

# Altina ekle:
			if app.ENABLE_IKASHOP_RENEWAL and app.EXTEND_IKASHOP_PRO:
				systemSetting.SetShopRangeView(ctrl.GetSliderPos() * 4400.0 + 600)
